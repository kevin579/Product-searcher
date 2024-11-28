import requests
import re 
import url_manager
import urllib.request, urllib.error
from bs4 import BeautifulSoup
import io

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

product = input("Please enter your product: ")
product = product.replace(" ", "+")

root_url = "https://www.walmart.ca/en/search?q="+product
fout = open("projects/applications/Commercial_Crawler/source.txt","w",encoding="utf-8")
source = askURL(root_url)
fout.write(source)
fout.close()
soup = BeautifulSoup(source,"html.parser")


product_divs = soup.findAll('div',class_='mb0 ph0-xl pt0-xl bb b--near-white w-25 pb3-m ph1')
products = {}
# print(product_divs)
for div in product_divs:
    link_elem = div.find('a', class_="absolute w-100 h-100 z-1 hide-sibling-opacity")
    link = "https://www.walmart.ca" + link_elem['href'] if link_elem else "N/A"
    
    price_elem = div.find('span', class_="w_q67L")
    price = price_elem.text.strip() if price_elem else "N/A"
        
#     # Find the image URL
    img_elem = div.find('img', class_="absolute top-0 left-0")
    if img_elem:
        img_url = img_elem['src']
        name = img_elem['alt']
    else:
        img_url = "N/A"
        name = "N/A"
        
    # Add to the dictionary
    products[name] = [price, img_url, link]

# print(len(products))
print(products)      




