from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver import ActionChains

opts = Options()
opts.add_argument(
    "user-agent = Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
)

driver = webdriver.Chrome('./chromedriver.exe', chrome_options = opts)

driver.get('https://www.flashscore.co/equipo/arsenal/hA1Zm19f/resultados/')

sleep(3)

try:
    boton_cookies = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[@id = "onetrust-accept-btn-handler"]'))
    )

    boton_cookies.click()
except Exception as e:
    print(e)
    
action = ActionChains(driver)

sleep(2)

for i in range(3):
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[@class = "event__more event__more--static"]'))
    )    
    
    #link = driver.find_element(By.XPATH, '//div[@class = "sportName soccer"]/a[text() = "Mostrar más partidos"]')
    action.move_to_element(driver.find_element(By.XPATH, '//a[@class = "event__more event__more--static"]')).click().perform()
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@title = "¡Haga click para detalles del partido!"]'))
    )
    
    sleep(2)
#results = driver.find_elements(By.XPATH, '//div[@title = "¡Haga click para detalles del partido!"]')

#print(len(results))