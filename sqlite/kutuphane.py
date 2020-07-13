"""Kütüphane Projesi"""

import sqlite3
import time

class Kitap():
    def __init__(self, isim,yazar,yayinevi,tur,baski):

        self.isim = isim
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.tur = tur
        self.baski = baski

    def __str__(self):

        return "Kitap ismi\nYazar: {}\nYayinevi: {}\nTur: {}\nBaski: {}\n".format(self.isim,self.yazar,self.tur,self.baski)

class Kutuphane():

    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):

        self.baglanti = sqlite3.connect("kutuphane.db") #sqlite3.connect fonksiyonuyla sen bana kutuphane db diye bir şey oluştur tarzında bir şey söylemiş oluyoruz

        self.cursor = self.baglanti.cursor() #cursor işlemiyle ben bu veritabanı zerinde bir tane işlem gerçekleştircek bir cursor oluşturuyorum

        #şimdi bu veritabanı içinde bir tane tablo oluşturcaz
        sorgu = "Create Table If not exists kitaplar (isim TEXT, yazar TEXT, yayinevi TEXT,tur TEXT,baski INT)" #tablonun ismi: kitalar
        self.cursor.execute(sorgu) #sorguyu çalıştırıyoruz ve tablomuzu oluşturuyoruz
        self.baglanti.commit() #bu işlemin veritabanı üzerinde etkili olması için bunu söylememiz gerekiyor

    def baglantiyi_kes(self):
        self.baglanti.close()

    def kitaplari_goster(self):

        sorgu = "Select * From kitaplar"

        self.cursor.execute(sorgu)

        kitaplar = self.cursor.fetchall() #kitaplar değişkenimiz içinde bilgiler gelicel

        if (len(kitaplar)==0):
            print("kütüphanede kitap bulunmuyor...")

        else:
            for i in kitaplar: #kitapların içinde demetler var i bu demetlerin her bir elemanı
                kitap = Kitap(i[0],i[1],i[2],i[3],i[4]) #i[0]=ismi,i[1]=yazarı,i[2]=türü...
                print(kitap) #kitap classındaki stryi yazdırıyor

    def kitap_sorgula(self,isim):
        sorgu = "Select * From kitaplar where isim = ?" #isme gör bunu sorgulamaya çalışcam

        self.cursor.execute(sorgu,(isim,)) #ismi demet halinde gönderiyoruz #bu sorgumu çalıştırmak istediğimi söylüyorum

        kitaplar = self.cursor.fetchall()

        if (len(kitaplar)==0):
            print("böyle bir kitap bulunmuyor")

        else:
            kitap = Kitap(kitaplar[0][0],kitaplar[0][1],kitaplar[0][2],kitaplar[0][3],kitaplar[0][4]) #ilk kitabımızdaki isme yazara baskıya türe falan ulaştık
            print(kitap)

    def kitap_ekle(self,kitap):

        sorgu= "Insert Into kitaplar Values(?,?,?,?,?)"

        self.cursor.execute(sorgu,(kitap.isim, kitap.yazar,kitap.yayinevi,kitap.tur,kitap.baski))
        self.baglanti.commit() #bunu yapmazsak veritabanına bağlantımız gitmicektir yani güncellenmicek

    def kitap_sil(self,isim):

        sorgu = "Delete From Kitaplar where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        self.baglanti.commit() #veritabanını güncellemiş oluyoruz

    def baski_yukselt(self,isim):

        sorgu = "Select * From kitaplar where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        kitaplar = self.cursor.fetchall()

        if (len(kitaplar)==0):
            print("Böyle bir kitap yok")

        else:
            baski = kitaplar[0][4]

            baski += 1
            sorgu2 = "Update kitaplar set baski = ? where isim =? "

            self.cursor.execute(sorgu2,(baski,isim)) #demetimin ilk elemanı baski ikinci elemanı isim

            self.baglanti.commit()

