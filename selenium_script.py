from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
start_time = time.time()
options = Options()
options = Options()
#options.add_argument("--headless")
#options.add_argument("--disable-gpu")
#options.add_argument("--no-sandbox")
#options.add_argument("enable-automation")
#options.add_argument("--disable-infobars")
#options.add_argument("--disable-dev-shm-usage")
browser = webdriver.Firefox(executable_path="./geckodriver",options=options)
print("Starting Browser")
browser.get('https://plus.pearson.com')
print("Loaded Pearson")
time.sleep(20)

browser.find_element_by_class_name('button-skip').click()
print("Closed Warning Message")
inputElement = browser.find_element_by_id("username")
inputElement.send_keys('nicholasxwang')
print("Put in Username")
inputElement = browser.find_element_by_id("password")
inputElement.send_keys('Password123')
print("Put in Password")
browser.find_element_by_id("mainButton").submit()
print("Logged in!")
time.sleep(30)
books = browser.find_elements_by_class_name('etext-title')
pics = browser.find_elements_by_class_name('etext-media')
listy = []
print("Fetched all Subjects")
for i in range(0,len(books)):
  book = books[i].text
  img = pics[i].get_attribute("src")
  listy.append({'book':book,'picture':img})
for i in range(0,len(books)):
  print(f"Reading {listy[i]['book']}")
  browser.get('https://plus.pearson.com/home')
  time.sleep(25)
  print(f"Reading {listy[i]['book']}\'s BASIC INFO")

  browser.find_elements_by_class_name('etext-info')[i].click()
  author = browser.find_elements_by_class_name('dialogcontentitem')[1].text
  isbn = browser.find_elements_by_class_name('dialogcontentitem')[2].text
  model = browser.find_elements_by_class_name('dialogcontentitem')[3].text
  listy[i]['ISBN'] = isbn
  listy[i]['author'] = author
  listy[i]['model'] = model
  print(f"Finding {listy[i]['book']}\'s Link to E-Book")
  browser.get('https://plus.pearson.com/home')
  time.sleep(20)
  browser.find_elements_by_class_name('etext-action')[i].click()
  time.sleep(20)
  
  url = browser.current_url
  url = url[0:url.find('/pages')]
  listy[i]['url']= url
  
  
with open('main.json','w') as out:
  import json
  json.dump(listy,out,indent=4)
print("Your pearson acocunt took", time.time() - start_time, "seconds to scrape.")
print("Your data is available in ./main.json !")