from flask import Flask, jsonify,render_template,request,make_response,json
import re
from amazon import find_amazon
from bestbuy import find_bestbuy
from costco import find_costco
from walmart import find_walmart
from crawler_total import crawl
from database import *
from file import *
app = Flask(__name__)
db = False
try:
    #Connect to database
    database = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'V3cd6t%T1',
        database = 'crawler'
    )
    db = True
except:
    print('No database connected')

scrape_methods = {
    "amazon": find_amazon,
    "bestbuy": find_bestbuy,
    "costco": find_costco,
    "walmart": find_walmart
}

@app.route('/', methods = ['GET', 'POST'])
def index():
    min_value = 0.1  # Default minimum price
    max_value = 10000
    price_order = "lth"
    if request.method == 'GET':
        return render_template('index.html')
    
    if request.method == 'POST':
        # Read input form values
        name = request.form.get("name")
        key_name = name.replace(" ", "")
        min_value = float(request.form.get('min_price', 0.1))
        max_value = float(request.form.get('max_price', 10000))
        price_order = request.form.get('price_order', "lth")

        amazon = request.form.get("amazon", "false")
        bestbuy = request.form.get("bestbuy", "false")
        costco = request.form.get("costco", "false")
        walmart = request.form.get("walmart", "false")

        sellers = []
        products = []

        if amazon == "true":
            sellers.append("amazon")
        if bestbuy == "true":
            sellers.append("bestbuy")
        if costco == "true":
            sellers.append("costco")
        if walmart == "true":
            sellers.append("walmart")

        # Connect to database if available
        if db:
            # Check if the table exists, create if not
            data = read(database, f"""
                SELECT COUNT(*) FROM information_schema.tables 
                WHERE table_schema = DATABASE() AND table_name = '{key_name}';
            """)
            if not data[0][0]:
                add_table = f"""
                    CREATE TABLE {key_name} (
                        name VARCHAR(200),
                        price INT,
                        link VARCHAR(1000),
                        image VARCHAR(1000),
                        seller VARCHAR(10)
                    )
                """
                execute(database, add_table)

            # For each selected seller
            for seller in sellers:
                print(seller)
                has_product = read(database, f"SELECT * FROM {seller} WHERE product = '{key_name}'")
                if has_product:
                    product = read(database, f"SELECT * FROM {key_name} WHERE seller = '{seller}'")
                else:
                    method = scrape_methods.get(seller)
                    product = method(name)
                    execute(database, f"INSERT INTO {seller} VALUES ('{key_name}')")
                    for p in product:
                        insert_product(database, key_name, p)
                products.extend(product)

        else:
            # Use file fallback if no database
            for seller in sellers:
                print(seller)
                product = read_file(name, seller)
                if not product:
                    method = scrape_methods.get(seller)
                    product = method(name)
                    product.append(["Dummy", "999999999", "Product", "Is", seller])  # Dummy product to block re-search
                    write_file(name, product)
                products.extend(product)

        # Filter products by price
        qualified = []
        for product in products:
            if not isinstance(product[1], (int, float)):
                price = re.findall(r'\d+', product[1])
                if price:
                    product[1] = int(price[0])
                else:
                    product[1] = 0  # Default if no price found
            if min_value <= product[1] <= max_value:
                qualified.append(product)

        # Sort products
        if price_order == "htl":
            qualified.sort(reverse=True, key=lambda x: x[1])
        else:
            qualified.sort(key=lambda x: x[1])

        # Render results
        return render_template('index.html', products=qualified)



if __name__ == "__main__":
    app.run()

