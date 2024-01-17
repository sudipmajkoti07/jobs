from bs4 import BeautifulSoup
import requests
import pandas as pd

url='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='
r=requests.get(url)
ram=r.text
soup=BeautifulSoup(ram,'lxml')

def start():

    jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    companynamelist=[]
    neededskills=[]
    linkofpost=[]

    for job in jobs:
        post=job.find('span',class_='sim-posted').span.text.replace('   ','')
        if post=='Posted few days ago':
            companyname=job.find('h3',class_='joblist-comp-name').text.replace('   ','')
            skills=job.find('span',class_='srp-skills').text.replace('   ','')
            link=job.find('a').get('href')
            companynamelist.append(companyname)
            neededskills.append(skills)
            linkofpost.append(link)

    data={'company name': companynamelist, 'skills': neededskills, 'link': linkofpost}
    df=pd.DataFrame(data)
    df.to_csv('file.csv')

if __name__=='__main__':
    start()
    


    

    