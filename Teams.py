from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from time import sleep

cont = 1.0
for i in range(30):
    porcentaje_tope = round(100/cont, 2)
    print('___________________________________')
    print(f'{round(cont, 1)}\t\t\t{porcentaje_tope}')
    cont += 0.1
print('\n\n\n')

opts = Options()
opts.add_argument(
    "user-agent = Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
)

driver = webdriver.Chrome('./chromedriver.exe', chrome_options = opts)

driver.get('')

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

Total_goals = []

cont_gg = 0
cont_NOgg = 0

for result in results:
    
    home_goals = int(result.find_element(By.XPATH, './/div[@class = "event__score event__score--home"]').text)
    away_goals = int(result.find_element(By.XPATH, './/div[@class = "event__score event__score--away"]').text)
    total_goals = home_goals + away_goals
    Total_goals.append(total_goals)
    
    if (home_goals!=0 and away_goals!=0):
        cont_gg += 1
    else:
        cont_NOgg += 1
        
prob_gg_result = round((cont_gg/len(results))*100, 2)
prob_NOgg_result = round((cont_NOgg/len(results))*100, 2)

print(f'Ambos marcan = {prob_gg_result}%\n(NO) ambos marcan = {prob_NOgg_result}%')
    
goals_limit = 0
    
while goals_limit < 5.5:
    more = 0
    less = 0
    for x in Total_goals:
        if x > goals_limit:
            more += 1
        else:
            less += 1
            
    prob_more_result = round((more/len(Total_goals))*100, 2)
    prob_less_result = round((less/len(Total_goals))*100, 2)

    print('-------------------------------------------------------------------------')
    print(f'mas de {goals_limit} = {prob_more_result}%\nmenos de {goals_limit} = {prob_less_result}%\n')
    goals_limit += 0.5
    
    
    
driver.get('')

sleep(1)

Team = driver.find_element(By.XPATH, '//div[@class = "heading__name"]').text
results = driver.find_elements(By.XPATH, '//div[@title = "¡Haga click para detalles del partido!"]')

print('\n\n\t\t\t'+Team+'\n')

Total_goals = []

cont_gg = 0
cont_NOgg = 0

for result in results:
    
    home_goals = int(result.find_element(By.XPATH, './/div[@class = "event__score event__score--home"]').text)
    away_goals = int(result.find_element(By.XPATH, './/div[@class = "event__score event__score--away"]').text)
    total_goals = home_goals + away_goals
    Total_goals.append(total_goals)
    
    if (home_goals!=0 and away_goals!=0):
        cont_gg += 1
    else:
        cont_NOgg += 1
        
prob_gg_result = round((cont_gg/len(results))*100, 2)
prob_NOgg_result = round((cont_NOgg/len(results))*100, 2)

print(f'Ambos marcan = {prob_gg_result}%\n(NO) ambos marcan = {prob_NOgg_result}%')
    
goals_limit = 0
    
while goals_limit < 5.5:
    more = 0
    less = 0
    for x in Total_goals:
        if x > goals_limit:
            more += 1
        else:
            less += 1
            
    prob_more_result = round((more/len(Total_goals))*100, 2)
    prob_less_result = round((less/len(Total_goals))*100, 2)

    print('-------------------------------------------------------------------------')
    print(f'mas de {goals_limit} = {prob_more_result}%\nmenos de {goals_limit} = {prob_less_result}%\n')
    goals_limit += 0.5