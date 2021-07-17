from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

web = Chrome()
web.get("https://www.lagou.com/")

# 找到全国元素，点击
el = web.find_element_by_xpath('//*[@id="changeCityBox"]/ul/li[1]/a')
el.click()  # 点击

time.sleep(2)  # 让浏览器缓一会儿，避免遇到ajax请求的网站没有拿到数据
# 找到输入框，输入python => 输入回车
web.find_element_by_xpath(
    '//*[@id="search_input"]').send_keys("python", Keys.ENTER)

# 查找存放数据的位置，提取数据
# 找到页面所有存放数据的li  find_elements_by_xpath 带s
li_list = web.find_elements_by_xpath('//*[@id="s_position_list"]/ul/li')
for li in li_list:
    job_name = li.find_element_by_tag_name("h3").text
    job_money = li.find_element_by_xpath("./div/div/div[2]/div/span").text
    company_name = li.find_element_by_xpath('./div/div[2]/div/a').text
    print(job_name, job_money, company_name)
