from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import subprocess
from urllib.parse import urlparse
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import caiji.mysql.mysql
from selenium.webdriver.common.action_chains import ActionChains

def XiangQing (http):
    options = Options()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    browser = webdriver.Chrome(options=options)
    browser.get(http)
     # 获取所有商品元素
    ele = browser.find_elements(By.CLASS_NAME, 'main-picture')
    con = len(ele)
     # 遍历每个商品元素
    for o in range(con):
        # 点击当前元素
        element = browser.find_element(By.CSS_SELECTOR, f'#bd_1_container_0 > div > div:nth-child(2) > div:nth-child(6) > div:nth-child({o+1})')
        time.sleep(0.2)
        element.click()
         # 切换到新打开的标签页
        browser.switch_to.window(browser.window_handles[1])
         # 获取当前页面网址
        current_url = urlparse(browser.current_url)
        html = browser.page_source
        url = (current_url.scheme + "://" + current_url.netloc + current_url.path)
        caiji.mysql.mysql.insert_sql('data', 'URL', "URL,HTML", (f"{url}","1"))
         # 关闭当前标签页
        browser.close()
         # 切换回原始标签页
        browser.switch_to.window(browser.window_handles[0])
     # 获取总页数
    total_pages = int(browser.find_element(By.CSS_SELECTOR, '#bd_1_container_0 > div > div:nth-child(2) > div:nth-child(7) > div > div:nth-child(9)').text)
     # 遍历所有页
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
         # 遍历当前页的每个商品元素
        for i in range(count):
            # 点击当前元素
            time.sleep(1)
            qqq = browser.find_element(By.CSS_SELECTOR, f'#bd_1_container_0 > div > div:nth-child(2) > div:nth-child(6) > div:nth-child({i+1})')
            # bd_1_container_0 > div > div:nth-child(2) > div:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div > img

            time.sleep(0.2)
            qqq.click()
             # 切换到新打开的标签页
            browser.switch_to.window(browser.window_handles[1])
             # 获取当前页面网址
            current_url = urlparse(browser.current_url)
            html = browser.page_source
            url = (current_url.scheme + "://" + current_url.netloc + current_url.path)
            caiji.mysql.mysql.insert_sql('data', 'URL', "URL,HTML", (f"{url}","1"))
             # 关闭当前标签页
            browser.close()
             # 切换回原始标签页
            browser.switch_to.window(browser.window_handles[0])

def YeMian ():
    a= caiji.mysql.mysql.select_sql('data', 'URL', "URL where is_crawl is null order by id desc limit 1")
    options = Options()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    Xiangqing_browser = webdriver.Chrome(options=options)
    Xiangqing_browser.get(a[0][0])
    #获取当前页面的标题
    Biao= Xiangqing_browser.title
    html = Xiangqing_browser.page_source
    #将html保存到txt文件
    with open('html.html', 'w', encoding='utf-8') as f:
        f.write(html)
        f.close()
    BiaoTi = Xiangqing_browser.find_element(By.CLASS_NAME, 'title-text').text
    Main_JiaGe =  Xiangqing_browser.find_element(By.CLASS_NAME, 'price-text').text
    XiangQingXinXi = Xiangqing_browser.find_element(By.CLASS_NAME, 'offer-attr-list').text
    SKU = []
    SKU =Xiangqing_browser.find_elements(By.CLASS_NAME, 'sku-item-name').text
    JiaGe = Xiangqing_browser.find_elements(By.CLASS_NAME, 'discountPrice-price').text
    #检查是否有变体
    print(BiaoTi,Main_JiaGe,XiangQingXinXi,SKU,JiaGe)





    if Biao == '验证码拦截':
        # huadong = Xiangqing_browser.find_element_by_css_selector('#nc_1_n1z')
        huadong = Xiangqing_browser.find_element(By.CSS_SELECTOR, '#nc_1_n1z')
        actions = ActionChains(Xiangqing_browser)
        actions.click_and_hold(huadong)
        actions.move_by_offset(300, 0)  # 向右滑动100个像素
        actions.release()
        actions.perform()
        Xiangqing_browser.refresh()

    time.sleep(0.5)
if __name__ == '__main__':
    YeMian()

