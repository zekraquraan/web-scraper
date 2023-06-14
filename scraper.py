import requests
from bs4 import BeautifulSoup
url=requests.get('https://en.wikipedia.org/wiki/History_of_Mexico')

def  get_citations_needed_count(url):
    
    soup=BeautifulSoup(url.content,'html.parser')
    citations=soup.find_all('sup',class_='noprint Inline-Template Template-Fact')
    return len(citations)



def  get_citations_needed_report(url):
    
    soup=BeautifulSoup(url.content,'html.parser')
    citations=soup.find_all('sup',class_='noprint Inline-Template Template-Fact')
    string=''
    for i in citations:
        c1=i.find_parent('p')
        c1_text=c1.text
        string+=f"{c1_text}\n\n"
    return string


print(get_citations_needed_count(url))

print(get_citations_needed_report(url))


    








