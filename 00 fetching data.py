import requests

proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "https://10.10.1.10:1080",
}


def fecthAndSaveToFile(url,path):
    r = requests.get(url)
    with open(path,"w")as f:
        f.write(r.text)
    
url = "https://timesofindia.indiatimes.com/sports"

fecthAndSaveToFile(url,"data/times.html")