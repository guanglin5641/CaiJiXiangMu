from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from amazoncaptcha import AmazonCaptcha
def solve_captcha(url):
    # 创建Chrome浏览器实例
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(10)
     # 解决验证码
    def solve_captcha():
        captcha = AmazonCaptcha.fromdriver(driver)
        solution = captcha.solve()
        return solution
    num_attempts = 1
    solution = solve_captcha()
    while not solution:
        solution = solve_captcha()
        num_attempts += 1
        print("循环次数:", num_attempts)
        if num_attempts > 3:
            print("循环次数超过限制，退出循环")
            break
    try:
        # 输入验证码并点击提交按钮
        driver.find_element(By.XPATH, '/html/body/div/div[1]/div[3]/div/div/form/div[1]/div/div/div[2]/input').send_keys(solution)
        driver.find_element(By.XPATH, '/html/body/div/div[1]/div[3]/div/div/form/div[2]/div/span/span/button').click()
    except Exception as e:
        print("出现错误:", e)
        print("重新开始循环")
     # 显式等待，等待所有元素渲染完成
    wait = WebDriverWait(driver, 10)
    try:
        dianji = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#sp-cc-rejectall-link')))
        dianji.click()
    except Exception as e:
        print("出现错误:", e)
        print("重新开始循环")
    try:
        CaiJi = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.wjya-fetch-detail > div > button > font > font')))
        CaiJi.click()
    except Exception as e:
        print("出现错误:", e)
        print("重新开始循环")
     # 保存网页源代码
    html = driver.page_source
    with open('../webpage.html', 'w', encoding='utf-8') as file:
        file.write(html)
     # 获取标题
    name = driver.find_element(By.ID,'productTitle').text
    print('标题: '+name)
     # 五点描述
    WuDianMiaoSHu = driver.find_elements(By.CSS_SELECTOR, '#feature-bullets > ul > li > span')
    descriptions = [element.text for element in WuDianMiaoSHu]
    for description in descriptions:
        print('五点描述:', description)
     # 检查是否有更多描述
    GengDuo = driver.find_elements(By.CSS_SELECTOR, '#feature-bullets > div > a > span')
    if GengDuo:
        driver.execute_script("arguments[0].click();", GengDuo[0])
        MiaoSHuLen = driver.find_elements(By.CSS_SELECTOR, '#feature-bullets > div > div > ul > li > span')
        for MiaoSHu in MiaoSHuLen:
            print('描述:', MiaoSHu.text)
    else:
        print('GengDuo元素不存在，忽略选中代码')
     # 获取详情
    XiangQing = driver.find_element(By.CSS_SELECTOR,'#productDescription > p > span')
    XiangQingText = XiangQing.text.replace('\n', '<br/>')
    print('详情：'+XiangQingText)


     # 获取颜色信息
    color_all = driver.find_elements(By.CLASS_NAME, 'imgSwatch')
    alt_attributes = []
    for element in color_all:
        alt_attribute = element.get_attribute('alt')
        alt_attributes.append(alt_attribute)
    print(alt_attributes)
    count = len(color_all)
    #获取变体
     # 重试次数
    num_attempts = 5
     # 获取颜色变体
    for _ in range(num_attempts):
        try:
            element = driver.find_element(By.CSS_SELECTOR, '#inline-twister-expander-content-color_name')
            break  # 如果成功找到元素，跳出循环
        except Exception as e:
            print("无法获取元素:", e)
            print("重新尝试")
    else:
        print("无法获取元素，重试次数达到上限")
        driver.quit()
        exit()
    total_variation_count = element.get_attribute('data-totalvariationcount')
    int_total_variation_count = int(total_variation_count)
    for i in range(2, int_total_variation_count + 2):
        css_selector = '#tp-inline-twister-dim-values-container > ul > li:nth-child({})'.format(i)
        print(css_selector)
        color= driver.find_element(By.CSS_SELECTOR, '#inline-twister-expanded-dimension-text-color_name').text
        print(color)
# 调用函数并传递网址
if __name__ == '__main__':
    url = 'https://www.amazon.co.uk/dp/B0BJ3P3DBH?th=1&psc=1'
    solve_captcha(url)
