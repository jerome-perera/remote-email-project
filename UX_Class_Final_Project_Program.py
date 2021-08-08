from bs4 import BeautifulSoup
import urllib.request
import csv
import pandas as pd   #Reading the excel file
import smtplib   #For a connection between the gmail and python scripts
from email.message import EmailMessage   #Sending emails

def sendEmail(to, sub, msg, msg1, msg2):
    print(f"email to {to} \nsend with subject: {sub}\nmessage: {msg}")
    email = EmailMessage()
    email['from'] = 'Jerome Perera'
    email['to'] = f'{to}'
    email['subject'] = f'{sub}'
    email.set_content(f'{msg}, {msg1}, {msg2}')

    with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as smtp:

        smtp.ehlo()
        smtp.starttls()
        smtp.login('jerome.s.perera@gmail.com', 'shanilka!$')
        smtp.send_message(email)
        print("Email send")
    pass

def scrapeLink(url):
    res = BeautifulSoup(urllib.request.urlopen(url).read(), 'lxml')
    print("Scraping link...\n")
    chart = res('table', {"class" : "wikitable"})[0].find_all('tr')
    for row in chart:
        col = row.findChildren(recursive = False)
        col = [element.text.strip() for element in col]
        print(col)
        
link = input("Enter the link you want to be scraped: ")
scrapeLink(link)
file = pd.read_excel("dataoutput.xlsx")
print(file)
for index, item in file.iterrows():
    sendEmail("goldencoyote1469@gmail.com", item['Subject'], item['Message'], item['Message 1'], item['Message 2'])
    
