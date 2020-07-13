"""import requests

url = "http://data.fixer.io/api/latest?access_key=196349c5655d51ff06515edb14d40dad"

birinci_doviz = input ("Birinci Döviz:")
ikinci=doviz = input("İkinci Döviz:")

response = requests.get(url + birinci_doviz)


json_verisi = response.json()
print(json_verisi["rates"][ikinci_doviz])
"""
#mail uygulaması
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys #hata mesajı yazmak için

mesaj = MIMEMultipart()
mesaj["From"] = "ferdaozturk5@gmail.com"
mesaj["To"] = "coskun.m.murat@gmail.com"
mesaj["Subject"] = "Smtpmail gönderme"

yazi = """

Smtp ile mail gönderiyorum
Hocam sizlere çok teşekkür ediyorum çok verimli geçiyor dersleriniz
Emeğinize sağlık:)
Öğrenciniz Ferda Öztürk

"""

mesaj_govdesi = MIMEText(yazi,"plain")
mesaj.attach(mesaj_govdesi)

#tryla servera bağlandık
try:
    mail =smtplib.SMTP("smtp.gmail.com",587)

    mail.ehlo()

    mail.starttls()

    mail.login("ferdaozturk5@gmail.com","Esrefese16.")

    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())

    print("Mail başarıyla gönderildi...")

    mail.close()

except:
    sys.stderr.wwrite("Bir sorun oluştu.")
    sys.stderr.flush()