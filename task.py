from selenium import webdriver
import time

option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=option)

links = [
    "https://www.tiket.com/", 
    "https://www.tokopedia.com/", 
    "https://www.orangsiber.com/", 
    "https://idejongkok.com/", 
    "https://kelasotomesyen.com/"
]

for link in links:
    driver.get(link)
    time.sleep(2)  
    driver.maximize_window()
    print(driver.title)
    time.sleep(2)  

driver.quit()
