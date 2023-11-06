import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 创建Chrome浏览器驱动对象
login_driver = webdriver.Chrome()

# 打开网址
url = "https://www.imageoss.com/upload"
login_driver.get(url)

username_input = login_driver.find_element(By.NAME, 'login-subject').send_keys('123')
password_input = login_driver.find_element(By.NAME, 'password').send_keys('123456789mmk..')
login_button = login_driver.find_element(By.CSS_SELECTOR, '#login > div.display-flex.height-min-full > div > div > div > form > fieldset > div.input-with-button > button').click()
#获取当前cookies
cookies = login_driver.get_cookies()
print(cookies)
#引用当前cookies


# 等待页面加载完成
time.sleep(5)

# 使用显示等待等待上传按钮可见并可操作
# upload_button = WebDriverWait(login_driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, "#anywhere-upload > div.content-width > div > div.upload-box-heading.c16.center-box > div > div:nth-child(1) > div.device-mobile--hide.upload-box-status-text > a:nth-child(1)"))
# )
#
# # 输入本地文件路径到文件上传输入框
# file_path = r"C:\Users\EDY\Downloads\image (4).png"
# login_driver.execute_script("arguments[0].style.display = 'block';", upload_button)  # 设置元素可见
# upload_button.send_keys(file_path)

# 等待上传完成或执行其他操作
time.sleep(10)

# 关闭浏览器
login_driver.quit()