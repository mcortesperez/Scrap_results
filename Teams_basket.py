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

driver.get('https://www.flashscore.co/equipo/denver-nuggets/CxvW27TI/resultados/')

sleep(2)

try:
    boton_cookies = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[@id = "onetrust-accept-btn-handler"]'))
    )

    boton_cookies.click()
except Exception as e:
    print(e)

sleep(2)

Team = driver.find_element(By.XPATH, '//div[@class = "heading__name"]').text
results = driver.find_elements(By.XPATH, '//div[@title = "¡Haga click para detalles del partido!"]')

print('\n\n\t\t\t'+Team+'\n')

Total_Scores = []

for result in results:
    
    home_score = int(result.find_element(By.XPATH, './/div[@class = "event__score event__score--home"]').text)
    away_score = int(result.find_element(By.XPATH, './/div[@class = "event__score event__score--away"]').text)
    total_score = home_score + away_score
    Total_Scores.append(total_score)
    
score_limit = 218.5
    
while score_limit < 245.5:
    more = 0
    less = 0
    for x in Total_Scores:
        if x > score_limit:
            more += 1
        else:
            less += 1
    prob_more_result = round((more/len(Total_Scores))*100, 2)
    prob_less_result = round((less/len(Total_Scores))*100, 2)

    print('-------------------------------------------------------------------------')
    print(f'mas de {score_limit} = {prob_more_result}%\nmenos de {score_limit} = {prob_less_result}%\n')
    score_limit += 0.5
    
    
    
driver.get('https://www.flashscore.co/equipo/orlando-magic/QZMS36Dn/resultados/')

sleep(1)

Team = driver.find_element(By.XPATH, '//div[@class = "heading__name"]').text
results = driver.find_elements(By.XPATH, '//div[@title = "¡Haga click para detalles del partido!"]')

print('\n\n\t\t\t'+Team+'\n')

Total_Scores = []

for result in results:
    
    home_score = int(result.find_element(By.XPATH, './/div[@class = "event__score event__score--home"]').text)
    away_score = int(result.find_element(By.XPATH, './/div[@class = "event__score event__score--away"]').text)
    total_score = home_score + away_score
    Total_Scores.append(total_score)
    
score_limit = 218.5
    
while score_limit < 245.5:
    more = 0
    less = 0
    for x in Total_Scores:
        if x > score_limit:
            more += 1
        else:
            less += 1
    prob_more_result = round((more/len(Total_Scores))*100, 2)
    prob_less_result = round((less/len(Total_Scores))*100, 2)

    print('-------------------------------------------------------------------------')
    print(f'mas de {score_limit} = {prob_more_result}%\nmenos de {score_limit} = {prob_less_result}%\n')
    score_limit += 0.5