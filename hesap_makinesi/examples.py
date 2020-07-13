"""
Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.

 Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

 BKİ 18.5'un altındaysa -------> Zayıf

 BKİ 18.5 ile 25 arasındaysa ------> Normal

 BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

 BKİ 30'un üstündeyse -------------> Obez


boy = float(input("boyunuzu giriniz:"))
kilo = float(input("kilonuzu giriniz:"))

kitle_indeks = kilo / (boy**2)

if kitle_indeks < 18.5 :
    print("zayif")
elif 18.5 < kitle_indeks < 25:
    print("normal")
elif 25 < kitle_indeks < 30:
    print("fazla kilolu")
elif 30 < kitle_indeks:
    print("obez")

a = int(input("ilk sayi:"))
b = int(input("ikinci sayi:"))
c = int(input("üçüncü sayi:"))

if a > b and a > c:
    print("en buyuk sayi {}dir".format(a))
if b > a and b > c:
    print("en buyuk sayi {}dir".format(b))
if c > a and c > b:
    print("en buyuk sayi {}dir".format(c))

vize1 = int(input("vize1 notunuz:"))
vize2 = int(input("vize2 notunuz:"))
final = int(input("final notunuz:"))

toplam = vize1*0.3 + vize2*0.3 +final*0.4

print (toplam)

if toplam >= 90:
    print("AA")
elif toplam >= 85:
    print("BA")
elif toplam >= 80:
    print("BB")
elif toplam >= 75:
    print("CB")
elif toplam >= 70:
    print("CC")
elif toplam >= 65:
    print("DC")
elif toplam >= 60:
    print("DD")
else:
    print("FF")


sekil = input("ucgen mi dortgen mi ")

if sekil == "dortgen" :
    a = int(input("ilk kenar uzunlugunu giriniz "))
    b = int(input("ikinci kenar uzunlugunu giriniz "))
    c = int(input("ucuncu kenar uzunlugunu giriniz "))
    d = int(input("dorduncu kenar uzunlugunu giriniz "))
    if a == b == c == d :
        print("kare")
    elif a == b and c == d and a != c or a == c and b == d and a != b or a == d and c == b and a != b:
        print ("dikdörtgen")
    else:
        print("çeşitkenar dörtgen")
else:
    a = int(input("ilk kenar uzunlugunu giriniz "))
    b = int(input("ikinci kenar uzunlugunu giriniz "))
    c = int(input("ucuncu kenar uzunlugunu giriniz "))
    if abs(a-b) < c < a+b or abs(b-c) < a < c+b or abs(a-c) < b < a+c :
        if a == b == c:
            print("eşkanar üçgen")
        elif a == b and b != c or a == c and b != c:
            print("ikizkenar üçgen")
        else:
            print ("çeşitkenar üçgen")
    else:
        print ("üçgen olma şartını sağlamıyor")
"""
# LOOP EXAMPLES

"""Problem 1
Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.
Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. 
Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)"""
"""
a = int(input("bir sayi giriniz:"))

toplam = 1
i = 2
while (i<a):
    if ((a%i) == 0):
        toplam += i
    i+=1

if (toplam == a):
        print("sayi mukemmeldir")
else:
        print("baska bir sayi deneyin")
"""
"""
Problem 2
Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.
Örnk olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı
( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.
Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4
"""


"""Problem 3
1'den 10'kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.
İpucu: İç içe 2 tane for döngüsü kullanın. Aynı zamanda sayıları range() fonksiyonunu kullanarak elde edin."""
"""
carpim =1

for i in range (1,10):
    for j in range (1,10):
        carpim = i*j
        print("{}x{}={}".format(i,j,carpim))
"""

"""Problem 4
Her bir while döngüsünde kullanıcıdan bir sayı alın ve 
kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin. 
Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.
İpucu : while döngüsünü sonsuz koşulla başlatın ve kullanıcı q'ya basarsa döngüyü break ile sonlandırın."""

"""toplam = 0

while True:
    a = input("bir sayi giriniz:")
    if (a == "q"):
        print("programdan çıkılıyor...")
        break
    a = int(a)
    toplam += a
print (toplam)"""

"""Problem 5
1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın. Bu işlemi continue ile yapmaya çalışın.
"""

"""for i in range(1,100):
    if (i%3==0):
        print (i)
    else:
        continue"""
"""Problem 6
Buradaki problemin çözümünü derslerimizde özellikle öğrenmedik.
Burada mantık yürüterek ve list comprehension kullanarak 1'den 100'e kadar olan sayılardan sadece çift
sayıları bir listeye atmayı yapmayı çalışın.
Not: Programlamada her detayı öğrenemeyiz. Bunun için bazı yerlerde deneme yanılma yoluyla da öğrendiğimiz şeyler olur.
Bu problemde deneme yanılma yoluyla list comprehension'ın koşullu durumlarla kullanımını öğreneceksiniz.
İpucu: Basit düşünmeye çalışın.
"""

"""liste = list()
for i in range (1,100):
    if (i%2==0):
        liste.append(i)
    i+=1
print (liste)
"""

"""liste = [x for x in range(1,101) if x % 2 == 0]
print(liste)

#asal mı

def asal_mi(sayi):
    if sayi == 1:
        return False

    elif sayi == 2:
        return True

    else:
        for i in range (2,sayi):
            if (sayi % i == 0):
                return False
        return True

while True:
    sayi = input("sayi:")

    if (sayi == "q"):
        break
    else:
        sayi = int(sayi)

        if(asal_mi(sayi)):
            print(sayi, "asal bir sayidir")
        else :
            print(sayi,"asal bir sayi değildir")"""

# tam bölen bulma

"""def tam_bolen(sayi):
    tam_bolenler =[]

    for i in range(2,sayi):
        if (sayi%i == 0):
            tam_bolenler.append(i)
    return tam_bolenler


while True:
    sayi = input("sayi:")

    if (sayi == "q"):
        break
    else:
        sayi = int(sayi)

        print("tam bolenler",tam_bolen(sayi))"""

#         FONKSİYONLAR ÖDEVİ

"""Problem 1
1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın. 
Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.
Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır.
 Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6)."""

"""def mukemmel_sayi(sayi):
    tam_bolen=[]
    for i in range(2,sayi):
        if (sayi % i == 0):
            tam_bolen.append(i)
    toplam = 0
    for j in tam_bolen:
        toplam = toplam + j
    return toplam

while True:
    sayi = input("sayi:")

    if sayi == "q":
        break

    sayi = int(sayi)

    elif (sayi == mukemmel_sayi(sayi)):
        print(sayi, "mukemmeldir")
    else:
        print(sayi,"mukemmel degildir")"""


"""Problem 2
Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın."""
"""
def ebob(sayi1,sayi2):
    bolen1 = [] # 2 4 6 12
    bolen2 = [] # 2,3,4,8,12,24
    ortak_bolenler = []
    c = 0
    for i in range(2,sayi1+1):
        if (sayi1) % i == 0:
            bolen1.append(i)
    for i in range(2,sayi2+1):
        if (sayi2) % i == 0:
            bolen2.append(i)
    for i in bolen1:
        for j in bolen2:
            if i == j:
                ortak_bolenler.append(j)
    for i in ortak_bolenler:
        if i > c:
            c = i
    return c

sayi1 = int(input("ilk sayi:"))
sayi2 = int(input("ikinci sayi:"))

print("ebobları", ebob(sayi1,sayi2))"""

"""Problem 3
Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK) dönen bir tane fonksiyon yazın.

Problem için şu siteye bakabilirsiniz;"""
"""
def ekok(sayi1,sayi2):
    bolen1 = [] # 2 4 6 12
    bolen2 = [] # 2,3,4,8,12,24
    ortak_bolenler = []
    c = 100000
    for i in range(2,sayi1+1):
        if (sayi1) % i == 0:
            bolen1.append(i)
    for i in range(2,sayi2+1):
        if (sayi2) % i == 0:
            bolen2.append(i)
    for i in bolen1:
        for j in bolen2:
            if i == j:
                ortak_bolenler.append(j)
    for i in ortak_bolenler: # 3
        if i < c: # 3<2
            c = i
    if c == 100000:
        return 1

    return c

sayi1 = int(input("ilk sayi:"))
sayi2 = int(input("ikinci sayi:"))

print("ekokları", ekok(sayi1,sayi2))"""

"""Problem 4
Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.
Örnek: 97 ---------> Doksan Yedi"""

"""birler =  ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]

def okunus(sayi):
    birinci = sayi % 10 #97 ise 7 birler bas
    ikinci = sayi // 10 #97 ise 9 onlar bas

    return onlar[ikinci] + " " + birler[birinci]


sayi = int(input("Sayı:"))

print(okunus(sayi))
"""
"""Problem 5
1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran bir fonksiyon yazın.
(a <= 100,b <= 100)"""
"""
def pisagor():
    for i in range(1,101):
        for j in range(1,101):
            for k in range(1,101):
                if i**2 + j**2 == k**2:
                   print(i,j,k,"pisagor sağlandı")



print (pisagor())

"""
"""
#hocanın yöntemi:

def pisagor_bulma():
    pisagor_listesi = list()
    for i in range(1, 101):
        for j in range(1, 101):

            c = (i ** 2 + j ** 2) ** 0.5

            if (c == int(c)):
                pisagor_listesi.append((i, j, int(c)))

    return pisagor_listesi

print(pisagor_bulma())
"""


# HATALARİSTİSNALAR

#sadece rakamları bastır

"""liste = ["345","sadas","324a","14","kemal"]

for i in liste:
    try:
        i = int(i)
        print(i)
    except:
        pass"""
"""
Bir sayının çift olup olmadığını sorgulayan bir fonksiyon yazın.
Bu fonksiyon, eğer sayı çift ise return ile bu değeri dönsün. 
Ancak sayı tek sayı ise fonksiyon raise ile ValueError hatası fırlatsın.
Daha sonra, içinde çift ve tek sayılar bulunduran bir liste tanımlayın ve liste üzerinde 
gezinerek ekrana sadece çift sayıları bastırın."""
"""
def cift_mi(sayi):
    if (sayi%2 == 0):
        return sayi
    else:
        raise ValueError

liste = [1,2,3,4,5,6,7,8,9,10,11,12,13]

for i in liste:
    try :
        cift_mi(i)
        print(cift_mi(i))
    except ValueError:
        pass"""

# BİLGİSAYAR
"""

import time

class Bilgisayar():
    def __init__(self, pc_durum = "kapali", sarj = 100,masaustu_klasorleri=["film_ss"]):
        self.pc_durum = pc_durum
        self.sarj = sarj
        self.masaustu_klasorleri = masaustu_klasorleri

    def pc_ac(self):
        parola = 1234
        deneme_hakki = 3
        if (self.pc_durum == "açık"):
            print("pc zaten açık")

        else:
            print("pc açılıyor...")
            self.pc_durum = "açık"
            print(Oturum listesi:
            1.Misafir Kullanıcı(şifresiz)
            2.Admin(şifreli)
            )
            islem = input("Açacağınız oturumu seçiniz: ")

            if (islem == "1"):
                print("oturum açılıyor")
            elif (islem == "2"):
                while True:
                    if (deneme_hakki == 0):
                        print("Giriş hakki bitti!!!")
                        print("sistem kapatiliyor")
                        self.pc_durum = "kapalı"
                        break
                    g_parola = int(input("Parolayı giriniz: "))
                    if (parola == g_parola):
                        print("Sisteme Hosgeldiniz...")
                        break
                    else:
                        print("Yanlış şifre")
                        deneme_hakki -= 1
            else:
                print("1 veya 2yi seçin")

    def pc_kapat (self):
        if(self.pc_durum == "kapalı"):
            print("zaten kapalı")

        else:
            print("pc kapanıyor...")
            self.pc_durum = "kapalı"


    def sarj_durumu(self):

        while True:

            if (10<sarj<25):
                print("düşük pil moduna geçiliyor")
            elif (5<sarj<10):
                print("pil ömrü azalıyor")
            elif (sarj<5):
                print("bilgisayar kapanmak üzere")
            elif (sarj == 100):
                print("batarya dolmuştur şarjtan çekiniz")

    def oturum_acma(self):
        parola = "1234"
        deneme_hakki=3
        if (oturum_ac == "kapali"):
            print("kullanıcı parola giriniz:")
            print(input(parola))
            while True:

                if (parola == parola):
                    print("oturum aciliyor")
                    break
                else:
                    print("yanlis parola")
                    deneme_hakki -= 1
                    if (deneme_hakki==0):
                        print("deneme hakkınız bitmiştir")
                        break

    def klasor_ekle(self,klasor_ismi):
        print ("klasör ekleniyor...")
        time.sleep(1)
        self.masaustu_klasorleri.append(klasor_ismi)
        print("klasor eklendi...")

    def __len__(self):
        return len(self.masaustu_klasorleri)

    def __str__(self):
        return "Pc durumu: {}\nŞarj Yüzdesi: {}\nKullanici Girişi: {}\nMasaustu: {}".format(self.pc_durum,self.sarj,self.oturum_ac,self.masaustu_klasorleri)

bilgisayar = Bilgisayar()

print(PC UYGULAMASI

1.PC aç

2.Pc kapat

3.Şarj yüzdesi

4.Klasör ekle

5.Klasör sayısını öğrenme

6.PC bilgileri 

Çıkmak için 'q'ya basın 
)

while True:

    islem = input("Bilgisayarda ne yapmak istersiniz? ")

    if(islem =="q"):
        print("program sonlandırılıyor...")
        break

    elif(islem=="1"):
        bilgisayar.pc_ac()

    elif(islem=="2"):
        bilgisayar.pc_kapat()

    elif(islem=="3"):
        bilgisayar.sarj_durumu()


    elif (islem == "4"):
        klasor_isimleri = input("klasor isimlerini , koyarak girin:")
        masaustu_klasorleri = [klasor_isimleri.split(",")]

        for eklenecekler in klasor_isimleri:
            bilgisayar.klasor_ekle(eklenecekler)


    elif (islem == "5"):
        print("klasör sayısı", len(bilgisayar))


    elif (islem == "6"):
        print(bilgisayar)

    else:
        print("geçersiz işlem")


"""
"""liste = [(3,4),(10,3),(5,6),(1,9)]"""
"""liste = []
for i in range(0,len(list)):
    tuple = list[i]
    liste.append(tuple[0]*tuple[1])
print(liste)"""

"""def alan_hesapla(tuple):
    return tuple[0]*tuple[1]
print(list(map(alan_hesapla,liste)))

liste = [(3,4,5),(6,8,10),(3,10,7)]

def ucgen_mi(tuple):
    if abs(tuple[0]-tuple[1])<tuple[2]<(tuple[0]+tuple[1]) or abs(tuple[0]-tuple[2])<tuple[1]<(tuple[0]+tuple[2]) or abs(tuple[1]-tuple[2])<tuple[0]<(tuple[1]+tuple[2]):
        return True
    else:
        return False

print(list(filter(ucgen_mi, liste)))

from functools import reduce
liste=[1,2,3,4,5,6,7,8,9,10]

liste2 = (list(filter(lambda x: x%2==0,liste))) #[2, 4, 6, 8, 10]
print(reduce(lambda x,y: x+y,liste2))#30

isimler = ["Kerim", "Tarık", "Ezgi", "Kemal", "İlkay", "Şükran", "Merve"]

soyisimler = ["Yılmaz", "Öztürk", "Dağdeviren", "Atatürk", "Dikmen", "Kaya", "Polat"]

for i in range(0,len(soyisimler)):
    print(list(zip(isimler,soyisimler)))
    """
#decorator
#1'den 1000'e kadar olan asal sayıları ekrana yazdıran bir program yazın. Daha sonra bir tane
# decorator fonksiyon kullanarak bu fonksiyona 1'den 1000'e kadar olan mükemmel
# sayıları yazdırma özelliği ekleyin.

"""def mukemmel_sayi(sayi):
    tam_bolen=[]
    for i in range(2,sayi):
        if (sayi % i == 0):
            tam_bolen.append(i)
    toplam = 0
    for j in tam_bolen:
        toplam = toplam + j
    return toplam
while True:
    sayi = input("sayi:")
    if sayi == "q":
        break
    sayi = int(sayi)
    elif (sayi == mukemmel_sayi(sayi)):
        print(sayi, "mukemmeldir")
    else:
        print(sayi,"mukemmel degildir")"""
"""def mukemmel_mi(func):
    def wrapper(sayilar):
        for sayi in range(1, 1001):
            toplam = 0
            i = 1
            while (i < sayi):
                if (sayi % i == 0):
                    toplam += i
                i += 1
            if (toplam == sayi):
                print(sayi)
    return wrapper

@mukemmel_mi
def asal(sayilar):
    asal_sayilar = [2] #0 1 2 3 4 5 6 7 8 9
    for i in range(3,sayilar): #0
        bolundu = False
        for j in range(2, i):
            if i % j == 0:
                bolundu = True
                break
        if bolundu == False:
            asal_sayilar.append(i)

    return asal_sayilar

print(asal(1000))"""

import os

pdf = list()
txt = list()
mp4 = list()

for klasor_yolu, klasor_isimleri,dosya_isimleri in os.walk("/Users/ferdaozturk"):
    for i in dosya_isimleri:
        if (i.endswith(".pdf")):
            pdf.append(i)

for klasor_yolu, klasor_isimleri,dosya_isimleri in os.walk("/Users/ferdaozturk"):
    for i in dosya_isimleri:
        if (i.endswith(".txt")):
            txt.append(i)

for klasor_yolu, klasor_isimleri,dosya_isimleri in os.walk("/Users/ferdaozturk"):
    for i in dosya_isimleri:
        if (i.endswith(".mp4")):
            mp4.append(i)


with open("pdf_dosyalarim.txt", "w", encoding="utf-8") as file1:
    for i in pdf:
        file1.write(i)
with open("txt_dosyalarim.txt", "w", encoding="utf-8") as file2:
    for i in txt:
        file2.write(i)
with open("mp4_dosyalarim.txt", "w", encoding="utf-8") as file3:
    for i in mp4:
        file3.write(i)




















