from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://ceshiren.com/")
# driver=webdriver.Firefox()
# driver.get("https://ceshiren.com/")
sleep(1)
driver.quit()