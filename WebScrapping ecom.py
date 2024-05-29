import requests
from bs4 import BeautifulSoup
import pandas as pd

proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "https://10.10.1.10:1080"
}

data = {'title': [], 'price': []}


url = "https://cottonking.com/collections/2-polo-t-shirts"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r = requests.get(url, headers=headers)
    
soup = BeautifulSoup(r.text, 'html.parser')

# print(soup.prettify())

title = soup.find_all(class_="product-card-title")
for titles in title:
  print(titles.get_text())
  data["title"].append(titles.get_text())
  

  
spans = soup.select("span.amount")
for span in spans:
  print(span.get_text())
  data["price"].append(span.get_text())
  
df = pd.DataFrame.from_dict(data)
df.to_csv("data.csv",index=False)