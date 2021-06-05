import requests
from bs4 import BeautifulSoup

res=requests.get('https://news.ycombinator.com/')
soup=BeautifulSoup(res.text,'html.parser')
print(soup.body.contents)
print("my name")
print("what your name")
print("i am printing my name")
print("my choeses to add name")
