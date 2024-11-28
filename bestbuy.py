import requests
import re 
import url_manager
import urllib.request, urllib.error
from bs4 import BeautifulSoup
import io
import json

def askURL(url):
    head = {  
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122  Safari / 537.36"
    }

    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html

product = input("Please enter your product: ").strip()
product = product.replace(" ", "%20")

root_url = "https://www.bestbuy.ca/api/v2/json/search?categoryid=&currentRegion=ON&include=facets%2C%20redirects&lang=en-CA&page=1&pageSize=24&path=&query="+product+"&exp=labels%2Csearch_abtesting_personalization_delta%3Ab0&token=e4e83717807a04004f92be667b00000013350000e8rdo1qui3zmnha&contextId=&hasConsent=true&sortBy=relevance&sortDir=desc"
fout = open("projects/applications/Commercial Crawler/source.txt","w",encoding="utf-8")
source = askURL(root_url)
fout.write(source)
fout.close()
soup = BeautifulSoup(source,"html.parser")
print(soup)
data = json.loads(str(soup))

# Extract the "sku" values from the "products" list
products_info = [
    {
        "name": product['name'],
        "productUrl": "https://www.bestbuy.ca/" + product['productUrl'],
        "thumbnailImage": product['thumbnailImage'],
        "regularPrice": product['regularPrice'],
        "salePrice": product['salePrice']
    }
    for product in data['products']
]

print(products_info)

# product_divs = soup.select('div.rush-component.s-featured-result-item.s-expand-height, div.sg-col-4-of-24.sg-col-4-of-12.s-result-item.s-asin.sg-col-4-of-16.sg-col.s-widget-spacing-small.sg-col-4-of-20')
# products = {}
# print(len(product_divs))
# for div in product_divs:
#     link_elem = div.find('a', class_="a-link-normal s-no-outline")
#     link = "https://www.amazon.ca" + link_elem['href'] if link_elem else "N/A"
    
#     price_elem = div.find('span', class_="a-price-whole")
#     price = price_elem.text.strip() if price_elem else "N/A"
        
#     # Find the image URL
#     img_elem = div.find('img', class_="s-image")
#     if img_elem:
#         img_url = img_elem['src']
#         name = img_elem['alt']
#     else:
#         img_url = "N/A"
#         name = "N/A"
        
#     # Add to the dictionary
#     products[name] = [price, img_url, link]

# print(len(products))
# print(products)      




