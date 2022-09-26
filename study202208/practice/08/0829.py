import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# def element_interaction():
#     driver=webdriver.Chrome()
#     driver.get("https://www.sogou.com/")
#     driver.find_element(By.ID,"query").send_keys("霍格沃兹")
#     time.sleep(2)
#     driver.find_element(By.ID,"query").clear()
#     time.sleep(2)
#     driver.find_element(By.ID,"query").send_keys("啦啦")
#     time.sleep(2)
#     driver.find_element(By.ID,"stb").click()
#     time.sleep(2)
#     driver.close()
# def get_attr():
#     driver=webdriver.Chrome()
#     driver.get("https://vip.ceshiren.com/#/ui_study")
#     web_element=driver.find_element(By.ID,"locate_id")
#     print(web_element.get_attribute("class"))
#     print(web_element.text)
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# def search_ceshiren():
#     driver=webdriver.Chrome()
#     driver.get("https://ceshiren.com")
#     driver.implicitly_wait(5)
#     # WebDriverWait(driver,10).until(
#     #     expected_conditions.element_to_be_clickable(By.CSS_SELECTOR,"#search-button")
#     # )
#     driver.find_element(By.CSS_SELECTOR, "#search-button > svg").click()
#     driver.find_element(By.ID,"search-term").send_keys("appium")
#     time.sleep(2)
#     driver.close()

#只能解出前5个，后面的都不对，需要参考答案
# def proper_fractions(n: int) -> int:
#     list1 = []
#     for i in range(1,n):
#         if (i % 2 == 0 and n%2 == 0) or (i % 3 == 0 and n%3==0) or (i % 5 == 0 and n%5==0):
#             pass
#         else:
#             list1.append(i)
#     print(list1)
#     return len(list1)

def format_duration(seconds: int) -> str:
    year=0
    day=0
    hour=0
    minute=0
    second=0
    if seconds==0:
        return f"now"
    elif seconds<60:
        return f"{seconds} second"
    elif seconds%60==0:
        if seconds/60<60:
            minute+=seconds/60
            return f"{int(minute)} minute"
        elif seconds/60/60<24:
            hour+=seconds/60/60
            return f"{int(hour)} hour"
        elif seconds/60/60/24<365 and seconds/60/60%24==0:
            day+=seconds/60/60/24
            return f"{int(day)} day"
        elif seconds/60/60/24%365==0:
            year+=seconds/60/60/24/365
            return f"{int(year)} year"
        else:
            year += seconds / 60 / 60 / 24 / 365
            day += seconds / 60 / 60 / 24 % 365
            hour += seconds / 60 / 60 % 24
            minute += seconds / 60 % 60
            second = seconds % 60
            return f"{int(year)} year,{int(day)} days,{int(hour)} hours,{int(minute)} minutes and {second} seconds"
    else:
        if seconds>60 and  seconds/60<60:
            minute += seconds / 60
            second=seconds%60
            return f"{int(minute)} minute and {second} seconds"
        elif seconds/60>60 and seconds/60/60<24:
            hour+=seconds/60/60
            minute+=seconds/60%60
            second = seconds % 60
            return f"{int(hour)} hour,{int(minute)} minutes and {second} seconds"
        elif seconds/60/60>24 and seconds/60/60/24<365:
            day+=seconds / 60 / 60/24
            hour += seconds / 60 / 60%24
            minute += seconds / 60 % 60
            second = seconds % 60
            return f"{int(day)} day,{int(hour)} hours,{int(minute)} minutes and {second} seconds"
        else:
            year+=seconds / 60 / 60 / 24/365
            day += seconds / 60 / 60 / 24%365
            hour += seconds / 60 / 60%24
            minute += seconds / 60 % 60
            second = seconds % 60
            return f"{int(year)} year,{int(day)} days,{int(hour)} hours,{int(minute)} minutes and {second} seconds"


if __name__ == '__main__':
    # element_interaction()
    # get_attr()
    # search_ceshiren()
    # print(proper_fractions(1))
    # print(proper_fractions(2))
    # print(proper_fractions(5))
    # print(proper_fractions(15))
    # print(proper_fractions(25))
    # print(proper_fractions(9999999))
    # print(proper_fractions(500000003))
    # print(proper_fractions(1532420))
    # print(proper_fractions(123456789))
    # print(proper_fractions(9999999999))
    print(format_duration(0))
    print(format_duration(1))
    print(format_duration(62))
    print(format_duration(120))
    print(format_duration(3600))
    print(format_duration(3662))
    print(format_duration(15731080))
    print(format_duration(132030240))
    print(format_duration(205851834))
    print(format_duration(253374061))
    print(format_duration(242062374))
    print(format_duration(101956166))
    print(format_duration(33243586))