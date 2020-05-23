import requests
from bs4 import BeautifulSoup
import pprint

url="https://www.mohfw.gov.in/"

def getStateWiseCovidData():
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"html.parser")
    table_body=soup.find('section',attrs={"id": "state-data"}).find("table").find('tbody')

    rows = table_body.find_all('tr')
    data=[]
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        #data.append({"State":cols[0],"Total Case":cols[1],"Cured":cols[2],"Deaths":cols[4]})
        data.append([ele for ele in cols if ele])  # Get rid of empty values
    pprint.pprint(data)

def parseSummaryData(data):
    try:
        res = []
        active = data[0].getText().strip().split('\n')[0]
        cured = data[1].getText().strip().split('\n')[0]
        deaths = data[2].getText().strip().split('\n')[0]
        migrated = data[3].getText().strip().split('\n')[0]
        res.append({"Active Case": active, "Cured": cured, "Deaths": deaths, "Migrated": migrated})
    except:
        print("Error to Parse Covid Data")
        res.append({"Active Case": 0, "Cured": 0, "Deaths": 0, "Migrated": 0})
    return res



def getSummarizedCovidData():
    try:
        result = []
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        data = soup.find('div', attrs={"class": "site-stats-count"}).find('ul').find_all("li")
        result=parseSummaryData(data)
        print(result)
    except:
        print("Error to Scrap Data From Source WebSite")
        result.append({"Active Case": 0, "Cured": 0, "Deaths": 0, "Migrated": 0})
    return result



getSummarizedCovidData()

#getStateWiseCovidData()



