# 🛒 SmartShopper – Product Search & Comparison

SmartShopper is a **Python + Flask** web app with a simple **HTML5** frontend.  

Too many shopping websites and don’t know where to go?  
Lots of similar products and hard to decide which one to get?  
Have a favorite item and want to know who sells it cheapest?  

Enter a product name once, and **SmartShopper** will **scrape multiple mainstream shopping sites**, compare results, and return the **best-matched product for you** — no need to open individual listings.

---

## ✨ Features
- 🔎 **Unified search** — find products across multiple e-commerce sites with a single query  
- ⚙️ **Customizable sources** — search only on the websites you trust  
- 📊 **Smart ranking** — considers title match, price sanity, top rating, and availability  
- ⚡ **Fast search** — optimized scraping with `requests` + `BeautifulSoup` and lazy loading (up to 60% faster)  
- 🖥️ **Clean HTML5 UI** — simple, user-friendly interface  

---

## 🧰 Tech Stack
- **Backend:** Python 3.11 · Flask  
- **Frontend:** HTML5 · CSS · JavaScript  
- **Database:** MySQL — stores product data, cached results, and user history  
- **Security:** Flask-Session — secure session management and state handling  
- **Scraping:** `requests`, `beautifulsoup4`  

---

## 🔎 Supported Websites
- ✅ **Amazon**  
- ✅ **Costco**  
- ✅ **Best Buy**  
- ✅ **Walmart**  
- 🔄 **Canadian Tire** (in progress)  
- 🔄 **eBay** (in progress)  

---

## ⚠️ Disclaimer
This project is for **educational and personal use only**. Please respect the Terms of Service of all target websites before using in production.
