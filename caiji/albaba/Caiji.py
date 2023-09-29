from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import subprocess
shortcut_path = r'C:\Users\86176\Desktop\Chrome.lnk'  # 替换为您的快捷方式路径
subprocess.Popen(['explorer', shortcut_path])

options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
browser = webdriver.Chrome(options=options)
browser.get('https://detail.1688.com/offer/735941026853.html ')
html = browser.page_source

print(html)
aaa