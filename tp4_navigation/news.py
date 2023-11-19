import selenium.webdriver # les pilotes des navigateurs
from selenium.webdriver.common.by import By # les modes de recherche des éléments
import time
options = selenium.webdriver.ChromeOptions()
driver = selenium.webdriver.Chrome(options=options)
url = "https://iut1.univ-grenoble-alpes.fr/"
driver.get(url)
time.sleep(3)
bouton = driver.find_element(By.ID, "tarteaucitronPersonalize2")
bouton.click()
liste_actus = driver.find_elements(By.CLASS_NAME, 'liste__objets__titre')
liens = []
liste_dicos = []
for actu in liste_actus:
    print(actu.text + " " + actu.get_attribute('href'))
    liens.append(actu.get_attribute('href'))
for url_actu in liens:
    dico = {}
    driver.get(url_actu)
    try:
        XPathT = f'//*[@id="avec_nav_avec_encadres"]/h1'
        XPathST = f'//*[@id="avec_nav_avec_encadres"]/div[2]/div/span'
        titre = driver.find_element(By.XPATH, XPathT)
        sous_titre = driver.find_element(By.XPATH, XPathST)
        dico["titre"] = titre.text
        dico["sous-titre"] = sous_titre.text
        liste_dicos.append(dico)
    except:
        print('Accès aux éléments impossibles')
print(dico)