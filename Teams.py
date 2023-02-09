from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from time import sleep

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

sleep(2)

#Team = driver.find_element(By.XPATH, '//div[@class = "heading__name"]').text
results = driver.find_elements(By.XPATH, '//div[@title = "¡Haga click para detalles del partido!"]')

more_2matches = 0
less_2matches = 0

for result in results:
    
    driver.get(result)
    home_goals = int(driver.find_element(By.XPATH, '//div[@class = "event__score event__score--home"]').text)
    away_goals = int(driver.find_element(By.XPATH, '//div[@class = "event__score event__score--away"]').text)
    total_goals = home_goals + away_goals
    
    if total_goals > 2.5:
        more_2matches += 1
    else:
        less_2matches += 1
        
prob_more2 = round((more_2matches/len(results))*100, 2)
prob_less2 = round((less_2matches/len(results))*100, 2)

print(len(results))
print(f'mas de 2.5 = {prob_more2}%\nmenos de 2.5 = {prob_less2}%')