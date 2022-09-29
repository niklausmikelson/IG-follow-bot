from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import random
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
      
def check_exists_by_xpath(xpath):
    try:
        driver.find_element(by=By.XPATH, value=xpath)
    except NoSuchElementException:
        return False
    return True
def click_until_interactable(xpath):
    interactable=False
    while(not interactable):
        try:
            driver.find_element(by=By.XPATH, value=xpath).click()
            interactable=True
            
        except(StaleElementReferenceException,ElementClickInterceptedException,ElementNotInteractableException,NoSuchElementException) as e:
            continue
def click_until_interactable_for_search(xpath):
    interactable=False
    while(not interactable):
        try:
            z=0
            sleep(1)
            driver.find_element(by=By.XPATH, value=xpath).click()
            interactable=True
            print("success")
        except(StaleElementReferenceException,ElementClickInterceptedException,ElementNotInteractableException,NoSuchElementException) as e:
            if(not z):
                z=1
                driver.execute_script('window.scrollTo(0,400)')
            continue
def click_until_interactable_for_reload(xpath):
    interactable=False
    r=0
    while(not interactable):
        try:
            driver.find_element(by=By.XPATH, value=xpath).click()
            interactable=True
            
        except(StaleElementReferenceException,ElementClickInterceptedException,ElementNotInteractableException,NoSuchElementException) as e:
            r=r+1
            print(r)
            if(r>20):
                driver.execute_script('location.reload()')
            continue
def choose_until_interactable(xpath):
    interactable=False
    while(not interactable):
        try:
            driver.find_element(by=By.XPATH, value=xpath)
            interactable=True
            
        except(StaleElementReferenceException,ElementClickInterceptedException,ElementNotInteractableException,NoSuchElementException) as e:
            continue
    return driver.find_element(by=By.XPATH, value=xpath)    
 
username="your username"
pswd="your password"
PATH = "C:\\Program Files (x86)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.instagram.com")
sleep(5)
driver.find_element(by=By.XPATH, value='//input[@type="text"]').send_keys(username)
driver.find_element(by=By.XPATH, value='//input[@name="password"]').send_keys(pswd)
sleep(1)
driver.find_element(by=By.XPATH, value='//button[@class="sqdOP  L3NKy   y3zKF     "]').click()
sleep(7)

#------------------------------------------------------------------U STOPPED HERE--------------------------------------------------------------------------------------
#
#sleep(40)
#searchBar

#preparing the searchTerm
searchTerm = ["desired account name you want to follow its followers"]
searchTerm = searchTerm[random.randint(0,len(searchTerm)-1)]
#searching
sleep(2)                                #//div/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]
driver.find_element(by=By.XPATH, value='//div/div/div/div/div[1]/div/div/div/div/section/nav/div[2]/div/div/div[2]/input').send_keys(searchTerm)
sleep(4)
click_until_interactable('//section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]')
print("done")

sleep(10)
click_until_interactable('//div/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[2]/a/div')
sleep(4)
print("awake2")
for j in range(10):
    for i in range(1,2400):         
        a=choose_until_interactable('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div['+str(i)+']/div[3]/button')
        typeValue=a.get_attribute('class')
        if (typeValue != "_acan _acap _acat"):
            click_until_interactable('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div['+str(i)+']/div[3]/button')
        #elem = driver.find_element(by=By.XPATH, value='//button[@aria-label="Close Modal"]')
        #if elem.is_displayed():
            #driver.find_element(by=By.XPATH, value='//button[@aria-label="Close Modal"]').click()
        #a=driver.find_element(by=By.XPATH, value='//a['+ str(i) +']//div[1]//div[1]//div[1]//button//span//div//img')
        sleep(random.uniform(4,7))
    sleep(10)
print("done2")
driver.close()