import bs4
import requests

response = requests.get('http://www.actel-ip.com/cwps/download_index/Firmware')
texte = response.text
html = bs4.BeautifulSoup(texte, 'html.parser')
tr = html.findAll('tr')
for t in tr:
    print(t.findAll('td')[2].text)
    
links = html.findAll('a')
for link in links:
    response = requests.get(link['href'])
    name = link['href'].split('/')[-1]
    print(name)
    with open(f"./download/{name}", "wb") as file:
        file.write(response.content)
