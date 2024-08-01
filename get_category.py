from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup


options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

browser=webdriver.Chrome(options=options)

category_xpath='/html/body/div[1]/div/div/div[2]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div[{}]'
websites_list=[]
page_number_list=[]


for z in range(1,28):
    print(str(z)+'. kategori yazildi')
    browser.get('https://www.teacherspayteachers.com/store/acorn-science')

    time.sleep(1)
    button=browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div[3]/div/div/div[2]/div/div/div[2]/button/div/div/div')
    button.click()                          
    time.sleep(1)
    button1=browser.find_element(By.XPATH,category_xpath.format(z))
    button1.click()
    websites_list.append(browser.current_url)
    nex_page=browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div[3]/div/div/div[2]/div/div/div/div/div[2]/div/div/div[1]')
    nex_page=browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div[3]/div/div/div[2]/div/div/div/div/div[2]/div/div/div[1]')
    nex_page=browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div[3]/div/div/div[2]/div/div/div/div/div[2]/div/div/div[1]')
    nex_page=browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div[3]/div/div/div[2]/div/div/div/div/div[2]/div/div/div[1]')
    nex_page=browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div[3]/div/div/div[2]/div/div/div/div/div[2]/div/div/div[1]')
    nex_page=browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div[3]/div/div/div[2]/div/div/div/div/div[2]/div/div/div[1]')
    time.sleep(5)
    nex_page.click()
    websites_list.append(browser.current_url)


    resp=requests.get(browser.current_url)
    soup=BeautifulSoup(resp.text,'html.parser')
    page_count=soup.find('div',attrs={'class':'Text-module__root--Jk_wf Text-module__detail--pmgl5'})
    page_number_list.append(page_count.get_text())


    


df=pd.DataFrame([websites_list,page_number_list]).T
print(df)

df.to_csv('category_websites.csv')
