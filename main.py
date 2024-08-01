import requests
from bs4 import BeautifulSoup
import pandas as pd

url_file='D:\\Python Code 2024\\UpWork\\Company_Automation\\teacherspayteachers\\urls.csv' #gather url thanks to Selenium and Excel Formula

df_urls=pd.read_csv(url_file)

list_urls=df_urls['link'].to_list()

#LISTs
list_category=[]
list_book_name=[]
list_resourceid=[]
list_pagelink=[]

#COLUMNs NAME
column_s=['Category','Book Name','Resource Id']



for url in list_urls:
    ###GET_URL###
    resp=requests.get(url)
    soup=BeautifulSoup(resp.text,'html.parser')
    ###-=-###

    ###SCRAPPING###
    name_category=soup.find('h2',attrs={'class':'Text-module__root--Jk_wf Text-module__headingSM--m0FXY Text-module__colorExtraDark--DAqgT Text-module__noMarginBottom--VJdLv'})
    name_book=soup.find_all('a',attrs={'class':'Link-module__link--WPOCg Link-module__standardQuiet--OcM14 ProductRowCard-module__cardTitleLink--YPqiC'})
    name_resourceid=soup.find_all('div',attrs={'class':'ProductRowLayout'})
    ###-=-###

    ###CREATE LIST###
    for k in name_book:
        list_category.append(name_category.get_text())

    for i in name_book:
        list_book_name.append(i.text)

    for j in name_resourceid:
        get_id=j.get('data-crometrics-resourceid')
        list_resourceid.append(get_id)

    for l in name_resourceid:
        firspart='https://www.teacherspayteachers.com'
        secondpart=l.find('a')['href']
        merge=firspart+secondpart
        list_pagelink.append(merge) 

###-=-###

###CREATE DATAFRAME###
df=pd.DataFrame([list_category,list_book_name,list_resourceid,list_pagelink]).T
print(df)
df.to_csv('UpWorkjob1.csv',index=0)
###-=-###