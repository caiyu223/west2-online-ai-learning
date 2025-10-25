from selenium import webdriver
from selenium.webdriver.chrome.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import json
import time



    
def first_login(login_url):
        service = EdgeService(r"C:\Program Files (x86)\Microsoft\Edge\Application\edgedriver_win64 (1)\msedgedriver.exe")
        driver = webdriver.Edge(service = service)
        driver.get(login_url)
        input('按任意键继续')
        time.sleep(3)
        cookies = driver.get_cookies()
        with open('cookies.json','w') as f:
            json.dump(cookies,f,ensure_ascii=False)
        print(cookies)
        


    #打开Edge浏览器

def login_by_cookies(url):
        service = EdgeService(r"C:\Program Files (x86)\Microsoft\Edge\Application\edgedriver_win64 (1)\msedgedriver.exe")
        driver = webdriver.Edge(service = service)
        #driver.maximize_window()

        
        driver.get(url)
        with open('cookies.json','rb') as f:
            cookies = json.load(f)
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.refresh()
        return driver

def get_hot_topics(driver):
        wait = WebDriverWait(driver, 10)
        print('--------')
        element = wait.until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div[3]/header/div/div[1]/div[1]/nav/a[3]')
        ))
        #点击
        element.click()
        driver.execute_async_script("window.scrollBy(0,300);")
        elements = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH,'//*[@id="TopstoryContent"]/div/div//div/div/div/div/div/h2/div/a')
            )
        )
        
        time.sleep(1)
        return elements

    


login_url = 'https://www.zhihu.com/signin'
url = 'https://www.zhihu.com/'


#first_login(login_url)
driver = login_by_cookies(url)
elements = get_hot_topics(driver)

