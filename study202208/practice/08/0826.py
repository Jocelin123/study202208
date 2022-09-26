# # 子生成器
# def average_gen():
#     total = 0
#     count = 0
#     average = 0
#     while True:
#         new_num = yield average
#         count += 1
#         total += new_num
#         average = total/count
#
# # 委托生成器
# def proxy_gen():
#     while True:
#         yield from average_gen()
#
# # 调用方
# def main():
#     calc_average = proxy_gen()
#     next(calc_average)            # 预激下生成器
#     print(calc_average.send(10))  # 打印：10.0
#     print(calc_average.send(20))  # 打印：15.0
#     print(calc_average.send(30))  # 打印：20.0
#
# if __name__ == '__main__':
#     main()

# def one():
#     print('one start')
#     res = yield from two()
#     print('function get res: ', res)
#     return 'one' + res
#
#
# def two():
#     print('two start')
#     res = yield from three()
#     print(">>> two1")
#     return res
#
#
# def three():
#     print(">>> three1")
#     yield 1
#     print(">>> three2")
#     return 'three'
#
#
# if __name__ == '__main__':
#     gen = one()
#     print(">>> 1")
#     send_1 = gen.send(None)
#     print(">>> 2")
#     print(send_1)
#     print(">>> 3")
#     send_2 = gen.send(None)
#     print(">>> 4")
#     print(send_2)
#     print(">>> 5")
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def web_locate():
    driver=webdriver.Chrome()
    # driver.get("https://vip.ceshiren.com/")
    driver.get("https://vip.ceshiren.com/#/ui_study")
    driver.implicitly_wait(5)
    # sleep(2)
    # web_element=driver.find_element(By.ID,"locate_id")
    # web_element=driver.find_element(By.NAME,"locate")
    # web_element=driver.find_element(By.CSS_SELECTOR,"#locate_id > a > span")
    # web_element=driver.find_element(By.XPATH,'//*[@id="locate_id"]/a/span')
    # web_element=driver.find_element(By.LINK_TEXT,"元素定位")
    # web_element=driver.find_element(By.XPATH,"//*[text()='个人中心']")
    # sleep(3)
    # web_element=driver.find_element(By.ID,'primary_btn')
    WebDriverWait(driver, 15).until(
        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#success_btn>span')))
    print(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#success_btn')))
    # print(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#success_btn > span')))
    # sleep(5)
    # print(driver.find_element(By.CSS_SELECTOR, '#success_btn > span').is_enabled())
    # sleep(5)
    # driver.find_element(By.ID,'success_btn').click()
    driver.find_element(By.CSS_SELECTOR, '#success_btn').click()
    sleep(6)
    # driver.implicitly_wait(3)
    driver.quit()
if __name__ == '__main__':
    web_locate()