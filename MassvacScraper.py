from bs4 import BeautifulSoup
import requests
import re
import sys

#check site
def Marshfield():
    html_text = requests.get('https://vaxfinder.mass.gov/?zip_or_city=&q=marshfield').text #put link for specific site
    soup = BeautifulSoup(html_text, 'lxml')
    #find html for both blocks of text
    divClass = soup.find_all('span', class_ = 'text')
    divClassTxt = str(divClass)
    vacHtml = open('MassvacScraperDocMarsh.txt', 'r') #create .txt in same folder to call on
    vacHtmlRead = vacHtml.read()
    #if new data is different from existing, overwrite txt file with new data
    if divClassTxt != vacHtmlRead:
        vacHtml = open('MassvacScraperDocMarsh.txt', 'w')
        vacHtml.write(divClassTxt)
        vacHtml.close()

    def check():
        with open('MassvacScraperDocMarsh.txt') as f:
            if 'Available' in f.read():
                return(True)
    
    if check():
        return(True)


#send sms
import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('<your email>', '<email password>')

import time
startTime = time.time()
resultCounter = 0
while True:
    print('refresh')
    if Marshfield():
        server.sendmail('MassvacScraper', '<phone number @ carrier email to text service>', 'there are vaccines available at marshfield')
        resultCounter += 1

    if resultCounter >= 1:
        sys.exit()
    time.sleep(15.0 - ((time.time() - startTime) % 15.0))