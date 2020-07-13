"""
Örnek özellikler;

1. Şarkı İsmi <<<isim
2. Sanatçı<<< sanatci
3. Albüm<<< album
4. Prodüksiyon Şirketi <<<sirket
5. Şarkı Süresi <<<sure

Örnek Metodlar;

1. Veritabanındaki Toplam Şarkı Süresini Hesaplayan Metod
2. Şarkı Ekle
3. Şarkı Sil
"""

import sqlite3
import time

class sarki():
    def __init__(self,isim,sanatci,album,sirket,sure):

        self.isim = isim
        self.sanatci = sanatci
        self.album = album
        self.sirket = sirket
        self.sure = sure

    def __str__(self):

        return "isim{}\nsanatci{}\nalbum{}\nsirket{}\nsure{}".format(self.isim,self.sanatci,self.album,self.sirket,self.sure)

class Sarki_listesi():
    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("sarki_listesi.db")
        self.cursor = self.baglanti.cursor()
        sorgu = "Create Table If Not Exists sarkilar(isim TEXT, sanatci TEXT, album TEXT, sirket TEXT, sure INT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def baglanti_kes(self):
        self.baglanti.close()

    def sarki_ekle(self,sarki):
        sorgu = "Insert Into sarkilar values (?,?,?,?,?)"
        self.cursor.execute(sorgu,(sarki.isim,sarki.sanatci,sarki.album,sarki.sirket,sarki.sure,))
        self.baglanti.commit()

    def sarki_sil(self,isim):
        sorgu = "Delete From sarkilar where isim = ?"
        self.cursor.execute(sorgu,(isim,))
        self.baglanti.commit()

    def sure_hesapla(self):
        sorgu = "Select * From sarkilar "

        self.cursor.execute(sorgu)

        sarkilar = self.cursor.fetchall()

        toplam = 0
        for i in sarkilar:
            toplam += i[4]
        print(toplam)
