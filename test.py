import requests

url = 'http://localhost:8000/crawler_class'
myobj = {
    'crawler_type': 'product',
    'site_name': 'amazon.in'
}

x = requests.post(url, json = myobj)
print(x.text)
