from flask import Flask, jsonify,render_template,request,make_response,json
from crawler_total import crawl
# import mysql.connector
app = Flask(__name__)
# database = mysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     passwd = 'V3cd6t%T1',
#     database = 'crawler'
# )
# print("connected")
# def execute(db, query):
#     cursor = db.cursor()
#     cursor.execute(query)
#     db.commit()
#     cursor.close()
# def read(db, query):
#     cursor = db.cursor()
#     cursor.execute(query)
#     result = cursor.fetchall()
#     return result if result else tuple()

# read(database, 'select * from crawler')

# def insert_product(db, table_name, product_data):
#     query = f"INSERT INTO {table_name} VALUES (%s, %s, %s, %s)"
#     try:
#         cursor = db.cursor()
#         cursor.execute(query, (
#             product_data[0],  # title
#             product_data[1],  # price
#             product_data[2],  # image_url
#             product_data[3]   # product_url
#         ))
#         db.commit()
#     except Exception as e:
#         print(f"Error inserting data: {e}")
#         database.rollback()

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method =='POST':
        name = request.form.get("name")

        print(name)
        

        # numbers = len(product)

        # x = read(database, f"""Select count(*) from information_schema.tables where table_schema = Database() and table_name = '{name}';""")
        # if x[0][0]:
        #     product = read(database, f"select * from {name};")
        #     print(product)
        # else:
        #     product = crawl(name)
        #     add_table = f"""create table {name} (
        #         name varchar(200),
        #         price int,
        #         link varchar(1000),
        #         image varchar(1000)
        #         )
        #         """
        #     execute(database, add_table)
        #     for p in product:
        #         insert_product(database, name, p)
        product = crawl(name)
        return render_template('index.html',products = product)
        # return jsonify(d)


if __name__ == "__main__":
    app.run()

# merge_sort(product, 0, numbers - 1)
        #
        # removeLeft = numbers//3
        # removeRight = numbers*3//4
        # product = product[removeLeft:removeRight]
        # totalPrice = 0
        # for p in product:
        #     totalPrice+=p[1]
        # averagePrice = totalPrice/len(product)
        # print(averagePrice)
        # goodproduct = []
        # for p in product:
        #     if p[1] > averagePrice/5 and p[1]<averagePrice*2:
        #         goodproduct.append(p)
        # execute(database, add_table)