import os
from bs4 import BeautifulSoup
import requests

url = 'https://www.scotiabank.com/ca/en/commercial-banking/scotia-connect-simple/'

listoflinks = ["payments.html", "administration.html",
               "reporting.html", "additional-services.html"]

for item in listoflinks:
    res = requests.get(url + item, headers={'User-Agent': 'Mozilla/5.0'})

    soup = BeautifulSoup(res.text, "html.parser")

    articles = soup.find_all("div", {"class": "card-content"})

    for card in articles:
        rows = card.find_all('div')

        for row in rows:

            details = row.find('p').getText().strip()
            link = row.find("a")['href']


            file = open("keywords.txt","a")
            L = [details, link]
            file.writelines(L) 
            file.close()

            print(details)
            print(link)

