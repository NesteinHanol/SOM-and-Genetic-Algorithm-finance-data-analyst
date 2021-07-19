# -*- coding: cp1254 -*-
##import urllib2
##import re
##htmlfile=urllib2.urlopen("https://www.investing.com/commodities/copper")
##htmltext=htmlfile.read()
##
##regex='<span class="arial_26 inlineblock pid-8831-last" id="last_last" dir="ltr">(.+?)</span>'
##pattern = re.compile(regex)
##price = re.findall(pattern,htmltext)


import urllib2
import re

url = "https://www.investing.com/commodities/copper"
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

req = urllib2.Request(url, headers=headers)

response = urllib2.urlopen(req)

your_json = response.read()
response.close()

regex='<span class="arial_26 inlineblock pid-8831-last" id="last_last" dir="ltr">(.+?)</span>'
pattern = re.compile(regex)
price = re.findall(pattern,your_json)

import time
#time.sleep(3600) 1 saat demek
#s=x[0]+x[2]+x[3]+x[4]+"."+x[6]+x[7] altın için gelen deger duzenle
#hepsi icin amerikan sunucusundan cek


##import smtplib                           #smtplib modulunu projemize ekledik
### Hesap bilgilerimiz
##kullanıcı="gmailadresimiz@gmail.com"
##kullanıcı_sifresi = 'gmailsifremiz'
##alıcı = 'gönderilen@mail.com'            # alıcının mail adresi
##konu = 'Selam'
##msj = 'Naber!'
### bilgileri bir metinde derledik
##email_text = """
##From: {}
##To: {}
##Subject: {}
##{}
##""" .format(kullanıcı,alıcı, konu, msj)
##try:
##server = smtplib.SMTP('smtp.gmail.com:587')   #servere bağlanmak için gerekli host ve portu belirttik
##server.starttls() #serveri TLS(bütün bağlantı şifreli olucak bilgiler korunucak) bağlantısı ile başlattık
##server.login(kullanıcı, kullanıcı_sifresi)   # Gmail SMTP server'ına giriş yaptık
##server.sendmail(kullanıcı, alıcı, email_text) # Mail'imizi gönderdik 
##server.close()     # SMTP serverimizi kapattık
##print ('email gönderildi')
##except:
##print("bir hata oluştu")
