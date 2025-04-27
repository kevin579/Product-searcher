import mysql.connector

def execute(db, query):
    """
    Execute a non-query SQL statement (e.g., CREATE, UPDATE, DELETE).

    Args:
        db (mysql.connector.connection_cext.CMySQLConnection): 
            An active MySQL database connection.
        query (str): 
            A SQL query string to execute.

    Returns:
        None

    Raises:
        mysql.connector.Error: 
            If a database-related error occurs during execution.
    """
    cursor = db.cursor()
    cursor.execute(query)
    db.commit()
    cursor.close()

def read(db, query):
    """
    Execute a SQL query that retrieves data (e.g., SELECT) and returns the results.

    Args:
        db (mysql.connector.connection_cext.CMySQLConnection): 
            An active MySQL database connection.
        query (str): 
            A SQL SELECT query string.

    Returns:
        tuple: 
            A tuple containing the fetched rows. 
            Returns an empty tuple if no results are found.

    Raises:
        mysql.connector.Error: 
            If a database-related error occurs during query execution.
    """
    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result if result else tuple()

def insert_product(db, table_name, product_data):
    """
    Insert a new product record into the specified table.

    Args:
        db (mysql.connector.connection_cext.CMySQLConnection): 
            An active MySQL database connection.
        table_name (str): 
            The name of the table to insert the product into.
        product_data (list or tuple): 
            A collection containing the following five elements in order:
            - title (str): The product's title.
            - price (float or str): The product's price.
            - image_url (str): URL to the product's image.
            - product_url (str): URL to the product's page.
            - seller (str): The product's seller information.

    Returns:
        None

    Raises:
        Exception: 
            Prints an error message if insertion fails and rolls back the transaction.
    """
    query = f"INSERT INTO {table_name} VALUES (%s, %s, %s, %s, %s)"
    try:
        cursor = db.cursor()
        cursor.execute(query, (
            product_data[0],  # title
            product_data[1],  # price
            product_data[2],  # image_url
            product_data[3],  # product_url
            product_data[4]   # seller
        ))
        db.commit()
    except Exception as e:
        print(f"Error inserting data: {e}")
        db.rollback()
    finally:
        cursor.close()
