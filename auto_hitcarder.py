# Buaa Ncov Hitcarder v1.3 @ Colanns
import sys
import logging
import io
from time import sleep
import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

user = ""                       # 你的统一认证账号
passwd = ""                     # 你的统一认证密码json
longitude = ""                  # 定位经度
latitude = ""                   # 定位纬度
ho = 0
mi = 5                          # 打卡时间，默认00:05

def do():
    log = open('rua.log','a')
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.set_window_size(720,1280)

    url = "https://app.buaa.edu.cn/ncov/wap/default"
    header = {'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
    browser.get(url)
    browser.implicitly_wait(3)

    username = browser.find_element_by_tag_name("input")
    username.send_keys(user)

    password = browser.find_element_by_xpath("//input[@type='password']")
    password.send_keys(passwd)

    login_button = browser.find_element_by_css_selector('div.btn')

    browser.execute_script("$(arguments[0]).click()", login_button)
    try:    
        element = WebDriverWait(browser, 10).until(           
            EC.presence_of_element_located((By.NAME, "sfzx")))
    finally:  
        browser.save_screenshot('picture1.png')

    browser.execute_script("window.navigator.geolocation.getCurrentPosition=function(success){"+
                                        "var position = {\"coords\" : {\"latitude\": \""+ latitude + "\",\"longitude\": \""+ longitude +"\"}};"+
                                        "success(position);}")

    tiwen = browser.find_element_by_xpath("//div[@name='tw']/div/div[2]")
    tiwen.click()

    where = browser.find_element_by_name("area")
    where.click()
    sleep(3)
    browser.save_screenshot('geo.png')
    suuubmit = browser.find_element_by_class_name('footers')
    suuubmit.click()
    browser.save_screenshot('confirm.png')
    sleep(1)

    ActionChains(browser).move_by_offset(360, 640).click().perform()
    browser.save_screenshot('ok.png')
    datee = datetime.date.today()
    
    print("%s 成功打卡！" %(datee),file=log)
    print("%s 成功打卡！" %(datee))
    sleep(50)
    browser.quit()
    log.close()

def main():  #0:05进行打卡
    while True:
        while True:
            now = datetime.datetime.now()
            if now.hour==ho and now.minute==mi:
                break
            print("%s 时间未到~" %(now))
            sleep(20)
        do()

main()
