import mysql.connector


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
        db.rollback()