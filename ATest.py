import time
from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.common.keys import Keys

driver=Chrome((r"C:\Users\Admin\AppData\Local\Programs\Python\Python36-32\chromedriver_win32\chromedriver.exe"))
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://www.google.com/")
time.sleep(5)
#Step1
element=driver.find_element_by_link_text('Gmail')
#Step2
act=ActionChains(driver)
#Step3
act.click(element).perform()
driver.close()

