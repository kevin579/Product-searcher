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

# product = input("Please enter your product: ").strip()
# product = product.replace(" ", "%20")
def find_bestbuy(product):
    product = product.replace(" ", "%20")
    root_url = "https://www.bestbuy.ca/api/v2/json/search?categoryid=&currentRegion=ON&include=facets%2C%20redirects&lang=en-CA&page=1&pageSize=24&path=&query="+product+"&exp=labels%2Csearch_abtesting_personalization_delta%3Ab0&token=e4e83717807a04004f92be667b00000013350000e8rdo1qui3zmnha&contextId=&hasConsent=true&sortBy=relevance&sortDir=desc"
    # fout = open("projects/applications/Commercial Crawler/source.txt","w",encoding="utf-8")
    source = askURL(root_url)
    # fout.write(source)
    # fout.close()
    soup = BeautifulSoup(source,"html.parser")
    # print(soup)
    data = json.loads(str(soup))

    # Extract the "sku" values from the "products" list
    products_info = [
        [
            product['name'],
            product['salePrice'],
            product['thumbnailImage'],
            "https://www.bestbuy.ca/" + product['productUrl'],
            "bestbuy"
            
        ]
        for product in data['products']
    ]

    return products_info

print(find_bestbuy("iphone 15"))

