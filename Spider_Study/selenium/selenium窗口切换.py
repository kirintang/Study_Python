from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time


web = Chrome()
web.get("https://www.lagou.com/")

web.find_element_by_xpath('//*[@id="changeCityBox"]/ul/li[1]/a').click()

time.sleep(2)

web.find_element_by_xpath(
    '//*[@id="search_input"]').send_keys("python", Keys.ENTER)

time.sleep(1)

web.find_element_by_xpath(
    '//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a/h3').click()

# 如何在新窗口查找信息
# 在selenium眼中，新窗口默认是不切换过来的
web.switch_to.window(web.window_handles[-1])

# 在新窗口提取内容
job_detail = web.find_element_by_xpath('//*[@id="job_detail"]/dd[2]/div').text

# 关掉子窗口
web.close()
# 变更selenium的窗口视角，回到原来的窗口中
web.switch_to.window(web.window_handles[0])
