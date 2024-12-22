from flask import Flask, jsonify,render_template,request,make_response,json
from crawler_total import crawl
import mysql.connector

app = Flask(__name__)

#Connect to database
database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'V3cd6t%T1',
    database = 'crawler'
)
print("connected")
def execute(db, query):
    cursor = db.cursor()
    cursor.execute(query)
    db.commit()
    cursor.close()
def read(db, query):
    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result if result else tuple()

# print(read(database, 'show tables;'))

def insert_product(db, table_name, product_data):
    query = f"INSERT INTO {table_name} VALUES (%s, %s, %s, %s,%s)"
    try:
        cursor = db.cursor()
        cursor.execute(query, (
            product_data[0],  # title
            product_data[1],  # price
            product_data[2],  # image_url
            product_data[3],   # product_url
            product_data[4]     #seller
        ))
        db.commit()
    except Exception as e:
        print(f"Error inserting data: {e}")
        database.rollback()

@app.route('/', methods = ['GET', 'POST'])
def index():
    min_value = 0.1  # Default minimum price
    max_value = 10000
    price_order = "lth"
    orders = {"lth":"", "htl":"desc"}
    if request.method == 'GET':
        return render_template('index.html')
    
    if request.method =='POST':
        name = request.form.get("name")
        key_name = name.replace(" ", "")
        min_value = float(request.form.get('min_price', 0.1))
        max_value = float(request.form.get('max_price', 10000))
        price_order = request.form.get('price_order', "lth")
        amazon = request.form.get("amazon","false")
        bestbuy = request.form.get("bestbuy","false")
        costco = request.form.get("costco","false")
        walmart = request.form.get("walmart","false")
        sellers = []
        if amazon == "true":
            sellers.append("amazon")
        if bestbuy == "true":
            sellers.append("bestbuy")
        if costco == "true":
            sellers.append("costco")
        if walmart == "true":
            sellers.append("walmart")

        x = read(database, f"""Select count(*) from information_schema.tables where table_schema = Database() and table_name = '{key_name}';""")
        if x[0][0]:
            product = read(database, f"select * from {key_name} order by price {orders[price_order]};")
            product = [p for p in product if min_value <= p[1] <= max_value]
            print("product exit in database")
        else:
            product = crawl(name)
            add_table = f"""create table {key_name} (
                name varchar(200),
                price int,
                link varchar(1000),
                image varchar(1000),
                seller varchar(10)
                )
                """
            execute(database, add_table)
            for p in product:
                insert_product(database, key_name, p)

        product = [p for p in product if p[4] in sellers]

        return render_template('index.html',products = product)


if __name__ == "__main__":
    app.run()

