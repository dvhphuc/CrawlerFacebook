from selenium import webdriver
from time import sleep
import time
from selenium.webdriver.common.by import By
PATH = "C:\Program Files (x86)\chromedriver.exe"
import numpy as np
browser = webdriver.Chrome(PATH)

browser.get("https://www.facebook.com/ConfessionUIT")
sleep(2)

SCROLL_PAUSE_TIME = 3

# Get scroll height
last_height = browser.execute_script("return document.body.scrollHeight")
i=0
while i<4:
    # Scroll down to bottom
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
    i+=1
f = open("Post.txt","w") 
elems = browser.find_elements_by_xpath("//a[@href]")
for elem in elems:
    f.write(elem.get_attribute("href"))
    f.write("\n")
f.close()

def normstring(s):
    words = s.split('/')
    if words[4]=='posts':
        text = words[5]
        return text[0:text.find('?')]
    else:
        return None
    
with open("Post.txt","r") as f:
    lines = f.readlines()

result = []
for line in lines:
    if 'posts' in line:
        result.append(normstring(line))
result = np.array(result)

print(np.unique(result))
