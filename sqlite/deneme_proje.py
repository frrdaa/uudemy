from kutuphane import *

#import * diyerek kutuphanenin içindeki classları kullanabilir hale geldik

print ("""*************************************

Kütüphane programına hoşgeldiniz.

İşlemler;

1.Kitapları göster

2.Kitap sorgulama

3.Kitap ekle

4.Kitap sil

5.Baski yükselt

Çıkmak için "q"ya basin

*************************************

""")
kutuphane = Kutuphane()

while True:
    islem = input("Yapacağınız işlem:")

    if(islem == "q"):
        print("Program sonlandırılıyor.....")
        print("Yine bekleriz....")
        break

    elif (islem == "1"):
        kutuphane.kitaplari_goster()

    elif (islem == "2"):
        isim = input ("hangi kitabı istiyorsunuz?")
        print("kitap sorgulanıyor...")
        time.sleep(2)

        kutuphane.kitap_sorgula(isim)

    elif (islem == "3"):
        isim = input ("isim:")
        yazar = input("yazar:")
        yayinevi = input("yayinevi:")
        tur = input("tur:")
        baski = int(input("baski:"))

        yeni_kitap = Kitap(isim,yazar,yayinevi,tur,baski)

        print("kitap ekleniyor...")
        time.sleep(2)

        kutuphane.kitap_ekle(yeni_kitap)
        print("kitap eklendi...")

    elif (islem == "4"):
        isim = input("hangi kitabı silmek istiyosunuz? ")

        cevap = input("emin misiniz? (E/H)")

        if(cevap == "E"):
            print("kitap siliniyor...")
            time.sleep(2)
            kutuphane.kitap_sil(isim)
            print("kitap silindi...")

    elif (islem == "5"):
        isim = input("hangi kitabın baskısını yukseltmek istiyorsunuz?")
        print("baski yukseltiliyor...")
        time.sleep(2)
        kutuphane.baski_yukselt(isim)
        print("baski yukseltildi...")

    else: print("Geçersiz işlem")