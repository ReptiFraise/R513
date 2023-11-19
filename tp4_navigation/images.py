import selenium.webdriver # les pilotes des navigateurs
from selenium.webdriver.common.by import By # les modes de recherche des éléments
import time
import urllib
from urllib import request as request
import url_parser
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
start = time.time() # stocke la date courante système
options = selenium.webdriver.ChromeOptions()
driver = selenium.webdriver.Chrome(options=options)
url = "https://iut1.univ-grenoble-alpes.fr/actualites/"
driver.get(url)
time.sleep(1)
bouton = driver.find_element(By.ID, "tarteaucitronPersonalize2")
bouton.click()
liens = []
for i in range(1,135):
    Xpath = f'//*[@id="avec_nav_sans_encadres"]/div[2]/div/div/div/div/span/ul/li[{i}]/a[1]'
    lien = WebDriverWait(driver, 10).until( 
        EC.presence_of_element_located( 
            (By.XPATH, Xpath) 
        )
    )
    lien = driver.find_element(By.XPATH, Xpath)
    liens.append(lien.get_attribute('href'))
for lien in liens:
    try:
        driver.get(lien)
        Xpath = '//*[@id="avec_nav_avec_encadres"]/figure/img'
        image = WebDriverWait(driver, 10).until( 
        EC.presence_of_element_located( 
            (By.XPATH, Xpath) 
        )
    )
        url_image = image.get_attribute("src")
        details_url = url_parser.get_url(url_image)
        nom_image = details_url.file + ".jpg"
        urllib.request.urlretrieve(url_image, f"./tp4_navigation/images/{nom_image}")
    except:
        print("Image non trouvée")
    time.sleep(1)
driver.quit()
fin = time.time()
duree = fin - start
print(f"{duree:.1f} secondes écoulées pour l'exécution du script")