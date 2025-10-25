from selenium import webdriver
from selenium.webdriver.chrome.service import Service as EdgeService

#打开Edge浏览器
service = EdgeService(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
driver = webdriver.Edge(service = service)

driver.maximize_window()
driver.get('https://www.runoob.com')
print(1)
element = driver.find_element()
print(element)