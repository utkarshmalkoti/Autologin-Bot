import requests
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import time

def open_class(mm,tp):
    print(tp)
    driver = webdriver.Chrome()
    driver.get("https://accounts.google.com/signin/v2/identifier?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2F%3Femr%3D0&followup=https%3A%2F%2Fclassroom.google.com%2F%3Femr%3D0&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    email = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
    email.send_keys("1803010230@ipec.org.in")
    email.send_keys(Keys.ENTER)
    WebDriverWait(driver,20).until(ec.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")))
    pas = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")

    pas.send_keys("kapaa456")
    pas.send_keys(Keys.ENTER)

    time.sleep(5)

    if(tp=='t'):
        print(tp)
        WebDriverWait(driver,10).until(ec.presence_of_element_located((By.XPATH,"/html/body/div[2]/div/div[2]/div/ol/li[2]/div[1]/div[3]/a")))
        room = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/ol/li[2]/div[1]/div[3]/a")
        link = room.get_attribute('href')
        driver.get(link)
    else:
        WebDriverWait(driver,50).until(ec.presence_of_element_located((By.XPATH,"/html/body/div[2]/div/div[2]/div/ol/li[1]/div[1]/div[3]/a")))
        room = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/ol/li[1]/div[1]/div[3]/a")
        link = room.get_attribute('href')
        driver.get(link)

    WebDriverWait(driver,50).until(ec.presence_of_element_located((By.XPATH,"/html/body/div[2]/div[1]/div[1]/div/div[2]/div[2]/span/a")))
    classroom = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div/div[2]/div[2]/span/a")
    link = classroom.get_attribute('href')
    driver.get(link)

    WebDriverWait(driver,50).until(ec.element_to_be_clickable((By.XPATH,"/html/body/div[1]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]")))
    time.sleep(5)
    join = driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]")
    join.click()
    time.sleep((mm*60)+(5*60))
    driver.close()
# def close_class():
    