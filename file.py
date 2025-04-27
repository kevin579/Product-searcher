def read_file(name, seller):
    """
    Read product data for a specific seller from a text file.

    Each product is expected to occupy five consecutive lines in the file:
    description, price, image URL, product link, and seller.

    Args:
        name (str): 
            The base name of the file (without extension) located in the 'data/' directory.
        seller (str): 
            The seller name to filter products by (e.g., 'amazon', 'bestbuy').

    Returns:
        list: 
            A list of products matching the specified seller, where each product is a list:
            [description (str), price (str), image URL (str), link (str), seller (str)].

    Notes:
        - If the file does not exist, it will be created as an empty file.
        - Only products matching the given seller are returned.

    Raises:
        IOError: 
            If there is an error opening or creating the file (silently handled).
    """
    products = []
    f_name = "data/" + name + ".txt"
    try:
        with open(f_name) as f:
            while 1:
                description = f.readline().strip("\n")
                if description == "":
                    break
                price = f.readline().strip("\n")
                image = f.readline().strip("\n")
                link = f.readline().strip("\n")
                seller_file = f.readline().strip("\n")
                if seller == seller_file:
                    products.append([description, price, image, link, seller])
    except:
        f = open(f_name, "x")
    f.close()
    return products

def write_file(name, products):
    """
    Append product data to a text file.

    Each product should be a list containing five elements:
    description, price, image URL, product link, and seller.

    Args:
        name (str): 
            The base name of the file (without extension) located in the 'data/' directory.
        products (list): 
            A list of products to write, where each product is a list of strings.

    Returns:
        None

    Notes:
        - If writing an element fails, 'NA' will be written instead.
    """
    f_name = "data/" + name + ".txt"
    with open(f_name, "a") as f:
        for product in products:
            product = [str(element) for element in product]
            for line in product:
                try:
                    f.write(line + "\n")
                except:
                    f.write("NA\n")
