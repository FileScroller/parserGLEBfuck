from bs4 import BeautifulSoup as bs
import requests

def page_found(html):
    response = requests.get(html)
    if response.status_code == 200:
        print('ok | ' + html) 
    else:
        print('err | ' + html)

r = requests.get('https://avito.ru/')
soup = bs(r.content, 'lxml')
links = [item['href'] if item.get('href') is not None else item['src'] for item in soup.select('[href^="http"], [src^="http"]') ]

for url in links:
    page_found(url)
    links.append(url)


print('Я начал работу с GIT')