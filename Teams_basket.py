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

sleep(2)

try:
    boton_cookies = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[@id = "onetrust-accept-btn-handler"]'))
    )

    boton_cookies.click()
except Exception as e:
    print(e)

sleep(2)