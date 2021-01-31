import time

from selenium import webdriver
# from scrapy import Selector
# from selenium.common.exceptions import NoSuchElementException


browser = webdriver.Chrome(executable_path="c:/Users/17846/Desktop/chromedriver.exe")

browser.get("https://item.jd.com/100008348542.html")
print(browser.page_source)
time.sleep(10)
# try:
#     click_ele = browser.find_element_by_xpath("//li[@clstag='shangpin|keycount|product|shangpinpingjia_1']")
#     click_ele.click()
# except NoSuchElementException as e:
#     pass
#
# sel = Selector(text=browser.page_source)
# print(sel.xpath("//span[@class='price J-p-7652013']/text()").extract_first())
browser.close()
