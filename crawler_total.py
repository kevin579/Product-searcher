import requests
import re 
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


def extract_integer(s):
    # Use regex to find all digits in the string
    if isinstance(s, int):
        return s
    if isinstance(s, float):
        return int(s)
    digits = re.findall(r'\d+', s)

    # Join all found digits into a single string and convert to integer
    if digits:
        return int(''.join(digits))
    else:
        return "N/A"  # Return None if no digits are found

def crawl(product):

    product1 = product.replace(" ", "+")

    root_url = "https://www.amazon.ca/s?k="+product1
    source = askURL(root_url)
    soup = BeautifulSoup(source,"html.parser")

    product_divs = soup.select('div.rush-component.s-featured-result-item.s-expand-height, div.sg-col-4-of-24.sg-col-4-of-12.s-result-item.s-asin.sg-col-4-of-16.sg-col.s-widget-spacing-small.sg-col-4-of-20')
    products = []
    for div in product_divs:
        link_elem = div.find('a', class_="a-link-normal s-no-outline")
        link = "https://www.amazon.ca" + link_elem['href'] if link_elem else "N/A"
        
        price_elem = div.find('span', class_="a-price-whole")
        price = extract_integer(price_elem.text.strip()) if price_elem else "N/A"
            
        img_elem = div.find('img', class_="s-image")
        if img_elem:
            img_url = img_elem['src']
            name = img_elem['alt']
            if name.strip()[:9] == "Sponsored":
                continue
        else:
            img_url = "N/A"
            name = "N/A"
        if name!="N/A" and price!="N/A" and img_url!="N/A" and link!="N/A":
            products.append([name,price, img_url, link,"amazon"])

    print("amazon done")
        


    product2 = product.replace(" ", "%20")
    root_url = "https://www.bestbuy.ca/api/v2/json/search?categoryid=&currentRegion=ON&include=facets%2C%20redirects&lang=en-CA&page=1&pageSize=24&path=&query="+product2+"&exp=labels%2Csearch_abtesting_personalization_delta%3Ab0&token=e4e83717807a04004f92be667b00000013350000e8rdo1qui3zmnha&contextId=&hasConsent=true&sortBy=relevance&sortDir=desc"
    source = askURL(root_url)
    soup = BeautifulSoup(source,"html.parser")
    data = json.loads(str(soup))


    for p in data['products']:
        if p['name'] != "N/A" and p['salePrice'] != "N/A" and p['thumbnailImage'] != "N/A" and p['productUrl'] != "N/A":
            products.append([p['name'],extract_integer(p['salePrice']),p['thumbnailImage'],"https://www.bestbuy.ca/" + p['productUrl'],"bestbuy"])

    print("bestbuy done")


    # product3 = product.replace(" ", "+")
    # root_url = "https://www.costco.ca/CatalogSearch?dept=All&keyword="+product3
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    # }
    # r = requests.get(root_url,headers=headers,timeout=30)
    # soup = BeautifulSoup(r.text,"html.parser")
    # product_divs = soup.findAll('div',class_='thumbnail')
    # for div in product_divs:
    #     link_elem = div.find('a', class_="product-image-url")
    #     link = link_elem['href'] if link_elem else "N/A"
        
    #     price_elem = div.find('div', class_="price")
    #     price = price_elem.text.strip() if price_elem else "N/A"
            
    #     img_elem = div.find('img', class_="img-responsive")
    #     img_url = "N/A"
    #     name = "N/A"
    #     if img_elem:
    #         if "src" in img_elem.attrs:
    #             img_url = img_elem['src']
    #             name = img_elem['alt']

    #     # if name != "N/A" and price != "N/A" and img_url != "N/A" and link != "N/A":
    #     products.append([name,extract_integer(price), img_url, link,"costco"])

    
    # print("costco done")
    product4 = product.replace(" ", "+")

    root_url = "https://www.walmart.ca/en/search?q="+product4
    source = askURL(root_url)
    soup = BeautifulSoup(source,"html.parser")
    product_divs = soup.findAll('div',class_='mb0 ph0-xl pt0-xl bb b--near-white w-25 pb3-m ph1')
    for div in product_divs:
        link_elem = div.find('a', class_="absolute w-100 h-100 z-1 hide-sibling-opacity")
        link = "https://www.walmart.ca" + link_elem['href'] if link_elem else "N/A"
        
        price_elem = div.find('span', class_="w_q67L")
        price = price_elem.text.strip() if price_elem else "N/A"
            
        img_elem = div.find('img', class_="absolute top-0 left-0")
        if img_elem:
            img_url = img_elem['src']
            name = img_elem['alt']
        else:
            img_url = "N/A"
            name = "N/A"
            
        # Add to the dictionary
        # if name != "N/A" and price != "N/A" and img_url != "N/A" and link != "N/A":
        products.append([name,extract_integer(price), img_url, link,"walmart"])

    print("walmart done")
    return products

