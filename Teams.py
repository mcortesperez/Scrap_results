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

driver.get('')

sleep(3)

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

more_1matches = 0
less_1matches = 0

more_2matches = 0
less_2matches = 0

more_3matches = 0
less_3matches = 0

gandg_matches = 0
no_gandg = 0

for result in results:
    
    home_goals = int(result.find_element(By.XPATH, './/div[@class = "event__score event__score--home"]').text)
    away_goals = int(result.find_element(By.XPATH, './/div[@class = "event__score event__score--away"]').text)
    total_goals = home_goals + away_goals
    
    if (home_goals != 0) and (away_goals != 0):
        gandg_matches += 1
    else:
        no_gandg += 1
    
    if total_goals > 1.5:
        more_1matches += 1
    else:
        less_1matches += 1
    
    if total_goals > 2.5:
        more_2matches += 1
    else:
        less_2matches += 1
        
    if total_goals > 3.5:
        more_3matches += 1
    else:
        less_3matches += 1
        
prob_more1 = round((more_1matches/len(results))*100, 2)
prob_less1 = round((less_1matches/len(results))*100, 2)

prob_more2 = round((more_2matches/len(results))*100, 2)
prob_less2 = round((less_2matches/len(results))*100, 2)

prob_more3 = round((more_3matches/len(results))*100, 2)
prob_less3 = round((less_3matches/len(results))*100, 2)

prob_goal_and_goal = round((gandg_matches/len(results))*100, 2)
prob_no_gandg = round((no_gandg/len(results))*100, 2)

print('----------------------------------------------------------------------------------------\n')
print(Team+'\n')
print(f'mas de 1.5 = {prob_more1}%\nmenos de 1.5 = {prob_less1}%\n')
print(f'mas de 2.5 = {prob_more2}%\nmenos de 2.5 = {prob_less2}%\n')
print(f'mas de 3.5 = {prob_more3}%\nmenos de 3.5 = {prob_less3}%\n')
print(f'ambos marcan = {prob_goal_and_goal}%\nNO marcan ambos = {prob_no_gandg}%\n')
print('----------------------------------------------------------------------------------------')