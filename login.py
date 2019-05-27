from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#logging in
n = input('how many users: ')
u = input("username: ")
p = input("password: ")
t = input("Who is your target: ")
f= open("targets.txt","w")
chromedriver = "C:/Users/123/Downloads/chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
url = "https://instagram.com/"+t+"/followers"
driver.get(url)
time.sleep(4)
driver.find_element_by_name("username").send_keys(u)
driver.find_element_by_name("password").send_keys(p)
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[4]/button").click()
time.sleep(10)

#Gathering steps
x = 1
y = int(n)+1
while x != y:
    prof = "/html/body/div[3]/div/div[2]/ul/div/li["+str(x)+"]/div/div[1]/div[2]/div[1]/a"
    u_name = "/html/body/div[3]/div/div[2]/ul/div/li["+str(x)+"]/div/div[1]"
    sc = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/ul/div/li["+str(x)+"]/div")
    sc.location_once_scrolled_into_view
    sc.location_once_scrolled_into_view
    name = driver.find_element(By.XPATH, u_name).find_element(By.XPATH, prof)
    time.sleep(1)
    name.location_once_scrolled_into_view
    time.sleep(1)
    res = name.get_attribute("href")
    f.write(res[26:-1]+"\n")
    print(res[26:-1]+" "+str(x)+"\n")
    x = x + 1
print("done ...")
f.close()
