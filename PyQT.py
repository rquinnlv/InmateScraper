import scraperwiki
import requests
from bs4 import BeautifulSoup

def cityLasVegasInmate(name):
    data = {'txtFirst': name}
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    url = 'http://www5.lasvegasnevada.gov/InmateSearch/'
    inmates = requests.post(url, data=data, headers=headers)

    soup = BeautifulSoup(inmates.content)
    table = soup.find(id="GridView1")

    iterow = iter(table.findAll('tr'))
    next(iterow)
    for row in iterow:
        col = row.findAll('td')
        data = {'id': col[1].string.strip(),
                'name': col[0].string.strip(),
                'age': col[2].string.strip(),
                'gender': col[4].string.strip(),
                'book_date': col[5].string.strip()}

        scraperwiki.sqlite.save(unique_keys=['id'], data=data)

def clarkCountyInmate(name):
    data = ('__VIEWSTATE=%2FwEPDwUIOTE5NTg4NjhkZGvx05uXGR%2BWuRIOdPjT9KzcmuLh1J8Zk1gT0J0aC2Wi&'
            '__EVENTVALIDATION=%2FwEdAAWCIueLxX7W6RwIfnVWJPj0JNOHGRTiA26VmVCqyHoxqsWzilCqUZiLm2Tkt0sWoCWjOglmm5fGSk5Ukp'
            'FsfK4enirgrpbTwEsK9BgCJuFqya%2FmyQJ7PsrYEacOYfCQSaPsSvX6AACoCDB8vMSi31O9&'
            'TxtID=&'
            'txtName=' + name +
            '&SearchName=++Submit++')
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    url = 'http://redrock.clarkcountynv.gov/ccdcincustody/incustodysearch.aspx'
    inmates = requests.post(url, data=data, headers=headers)

    soup = BeautifulSoup(inmates.content)
    table = soup.find(id="DataGrid1")

    iterow = iter(table.findAll('tr'))
    next(iterow)
    for row in iterow:
        col = row.findAll('td')
        data = {'id': col[1].string.strip(),
                'name': col[2].string.strip(),
                'age': col[6].string.strip(),
                'gender': col[8].string.strip(),
                'book_date': col[3].string.strip()}

        scraperwiki.sqlite.save(unique_keys=['id'], data=data)

cityLasVegasInmate('Ryan')
clarkCountyInmate('Ryan')