from sarki_listesi import *

print("""*************************************

Kütüphane programına hoşgeldiniz.

İşlemler;

1. Şarkı Ekle
2. Şarkı Sil
3. Veritabanındaki Toplam Şarkı Süresini Hesaplayan Metod

Çıkmak için "q"ya basin

*************************************

""")
sarki_listesi = Sarki_listesi()

while True:
    islem = input("yapacağınız işlem?")

    if (islem == "q"):
        print("Program sonlandırılıyor...")
        print("yine bekleriz...")
        time.sleep(2)
        break

    elif (islem == "1"):
        isim = input("isim")
        sanatci = input("sanatci")
        album = input("album")
        sirket = input("sirket")
        sure = int(input("sure"))

        yeni_sarki = sarki(isim,sanatci,album,sirket,sure)
        print("sarki ekleniyor...")
        time.sleep(2)

        sarki_listesi.sarki_ekle(yeni_sarki)
        print("sarki eklendi")

    elif (islem == "2"):
        isim = input("isim")

        sarki_listesi.sarki_sil(isim)
        print("sarki siilindi")

    elif (islem == "3"):
        sarki_listesi.sure_hesapla()
    else:
        print("gecersiz işlem")
