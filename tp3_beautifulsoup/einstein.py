import bs4
import requests

response = requests.get("https://fr.wikipedia.org/wiki/Albert_Einstein")
texte = response.text
html = bs4.BeautifulSoup(texte, "html.parser")
headings = html.findAll(['h1', 'h2', 'h3'])
headings.remove(headings[0])
i = 1
for heading in headings:
    tab = int(heading.name.split("h")[1])
    if tab == 1:
        print("1 " + heading.text)
    elif tab == 2:
        print("\t" * tab + f"1.{str(i)} " + heading.text)
        i += 1
        j = 1
    elif tab == 3:
        print("\t" * tab + f"1.{str(i-1)}.{j} " + heading.text)
        j += 1

    

    