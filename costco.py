import requests
import re 
import url_manager
import urllib.request, urllib.error
from bs4 import BeautifulSoup
import io


product = input("Please enter your product: ")
product = product.replace(" ", "+")

root_url = "https://www.costco.ca/CatalogSearch?dept=All&keyword="+product
print(root_url)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
r = requests.get(root_url,headers=headers,timeout=30)
soup = BeautifulSoup(r.text,"html.parser")
fout = open("projects/applications/Commercial Crawler/source.txt","w",encoding="utf-8")
fout.write(r.text)
fout.close()



product_divs = soup.findAll('div',class_='thumbnail')
products = {}
for div in product_divs:
    link_elem = div.find('a', class_="product-image-url")
    link = link_elem['href'] if link_elem else "N/A"
    
    price_elem = div.find('div', class_="price")
    price = price_elem.text.strip() if price_elem else "N/A"
        
    # Find the image URL
    img_elem = div.find('img', class_="img-responsive")
    if img_elem:
        img_url = img_elem['src']
        name = img_elem['alt']
    else:
        img_url = "N/A"
        name = "N/A"
        
    # Add to the dictionary
    products[name] = [price, img_url, link]

    print(len(products))
print(products)      




