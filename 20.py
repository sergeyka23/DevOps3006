from selenium import webdriver
from time import sleep
my_driver = webdriver.Chrome()
# my_driver = webdriver.Chrome(executable_path="c:/Users/dementis/download/choremdriver.exe")
# my_driver.get("https://github.com")
my_driver.get("file:///C:/Users/dementis/PycharmProjects/tip_calc/index.html")
billamt = my_driver.find_element(by="id", value= "billamt").send_keys("100")
my_driver.find_element(by="xpath", value='//*[@id="serviceQual"]/option[4]').click()
my_driver.find_element(by="id", value="peopleamt").send_keys("5")
my_driver.find_element(by="id", value="musicquality").send_keys("5")
my_driver.find_element(by="id", value="calculate").click()
expected = "8.00"
actual = my_driver.find_element(by="id", value="tip").text

assert expected!=actual

# if expected==actual:
#    print("ok")
# else:
#    print("Not ok")

#for i in range(5):
#    sleep(5)
#    my_driver.refresh()

#my_driver.close()