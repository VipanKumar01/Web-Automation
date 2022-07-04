# Name = Vipan Kumar
# user name = @VipanKumar01

from logging import exception
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# Launching WebDriver
driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")



rollno = [2001345011001]
temp = [2001345011003]

driver.maximize_window() # It Makes the Maximize window
try:
    while temp != rollno:
        driver.get("https://dbrauaaems.in/StuRoll_2021.aspx")
        driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_txtroll"]').send_keys(rollno[0])
        rollno[0] = rollno[0]+1
        
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_Button1"]').click()

        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_lnksem1"]').click()
        name = driver.find_element_by_id("ContentPlaceHolder1_lblName").text
        print(name)
        
        driver.execute_script("document.body.style.zoom='79%'")
        time.sleep(5)
        
        
        myScreenshot = pyautogui.screenshot()
        # myScreenshot = driver.find_element_by_xpath('/html/body').screenshot(f'{name}.png')
        myScreenshot.save(f'{name}.png')
        driver.implicitly_wait(4)
except exception as e:
    print(e)  
finally:
    driver.close()
# The Result is saved the Student Name
# --HappyCode--
