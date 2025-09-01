import requests
import re 
import url_manager
import urllib.request, urllib.error
from bs4 import BeautifulSoup
import io

import requests
import json

def fetch_pre_loaded(name, start=0):
    url = "https://search.costco.ca/api/apps/www_costco_ca/query/www_costco_ca_search"
    
    # Query parameters
    params = {
        'expoption': 'def',
        'q': name,
        'locale': 'en-CA',
        'start': start,
        'expand': 'false',
        'userLocation': 'ON',
        'loc': '802-bd,530-wh,559-dz,559-wm,792-wm,894_0-cwt,894_0-edi,894_0-membership,894_0-mpt,894_0-otw,894_0-spc,894_1-edi,894_1-mpt,946-dz,946-wm,9894-wcs,993-wm',
        'whloc': '530-wh',
        'fq': '{!tag=item_program_eligibility}item_program_eligibility:("ShipIt")'
    }
    
    # Headers
    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Content-Type': 'application/json',
        'Origin': 'https://www.costco.ca',
        'Referer': 'https://www.costco.ca/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'x-api-key': '134a4023-68d5-4138-8e03-8353667d5fb3'
    }
    
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse and return JSON response
        return response.json()
    
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        return None
    
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


def find_costco(name):
    products = []
    return products
    data = fetch_pre_loaded(name)
    
    if data:
        if 'response' in data and 'docs' in data['response']:
            for product in data['response']['docs']:
                name = product.get('name', 'N/A')
                price = product.get('item_location_pricing_salePrice', 'N/A')
                image = product.get('image', 'N/A')
                link = product.get('group_id', 'N/A')
                link = "https://www.costco.ca/" + name.lower().replace(" ", "-") + ".product."+ link + ".html"
                products.append([name,price,image,link,"costco"])
    if len(products)==0:
        root_url = "https://www.costco.ca/"+name+".html"
        headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        print("got")
        r = requests.get(root_url,headers=headers,timeout=30)
        print("got")
        soup = BeautifulSoup(r.text,"html.parser")
        product_divs = soup.findAll('div',class_='thumbnail')
        for div in product_divs:
            link_elem = div.find('a', class_="product-image-url")
            link = link_elem['href'] if link_elem else "N/A"
            
            price_elem = div.find('div', class_="price")
            price = price_elem.text.strip() if price_elem else "N/A"
                
            img_elem = div.find('img', class_="img-responsive")
            img_url = "N/A"
            name = "N/A"
            if img_elem:
                if "src" in img_elem.attrs:
                    img_url = img_elem['src']
                    name = img_elem['alt']
            if name != "N/A" and price != "N/A" and img_url != "N/A" and link != "N/A":
                products.append([name,extract_integer(price), img_url, link,"costco"])

    return products
# print("hell")
# print("o")