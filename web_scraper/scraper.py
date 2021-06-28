import requests
import pprint
from bs4 import BeautifulSoup



def get_citations_needed_count(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    result=soup.find_all('sup',class_='noprint Inline-Template Template-Fact')
    print(len(result),'citations')
    return f'{len(result)} citations'
    

def get_citations_needed_report(url):
    array = []
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    ps=soup.find_all('p')
    for p in ps:
        citations=p.find_all('a',title='Wikipedia:Citation needed')
        for citation in citations:
            array.append(p.text)

    print (('\n2').join(array))
    return ('\n2').join(array)


       


if __name__ == '__main__':
    URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    get_citations_needed_count(URL)
    get_citations_needed_report(URL)




