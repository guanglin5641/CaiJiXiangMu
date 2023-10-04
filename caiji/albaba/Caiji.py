from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import subprocess
from urllib.parse import urlparse

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
shortcut_path = r'C:\Users\lenovo\Desktop\Google.lnk'  # 替换为您的快捷方式路径
subprocess.Popen(['explorer', shortcut_path])
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
browser = webdriver.Chrome(options=options)
browser.get('https://shop25933le021370.1688.com/page/offerlist.html')
ele = browser.find_elements(By.CLASS_NAME, 'main-picture')
con = len(ele)
for o in range(con):
    # 点击当前元素
    element = browser.find_element(By.CSS_SELECTOR, f'#bd_1_container_0 > div > div:nth-child(2) > div:nth-child(6) > div:nth-child({o+1})')
    element.click()
     # 切换到新打开的标签页
    browser.switch_to.window(browser.window_handles[1])
    #获取当前页面网址
    current_url = urlparse(browser.current_url)
    html = browser.page_source
    print(current_url.scheme + "://" + current_url.netloc + current_url.path)
     # 关闭当前标签页
    browser.close()
     # 切换回原始标签页
    browser.switch_to.window(browser.window_handles[0])
 # 获取总页数
total_pages = int(browser.find_element(By.CSS_SELECTOR, '#bd_1_container_0 > div > div:nth-child(2) > div:nth-child(7) > div > div:nth-child(9)').text)
for _ in range(total_pages):
    try:
        # 点击下一页按钮
        next_button = browser.find_element(By.CSS_SELECTOR, '#bd_1_container_0 > div > div:nth-child(2) > div:nth-child(7) > div > button:nth-child(10)')
    except:
        next_button = browser.find_element(By.CSS_SELECTOR, '#bd_1_container_0 > div > div:nth-child(2) > div:nth-child(7) > div > button:nth-child(11)')
    next_button.click()
     # 获取当前页的所有元素
    elements = browser.find_elements(By.CLASS_NAME, 'main-picture')
    count = len(elements)
    for o in range(count):
        # 点击当前元素
        time.sleep(1)
        qqq = browser.find_element(By.CSS_SELECTOR, f'#bd_1_container_0 > div > div:nth-child(2) > div:nth-child(6) > div:nth-child({o+1})')
        # bd_1_container_0 > div > div:nth-child(2) > div:nth-child(6) > div:nth-child(1) > div:nth-child(1)
        # bd_1_container_0 > div > div:nth-child(2) > div:nth-child(6) > div:nth-child(1) > div:nth-child(1) > div > img
        qqq.click()
                 # 切换到新打开的标签页
        browser.switch_to.window(browser.window_handles[1])
        #获取当前页面网址
        current_url = urlparse(browser.current_url)
        html = browser.page_source
        print(current_url.scheme + "://" + current_url.netloc + current_url.path)
         # 关闭当前标签页
        browser.close()
         # 切换回原始标签页
        browser.switch_to.window(browser.window_handles[0])
browser.quit()





