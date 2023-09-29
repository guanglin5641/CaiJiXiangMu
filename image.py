import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
 # 创建Chrome浏览器驱动对象
login_driver = webdriver.Chrome()
# 打开网址
url = "https://www.imageoss.com/upload"
login_driver.get(url)
username_input = login_driver.find_element(By.NAME, 'login-subject').send_keys('123')
password_input = login_driver.find_element(By.NAME, 'password').send_keys('123456789mmk..')
login_button = login_driver.find_element(By.CSS_SELECTOR, '#login > div.display-flex.height-min-full > div > div > div > form > fieldset > div.input-with-button > button').click()



 # 等待页面加载完成
time.sleep(5)
# 关闭浏览器
login_button.quit()