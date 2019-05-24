from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#logging in
n = input('how many users: ')
u = input("username: ")
p = input("password: ")
f= open("targets.txt","w")
chromedriver = "C:/Users/123/Downloads/chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
url = "https://instagram.com/"+u+"/followers"
driver.get(url)
driver.find_element_by_name("username").send_keys(u)
driver.find_element_by_name("password").send_keys(p)

time.sleep(2)
b = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[4]/button").click()
time.sleep(4)

#Gathering steps
x = 1
y = int(n)+1
while x != y:
    prof = "/html/body/div[3]/div/div[2]/ul/div/li["+str(x)+"]/div/div[1]/div[2]/div[1]/a"
    name = driver.find_element_by_xpath(prof)
    res = name.get_attribute("href")
    f.write(res[26:-1]+"\n")
    x = x + 1


f.close()
