import requests
from bs4 import BeautifulSoup
import smtplib

def sendMail():
    server = smtplib.SMTP('smtp.gmail.com',587)

    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('your-mail','your-password')

    msg = f"Hey!, Price of {title} has become low\n\n CLick on this link to buy {URL}"

    server.sendmail(
        'your-mail',
        'receiver-mail',
         msg
    )

    print(msg)
    print('Mail Sent')

    server.quit()


URL ='https://www.amazon.in/Fossil-Fenmore-Multifunction-Black-BQ2364/dp/B07R4P572S/ref=sr_1_59_mod_primary_lightning_deal?dchild=1&keywords=watch+black+metal&qid=1600078651&sbo=Tc8eqSFhUl4VwMzbE4fw%2Fw%3D%3D&smid=A2XS4ABRR727IE&sr=8-59'

headers ={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}

page = requests.get(URL,headers=headers)

soup = BeautifulSoup(page.content,'html.parser')

# print(soup.prettify())

title=soup.find(id='productTitle').getText().strip()
print(title)

p = soup.find(id='priceblock_dealprice').getText()
p= p.replace(',','')
price=int(p[2:6])

if(price<=5500):
    print('Buy!! {} is its price'.format(price))
    sendMail()
    
else:
    print('Wait price is {} !!'.format(price))