from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
PATH = "C:\Program Files (x86)\chromedriver.exe"

browser = webdriver.Chrome(PATH)

browser.get("https://www.facebook.com/ConfessionUIT/posts/7275591609179647")

sleep(3)

showcomment_link = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div[2]/div[2]/div[1]/div/div[3]/span/a")
showcomment_link.click()
sleep(3)

allcomments_link = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div[2]/div[3]/div[1]/div/div/div/div/a")
allcomments_link.click()
sleep(3)

allcomments_link = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[3]/div/div/div/ul/li[3]/a/span/span/div/div[1]")
allcomments_link.click()
sleep(3)

allcomments_link = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div[2]/div[3]/div[2]/div/a/div")
allcomments_link.click()
sleep(3)

#comment_list = browser.find_elements_by_xpath("//div[@aria-label='Comment']")
comment_list = browser.find_elements(by=By.XPATH,value="//div[@aria-label='Comment']")
#print(comment_list)
f = open("Comments.txt","w")
for comment in comment_list:
    content = comment.find_element_by_class_name("_3l3x")
    print(content.text)
    f.write(content.text)
f.close()