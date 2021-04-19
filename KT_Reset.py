from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

opts = webdriver.ChromeOptions()
opts.add_argument('headless')
opts.add_argument('window-size=1920x1080')
opts.add_argument("--disable-gpu")
opts.add_argument("no-sandbox")
opts.add_argument("--disable-dev-shm-usage")
opts.add_argument("lang=ko_KR")

driver = webdriver.Chrome(options=opts)
driver.get('http://access.olleh.com')
time.sleep(0.5)

select_internet = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div/ul/li[3]/strong/a')
select_internet.click()
time.sleep(0.5)

select_confirm = driver.switch_to_alert()
select_confirm.accept()

kt_ID = driver.find_element_by_id('l_id')
kt_ID.send_keys('reset')

kt_PW = driver.find_element_by_id('l_pw')
kt_PW.send_keys('reset1')

driver.execute_script('reset_id_submit();')
time.sleep(10)

kt_confirm = driver.find_element_by_class_name('s1')
kt_confirm.click()