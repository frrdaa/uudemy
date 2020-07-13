print ("hello world")
# tekli yorum satırı

"""
Çoklu yorum satırı
"""

# kntrl üst r = run the code
"""
k = 35
l = 87
m = 6

toplam = k + l
print (toplam)

bolum = k / m
print (bolum)

tamsayi_bolum = k // m
print (tamsayi_bolum)

ust = 2**3
# 2^3 demek yani 8
print (ust)

kup_kok = 8 ** (1/3)
print(kup_kok)
print (-kup_kok)
"""# basina - koyarsan isaret degistirmis olursun

# STRINGS

print ("""merhaba""")
print ("merhaba")
print ('merhaba')
print ('Ferda\'nin bugun dersi var')
print ("Ferda'nin bugun dersi var")
"""
a = ("jupyter")
print (a[0]) #j
print (a[1]) #u
print (a[2]) #p
print (a[3]) #y
print (a[-3]) #t
print (a[-2]) #e
print (a[-1]) #r"""

# baslama indexi : bitis indexi : atlama degeri
"""
b = ("Yakında yurtdışına gidecegim.")
print(b[4:10])
print (b[:12]) #en baştan 12.karaktere kadar 0dan başlıyor space de karakter
print (b[:-1]) # -1 sondaki karakter demek yani sonuncu karaktere kadar hepsini yazar (cumle sonuna . koymadı) NEDEN?
print (b[::2]) #baslama ve bitis indexi vermemis sadece atlama indexi vermis 2 2 atlayarak yazcak
print (b[4:14:3]) #4ten basla 14 e kadar ama 14 dahil degil 3 er atlayarak yaz
print (b[::-1]) #stringi tersten yaz demek oluyor

print (len(b)) #stringin uzunlugunu soyluyor

x = "yakinda "
y = "yurtdisina "
z = "gidecegim"

m = x + y + z
print (m) # yakinda yurtdisina gidecegim

t = x*3
print (t) # yakinda yakinda yakinda
print ( t + "!" * 3) # yakinda yakinda yakinda !!!

a= "ferda"
a = a + "ozturk"
print (a) # ferdaozturk

print ("printin", "içine", "birden", "çok şey yazarken", "virgülle ayırabilirsin", 190)

n = 3.14
print(type(n)) #float yazdı
print("ocak","şubat", "mart", sep = "-" ) #araya - koyar ocak-şubat-mart
print("ocak","şubat", "mart", sep = "/" ) #ocak/şubat/mart
print("ocak","şubat", "mart", sep = "\n" ) #alt alta yazar
print(*"TBMM", sep = ".") # T.B.M.M"""
#yani * koyarsan tek tek ayırıp printe gönderir yani harflerin aralarına boşluk koymuş olur

#                        FORMATLAMA
"""
a = 3
b = 4
print("{}+{}in toplami {}dir." .format(a,b,a+b))

print("{1} {0} {2}".format("yurtdisina","Ferda","gidecek"))
#Ferda yurtdisina gidecek.

print("{:.2f} {:.2f} {:.3f}" .format(3.1264,5.356,7.5629))"""
#3.13 5.36 7.563 (yuvarlıyor yazmadığı virgülü)

#                            LİSTELER
"""
liste = ["Ferda","2021de","Amalfi'nin","altından","ziplayarak","geçiyor."]
print(type(liste)) #liste
print(len(liste))
liste2 = list("İtalya")
print(liste2) #['İ', 't', 'a', 'l', 'y', 'a']
print(liste[-1]) #geçiyor. -sondaki elemanı yazar-
print(liste[::-1]) #['geçiyor.', 'ziplayarak', 'altından', "Amalfi'nin", '2021de', 'Ferda']
print(liste[:2]) #['Ferda', '2021de']
print(liste[::2]) #['Ferda', "Amalfi'nin", 'ziplayarak']
liste = ["ferda"]
liste2 = ["ozturk"]
toplam = liste + liste2
print(toplam) #['ferda', 'ozturk']
yurtdisi = ["gitcem"]
yurtdisi = yurtdisi * 3
print (yurtdisi) #['gitcem', 'gitcem', 'gitcem']
"""
#                          METOTLAR
"""
liste = ["Almanya","İtalya"]
liste.append("Fransa")
print(liste) #['Almanya', 'İtalya', 'Fransa']
liste.pop(1)
print(liste) #['Almanya', 'Fransa']
liste.pop()
print(liste) #['Almanya']

liste = [5,10,26,11]
liste.sort()
print(liste) #[5, 10, 11, 26]
liste.sort(reverse = True)
print(liste) #[26, 11, 10, 5]

liste = ["Almanya","İtalya","Fransa", "İsviçre"]
liste.sort()
print(liste)
#['Almanya', 'Fransa', 'İsviçre', 'İtalya'] ascııye göre sıralar

liste = [[1,2], [3,4], [5,6]]
print(liste) #[[1, 2], [3, 4], [5, 6]]
#3 e nasıl ulaşırım?
print (liste[1]) #[3, 4]
print (liste[1][0]) #3"""

#             DEMETLER(TUPLELAR)
"""
demet = (1,2,3,4,5,6,7)
print(type(demet)) #<class 'tuple'>
print(demet[4]) #5
print(demet[::2]) #(1,3,5,7)

tuple2 = ("almanya", "almanya", "almanya", "italya","italya", "hollanda")
print(tuple2.count("almanya")) #3
print(tuple2.index ("hollanda")) #5 kaçıncı indexte olduğunu söylüyor
# ASIL ÖZELLİĞİ DEĞİŞMEZ OLMASI SEN BİR KOD YAZARKEN DEĞERLERİN DEĞİŞTİRİLEMEZ OLMASINI İSTİYORSAN LİSTE YERİNE TUPLE KULLANIRSIN
"""
#                      SÖZLÜK (DICTIONARY)
"""
sozluk1 = {"bir":1, "iki":2, "üç":3}
print(type(sozluk1)) #<class 'dict'>
sozluk2 = {}
print(sozluk2) #{}
print(sozluk1["bir"]) #1
sozluk1["dört"] = 4
print(sozluk1) #{'bir': 1, 'iki': 2, 'üç': 3, 'dört': 4}

a = {"bir":[1,2,3,4], "iki":[5,6,7,8], "üç":[9,10,11,12]}
print(a["iki"]) #[5, 6, 7, 8]

print(sozluk1)
print(sozluk1.keys()) #dict_keys(['bir', 'iki', 'üç', 'dört'])
print(sozluk1.values()) #dict_values([1, 2, 3, 4])
print(sozluk1.items()) #dict_items([('bir', 1), ('iki', 2), ('üç', 3), ('dört', 4)])
"""
#                  INPUT FONKSIYONU
"""
name = input("What is your name?\n")
print("Hello", name)

a = int(input("birinci sayi:"))
b = int(input("ikinci sayi:"))
c = int(input("ucuncu sayi:"))

print("toplamlari:", a+b+c)


print("Oyuncu Kaydetme Programi")

ad = input("oyuncunun adi")
soyad = input("oyuncunun soyadi")
takim = input ("oyuncunun takimi")

bilgiler = [ad,soyad,takim]

print("oyuncunun adi: {}\nOyuncunun soyadi:{}\nOyuncunun takimi:{}\n".format(bilgiler[0],bilgiler[1],bilgiler[2]))


#denklemin koklerini bulma programi

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

delta = b**2 - 4*a*c

x1 = (-b - (delta**(1/2))) / (2*a)
x2 = (-b + (delta**(1/2))) / (2*a)

kokler = [x1,x2]

print("ilk kok {}\nikinci kok {}\n" .format(kokler[0],kokler[1]))


#kullanicidan 3 sayi alip ekrana yazdırma(format kullanarak)

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

carpim = a*b*c

print(carpim)


#boy kilo iste Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)

boy = float(input("boy:"))
kilo = float(input("kilo:"))

index = kilo / (boy**2)

print(index)


#Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.

yakit = int(input("kmde ne kadar yakıyor"))
yol = int(input("kac km yol yapiyor"))

fatura = yakit*yol

print (fatura)


#Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.

a = int(input("a:"))
b = int(input("b:"))
c = 0

c = a
a = b
b = c

print("a:{} \nb:{}\n".format(a,b) )


#Hipotenüs Formülü: a^2 + b^2 = c^2

a = int(input("a:"))
b = int(input("b:"))

hipo = (a**2 + b**2)** (0.5)

print (hipo)


print(bool (0)) #false
print(bool (0.0)) #false
print(bool (1)) #true
print(bool (-1)) #true
print(bool (14)) #true

a = None #henuz deger atanmamis demek oluyor
print(a) #none

yas = int(input("yasinizi giriniz"))

if yas < 18:
    print("giremezsiniz!")
else:
    print("hoşgeldiniz")
"""

#                    FOR DONGUSU
"""
liste = [1,2,3,4,5,6,7]

toplam = 0
for eleman in liste:
    toplam = toplam + eleman
print(toplam)

s = "Python"

for i in s:
    print(i)
"""
liste = [(1,2),(3,4,),(5,6)]

for eleman in liste:
    print(eleman)
"""
(1, 2)
(3, 4)
(5, 6)
"""
for (i,j) in liste:
    print("i:{} j:{}".format(i,j))
"""
i:1 j:2
i:3 j:4
i:5 j:6
"""

for (i,j) in liste:
    print(i,j)
"""
1 2
3 4
5 6
"""
"""
sozluk = {"bir":1, "iki":2, "üç":3, "dört":4}
for eleman in sozluk:
    print(eleman)
#bir iki üç dört
for eleman in sozluk.values():
    print(eleman)
#1 2 3 4
for i,j in sozluk.items():
    print("anahtar:", i, "değer",j)"""
"""
anahtar: bir değer 1
anahtar: iki değer 2
anahtar: üç değer 3
anahtar: dört değer 4"""

#              WHILE DONGUSU
"""
i = 0

while (i<10):
    print("i nin değeri",i)
    i+=1

liste = [1,2,3,4,5]

index = 0

while (index < len(liste)):
    print("index:", index, "liste elemanı", liste[index])
    index += 1"""
#           RANGE fonk
"""
print (*range(20,0,-1)) #20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1
print (*range(0,100,2)) #0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54

for sayi in range(0,10):
    print(sayi) # altalta 0123456789
for i in range (10):
    print(i)  # altalta 0123456789
for i in range (10):
    print("*"*i)"""
"""
*        i yi * ile çaeptık
**
***
****
*****
******
*******
********
*********
"""

#             BREAK CONTINUE
"""
i=0

while(i<10):
    if (i==5):
        break
    print(i)
    i+=1

liste = [1,2,3,4,5,6]
for i in liste:
    if (i==3):
        break
    print(i)


while True: #true yazınca sonsuz döngü
    isim = input("isim(çıkmak için q ya basin)")
    if(isim == "q"):
        print("programdan çıkılıyor...")
        break
    print("isminiz", isim)
 """
#continue yu görünce alttaki hiçbir işlemi yapma döngünün dön
"""
liste = [1,2,3,4,5,6]
for i in liste:
    if(i==3 or i==5):
        continue
    print("i:", i) # 1 2 4 6

"""
"""
i = 0
while (i<10):
    if(i==2):
        continue
    print(i)
    i+=1 #bu sonsuz döngüye girer 
"""
"""#sonsuz döngüye girmesi sorununu nasıl çözeriz?
i = 0
while (i<10):
    if(i==2):
        i+=1
        continue
    print(i)
    i+=1 #0 1 3 4 5 6 7 8 9"""

#          LIST COMPREHENSION

#bir listeden başka bir liste oluşturmak:
"""
liste1 = [1,2,3,4,5]
liste2 = list()

for i in liste1:
    liste2.append(i)
print(liste2) #[1, 2, 3, 4, 5]

#bunun kısa yolu şudur:

liste3 = [1,2,3,4,5]
liste4 = [i for i in liste3]
print(liste4) #[1, 2, 3, 4, 5]

liste = [(1,2),(3,4),(5,6),(7,8)]
liste1 = [i*j for i,j in liste]
print(liste1) #[2, 12, 30, 56]

liste = [(1,2),(3,4),(5,6),(7,8)]
liste1 = [(i,j) for i,j in liste]
print(liste1) #[(1, 2), (3, 4), (5, 6), (7, 8)]

ulke = "Izlanda"

gidilmeli = [i*3 for i in ulke]
print(gidilmeli) #['III', 'zzz', 'lll', 'aaa', 'nnn', 'ddd', 'aaa']

liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
liste1 = list()
for i in liste:
    for x in i:
        liste1.append(x)
print(liste1)
# kısa yolu
liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
liste1 = [x for i in liste for x in i]
print(liste1) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
"""
#         METODLAR/ METOTLAR

"""a = [1,2,3,4,5]

a.insert(1, "Hey") #[1, 'Hey', 2, 3, 4, 5]
a.append("python") #[1, 'Hey', 2, 3, 4, 5, 'python']
a.pop() # [1, 'Hey', 2, 3, 4, 5] // kaldırıyor sondaki elemanı
print(a)
help(a.append) #metodun ne işe yaradığını unutursan"""
"""append(object, /) method of builtins.list instance
    Append object to the end of the list."""

#       FONKSIYONLAR
"""
def selamla():
    print("merhaba")
    print("nasılsınız")
print(type(selamla))#<class 'function'>
selamla()

def selamla(isim): #parametre yolluyosun isim diye
    print("isminiz", isim)

selamla("kemal") #kemal bir arguman oluyo #isminiz kemal

def toplama(a,b,c):
    print("toplamlari", a+b+c)

toplama(3,4,5) # toplamlari 12

def faktoriyel(sayi):
    faktoriyel = 1
    if(sayi==0 or sayi == 1):
        print("faktoriyel", faktoriyel)
    else:
        while(sayi>=1):
            faktoriyel *= sayi
            sayi -= 1
        print("faktoriyel",faktoriyel)

faktoriyel(5)#faktoriyel 120"""

#       RETURN
#RETURN BİR FONKSİYONU TAAMEN SONLANDIRAN BİR İFADE
#FONKSİYONA RETURN YAZDIYSAN O FONK'UN ALTINAYAZDIĞIN HİÇBİR ŞEY ÇALIŞMAZ
"""def toplama(a,b,c):
    print("toplamlari", a+b+c)

def ikiylecarp(a):
    print("carpım", a*2)

toplam = toplama (3,4,5)
ikiylecarp(toplam) #none type hatası verir

print(type(toplam)) #noneType"""
"""
def toplama(a,b,c):
    return a+b+c

def ikiylecarp(a):
    return a*2 #dış dünyaya yani çağrıldığı yere bu değeri döndürüyo götürüpp yazıyor

toplam = toplama (3,4,5)
#return yazdığımız için artık çağrıldığı yere 12 değerini döndürüyo
# sanki artik toplama (3,4,5)  yazmıyor da 12 yazıyor
#toplam = 12 gibi
print(ikiylecarp(toplam)) #print(24) gibi çıktı = 24

def uclecarp(a):
    print("1.fonksiyon çalıştı")
    return a*3
def ikiyletopla(a):
    print("2.fonksiyon çalıştı")
    return a+2
def dordebol(a):
    print("3.fonksiyon çalıştı")
    return a/4

print(dordebol(ikiyletopla(uclecarp(16))))"""
"""
1.fonksiyon çalıştı
2.fonksiyon çalıştı
3.fonksiyon çalıştı
12.5
"""
# RETURN KULLANILMAYAN FONK'LARA VOID FONK DENİR DEĞER DONDURMUYO

#       PARAMETRE TURLERİ

"""def selamla(isim):
    print("selam",isim)

selamla("murat")

#selamla() # hata verir

def selamla(isim = "isimsiz"):
    print("selam",isim)
selamla() #selam isimsiz //hata vermedi

def bilgilerigoster(ad,soyad,numara):
    print("AD:", ad, "Soyad:", soyad, "Numara:", numara)

bilgilerigoster("murat","coskun","123")#AD: murat soyad coskun numara 123

def bilgilerigoster(ad="bilgiyok",soyad="bilgiyok",numara="bilgiyok"):
    print("AD:", ad, "Soyad:", soyad, "Numara:", numara)

bilgilerigoster()#AD: bilgiyok Soyad: bilgiyok Numara: bilgiyok
bilgilerigoster("ferda")#AD: ferda Soyad: bilgiyok Numara: bilgiyok
#esnek
def toplama(a,b,c):
    print("toplamlari", a+b+c)

toplama(3,4,5)
#toplama(3,4,5,6)

def toplama(*a):
    toplam = 0
    for i in a:
        toplam +=i
    print(toplam)
#toplama(3,4,5)#(3, 4, 5)
#toplama(3,4,5,7) #(3, 4, 5,7) tuple demet olarak tutuluyo


toplama(1,2,3)#6
toplama(1,2,3,4,5)#15

help(print) # yazıp defaultlara bakabilirsin"""

#              YEREL(local) VE GLOBAL DEGİSKENLER
"""
# if while da tanımlananlar global
#YEREL: bir fonk içinde üretilen he rbir değşkendir ve fonks çağrısı dışında erişilemez
def fonksiyon():
    a=10 #yerel
    print(a)

fonksiyon()
print(a)

b=5 #global
def fonksiyon():
    print(b)
fonksiyon()

def fonksiyon():
    print(s)
fonksiyon()
s="python" 
"""
#hata verdi globalde tanımlı ama fonk dan önce tanımlamalıydım
"""
c = 10 #global c
def fonksiyon():
    c=2 #local c
    print(c) #burda local c yi kullanır
fonksiyon() #local c kullancağından 2 bastırır
print(c) #fonk çağrısıyla işim bitti artık global c yi kullancak yani 10 basar
# programda 2 tane c var biri local biri global"""
"""
#ben 2 c kullanmak istemiyorum globaldekini kullanmak istiyorum

#             GLOBAL DEYİMİ
"""
"""d=5

def fonksiyon():
    global d
    d = 3
    print(d) #3 #global değeri 5ten 3 e değştirdik

fonksiyon()
print(d)#3"""

#          LAMBDA İDAFELERİ
#buyuk uzun fonk kullanılmıyorlar kısa fonk için derli toplu durabilir
#list compherisona benziyo
"""
def ikiylecarp(x):
    return x*2
print(ikiylecarp(3)) #6

#yukarıdakinin kısası

ikiylecarp = lambda x : x*2

def toplama(x,y,z):
    return x+y+z
print(toplama(10,11,12)) #33

toplama = lambda x,y,z : x+y+z
print(toplama(3,4,5)) #12

def terscevir(s):
    return s[::-1]

print(terscevir("python"))

ters = lambda s : s[::-1] #nohtyp
print (ters("python"))

cifttek = lambda sayi : sayi % 2==0
print(cifttek(14)) #true
"""

#   MODÜLLER
"""
import math
#print(dir(math)) içinde hangi fonksiyonların olduğunu gösteriyo
#print(help(math)) gösterdiği fonksiyonların anlamını yazıyo

print(math.factorial(6))

import math as matematik # modülün adını değşitriyo

print(matematik.factorial(4))

from math import *# at modulun içindeki tum fonks dahil ediyoruz

print(factorial(5)) # mat yazmaya gerek kalmıyo

"""
"""from math import floor, ceil

#print(factorial(5))  #fact dahil değil çalışmaz
print(ceil(6.1)) #7
"""

def factorial(Sayi):
    print("benm fonksiyonum")

    faktoriyel = 1
    if (Sayi == 0 or sayi ==1):
        return 1
    else:
        while (sayi>=1):
            faktoriyel *= sayi
            sayi -= 1
        return faktoriyel
from math import *
print(factorial(5)) # benım fonk yazmadı direk math kutup içindeki fact ı kullandı
# python son gordugu fonk u alıyor
#en son kendı fonk yazılsaydı onu çalıştırcaktı

#               MODULLER
"""
import random
import time

print("""
#sayi tahmin oyunu
""")
rastgele_sayi = random.randint(1,40) # rastgele sayi üretcek

tahmin_hakki = 7
while True:
    tahmin = int(input("tahmininiz:"))

    if(tahmin<rastgele_sayi):
        print("bilgiler soegulanıyor...")
        time.sleep(1)

        print("daha yüksek bir sayi söyleyin")

        tahmin_hakki -=1
    elif(tahmin> rastgele_sayi):
        print("bilgiler soegulanıyor...")
        time.sleep(1)

        print("daha düşük bir sayi söyleyin")

        tahmin_hakki -=1

    else:
        print("bilgiler soegulanıyor...")
        time.sleep(1)

        print("tebrikler", rastgele_sayi)
        break
    if (tahmin_hakki==0):
        print("tahmin hakkiniz bitti ")"""

#     NESNE TABANLI PROGRAMLAMA

class Araba():
    model = "renault megane"
    renk = "gümüş"
    beygir_gücü = 110
    silindir = 4
    def __init__(self): #self objeyi gösteren bir referans
        print("init fonksiyonu çağırıldı")

araba1 = Araba()
print(araba1) #<__main__.Araba object at 0x102ada650>
araba2 = Araba()
print(araba2) #<__main__.Araba object at 0x10cda4790>
print(araba1.model) #renault megane
print(araba2.model) #renault megane

class Araba():

    def __init__(self, model, renk, beygir_gucu,silindir):
        print("init fonksiyonu çağırıldı")
        self.model = model
        self.renk = renk
        self.beygir_gucu = beygir_gucu
        self.silindir = silindir

araba1 = Araba("BMW M4", "siyah", 425, 6)
araba2 = Araba("Mercedes AMG Roadster", "lacivert", 585,8)
print(araba1.model)
print(araba2.model)

class Araba():

    def __init__(self, model="Bilgi Yok", renk = "Bilgi Yok", beygir_gucu = 300,silindir = 4):
        print("init fonksiyonu çağırıldı")
        self.model = model
        self.renk = renk
        self.beygir_gucu = beygir_gucu
        self.silindir = silindir
araba = Araba(beygir_gucu = 320)
print(araba.model) #Bilgi Yok
print(araba.beygir_gucu) #320

class TV_kanallari():
    def __init__(self, ad, spiker, reyting):
        self.ad = ad
        self.spiker = spiker
        self.reyting = reyting

    def bilgileri_goster(self):
        print("""
        Program Kanalının Özellikleri
        
        Kanalın Adi : {}
        
        Ana Haber Spikerinin İsmi : {}
        
        Reytingi : {}

        """.format(self.ad,self.spiker,self.reyting))


#11 mayıs 2020 sonuçları
kanal1 = TV_kanallari("CNN", "Fulya Kalfa", 0.48)
kanal2 = TV_kanallari("Habertürk", "Buket Aydın", 0.36)
kanal3 = TV_kanallari("NTV","Seda Öğretir",0.38)

kanal_listesi=[kanal1,kanal2,kanal3]

for i in kanal_listesi:
   print(i.bilgileri_goster())

#       HERITANCE - MİRAS-KALITIM
"""
class Calisan():
    def __init__(self,isim,maas,departman):
        print("calisan sinifinin init fonksiyonu")

        self.isim =isim
        self.maas = maas
        self.departman = departman

    def bilgilerigoster(self):
        print("calisan sinifinin bilgileri...")

        print("isim: {}\nMaas: {}\nDepartman: {}\n".format(self.isim,self.maas,self.departman))

    def departman_degistir(self,yeni_departman):
        self.departman = yeni_departman

class Yonetici(Calisan):
    pass # buraya pass yazmayıp boş bırakırsan hata verir sonra yazcağın kodlar için pass yaz

yonetici = Yonetici("Ferda",10000,"bilisim") #calisan sinifinin init fonksiyonu
#yani calisan sınıfını calıstırdı inherit ettiğimiz için

print(yonetici.bilgilerigoster())
yonetici.departman_degistir("insan kaynaklari")
print((yonetici.bilgilerigoster()))

print(dir(yonetici)) #class içindeki fonkları görebiliriz

class Yonetici(Calisan):
    def zam_yap(self,zam_miktari):
        self.maas +=zam_miktari

yonetici=Yonetici("ferr",8000,"pazarlama")
yonetici.zam_yap(750)
yonetici.bilgilerigoster()
"""
#       OVERRIDING -İPTAL ETME
"""
class Yonetici(Calisan):
    def __init__(self,isim,maas,departman,kisi_sayisi):
        print("yonetici sınıfının init fonksiyonu")
        self.isim =isim
        self.maas = maas
        self.departman = departman
        self.kisi_sayisi = kisi_sayisi

    def bilgilerigoster(self):
        print("yonetici sinifinin bilgileri...")

        print("isim: {}\nMaas: {}\nDepartman: {}\nSorumlu kişi sayisi: {}".format(self.isim, self.maas, self.departman, self.kisi_sayisi))

    def zam_yap(self,zam_miktari):
        self.maas +=zam_miktari
yonetici = Yonetici("ahmet",4800,"bilisim",10)#yonetici sınıfının init fonksiyonu
yonetici.bilgilerigoster()"""

#                    SUPER ANAHTAR KELİMESİ
"""
class Calisan():
    def __init__(self,isim,maas,departman):
        print("calisan sinifinin init fonksiyonu")

        self.isim =isim
        self.maas = maas
        self.departman = departman

    def bilgilerigoster(self):
        print("calisan sinifinin bilgileri...")

        print("isim: {}\nMaas: {}\nDepartman: {}\n".format(self.isim,self.maas,self.departman))

    def departman_degistir(self,yeni_departman):
        self.departman = yeni_departman

class Yonetici(Calisan):
    def __init__(self,isim,maas,departman,kisi_sayisi):
        print("yonetici sınıfının init fonksiyonu")
        #BU 3Ü ZATEN CALIŞANDA TANIMLI BEN NEDEN BİDAHA +3 SATIR KOD YAZIM Kİ
      #  self.isim =isim
      #  self.maas = maas
      #  self.departman = departman
        super().__init__(isim,maas,departman)
        self.kisi_sayisi = kisi_sayisi

    def bilgilerigoster(self):
        print("yonetici sinifinin bilgileri...")

        print("isim: {}\nMaas: {}\nDepartman: {}\nSorumlu kişi sayisi: {}".format(self.isim, self.maas, self.departman, self.kisi_sayisi))

    def zam_yap(self,zam_miktari):
        self.maas +=zam_miktari

yonetici = Yonetici("ferd",132, "bilisim",9) #yonetici sınıfının init fonksiyonu
#                                             calisan sinifinin init fonksiyonu
yonetici.bilgilerigoster()"""

#             OZEL METODLAR
"""
class Kitap():
    pass


kitap = Kitap()#burda __init__metodu çağrılıyor

print(kitap)#burda __str__metodu çağrılıyor
#<__main__.Kitap object at 0x10aa608d0>
"""
"""
len(kitap) #__len__ metodu çağrılmak isteniyor
#TypeError: object of type 'Kitap' has no len()
"""
"""
del kitap #__del__metodu çağrılıyor
#kitabı siliyo
print(kitap#NameError: name 'kitap' is not defined
#kitabı sildiğim için eror verdi
"""
"""
class Kitap():
    def __init__(self,isim,yazar,sayfa_sayisi,tur):
        print("init fonksiyonu")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.tur = tur

kitap = Kitap("istanbul hatirası","ahmet ümit",561,"polisiye")#init fonksiyonu
#initi kendimiz tanımlamışolduk

class Kitap():
    def __init__(self,isim,yazar,sayfa_sayisi,tur):
        print("init fonksiyonu")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.tur = tur
    def __str__(self):
        return "isim: {}\nYazar:{}\nSayfa Sayisi:{}\nTürü:{}".format(self.isim,self.yazar,self.sayfa_sayisi,self.tur)

kitap = Kitap("istanbul hatirası","ahmet ümit",561,"polisiye")

print(kitap)"""
"""
init fonksiyonu
isim: istanbul hatirası
Yazar:ahmet ümit
Sayfa Sayisi:561
Türü:polisiye"""

"""
class Kitap():
    def __init__(self,isim,yazar,sayfa_sayisi,tur):
        print("init fonksiyonu")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.tur = tur
    def __str__(self):
        return "isim: {}\nYazar:{}\nSayfa Sayisi:{}\nTürü:{}".format(self.isim,self.yazar,self.sayfa_sayisi,self.tur)
    def __len__(self):
        return self.sayfa_sayisi

kitap = Kitap("istanbul hatirası","ahmet ümit",561,"polisiye")
print(len(kitap)) #561


class Kitap():
    def __init__(self,isim,yazar,sayfa_sayisi,tur):
        print("init fonksiyonu")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.tur = tur
    def __str__(self):
        return "isim: {}\nYazar:{}\nSayfa Sayisi:{}\nTürü:{}".format(self.isim,self.yazar,self.sayfa_sayisi,self.tur)
    def __len__(self):
        return self.sayfa_sayisi
    def __del__(self):
        print("kitap objesi siliniyor....")

kitap = Kitap("istanbul hatirası","ahmet ümit",561,"polisiye")
del(kitap) #kitap objesi siliniyor....

"""

#         TV KUMANDASI
"""
import random
import time

class Kumanda():
    def __init__(self, tv_durum = "Kapali", tv_ses=0, kanal_listesi = ["trt"], kanal = "trt"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi= kanal_listesi
        self.kanal = kanal

    def tv_ac (self):
        if(self.tv_durum == "açık"):
            print("televizyon zaten açık")

        else:
            print("tv açılıyor...")
            self.tv_durum = "açık"

    def tv_kapat (self):
        if(self.tv_durum == "kapalı"):
            print("zaten kapalı")

        else:
            print("televizyon kapanıyor...")

    def ses_ayarlari(self):

        while True:
            cevap= input("sesi azalt: '<'\nSesi Arttır: '>'\nÇıkış: çıkış")

            if (cevap== "<"):
                if (self.tv_ses != 0):

                    self.tv_ses -= 1
                    print("ses:", self.tv_ses)
            elif (cevap== '>'):
                if (tv_ses != 31):
                    self.tv_ses +=1
                    print("ses:", self.tv_ses)

            else:
                print("ses guncellendi:",self.tv_ses)
                break

    def kanal_ekle(self,kanal_ismi):
        print ("kanal ekleniyor...")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("kanal eklendi...")

    def rastgele_kanal(self):
        rastgele = random.randint(0, len(self.kanal_listesi)-1)

        self.kanal = self.kanal_listesi[rastgele]

        print("şu anki kanal:", self.kanal)


    def __len__(self):

        return len(self.kanal_listesi)

    def __str__(self):

        return "Tv durumu: {}\nTv ses: {}\nKanal listesi: {}\nŞuanki kanal: {}\n".format(self.tv_durum,self.tv_ses, self.kanal_listesi,self.kanal)

kumanda = Kumanda()

print (TV UYGULAMASI
    
    1.Tv aç
    
    2.Tv kapat
    
    3.Ses ayarları
    
    4.Kanal ekle
    
    5.Kanal sayısını öğrenme
    
    6.Rastgele kanala geçme
    
    7.Tv bilgileri
    
    Çıkmak için 'q'ya basın
       )
while True:

    islem = input("işlemi seçiniz:")

    if(islem =="q"):
        print("program sonlandırılıyor...")
        break

    elif(islem=="1"):
        kumanda.tv_ac()

    elif(islem=="2"):
        kumanda.tv_kapat()

    elif(islem=="3"):
        kumanda.ses_ayarlari()

    elif(islem=="4"):
        kanal_isimleri = input("kanal isimlerini ',' ile ayırarak girin:")
        kanal_listesi = kanal_isimleri.split(",")

        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)

    elif (islem == "5"):

        print("kanal sayisi:", len(kumanda))

    elif (islem == "6"):
        kumanda.rastgele_kanal()

    elif (islem == "7"):
        print(kumanda)

    else:
        print("geçersiz işlem")"""


#      HATALAR VE İSTİSNA

# a = int("fgyudsjıs")
#ValueError: invalid literal for int() with base 10: 'fgyudsjıs'

#hatayı nasıl gideririz
"""
try:
    a= int("hdejkwl1234")
    print("prg burada")

except:
    print("bir hata oluştu")
print("bloklar sona erdi")
#bir hata oluştu
#bloklar sona erdi
#try a girdi hata aınca mecbur excepte gircek
#hata vermese excepte girmez

try:
    a= int("hdejkwl1234")
    print("prg burada")

except ValueError:
    print("bir hata oluştu")
print("bloklar sona erdi")
#bir hata oluştu
#bloklar sona erdi

try:
    a = int(input("sayi1:"))
    b = int(input("sayi2:"))
    print(a/b)
except ValueError:
    print("lütfen doğru inputu girin")
except ZeroDivisionError:
    print("bir sayi 0 a bölünemez")
print("bloklar sona erdi")


try:
    a = int(input("sayi1:"))
    b = int(input("sayi2:"))
    print(a/b)
except (ValueError,ZeroDivisionError):
    print("value or zero eror")
print("bloklar sona erdi")


try:
    a = int(input("sayi1:"))
    b = int(input("sayi2:"))
    print(a/b)
except ValueError:
    print("lütfen doğru inputu girin")
except ZeroDivisionError:
    print("bir sayi 0 a bölünemez")
finally:
    print("burası çalıştı") #KESİN ÇALIŞIR BURASI
print("bloklar sona erdi")
"""
# HATA FIRLATMAK
"""
def terscevir(s):
    if(type(s)!= str):
        raise ValueError("lutfen string bir deger girin")
    else:
        return s[::-1]

print (terscevir("python"))
print(terscevir(12)) #ValueError: lutfen string bir deger girin"""

"""

def terscevir(s):
    if(type(s)!= str):
        raise ValueError("lutfen string bir deger girin")
    else:
        return s[::-1]

try:
    print(terscevir(12))
except ValueError:
    print("fonksiyon hata verdi")"""

#      DOSYA AÇMA VE YAZMA İŞLEMLERİ

# w kipi = yazma kipi

print(open("bilgiler.txt","w"))
#<_io.TextIOWrapper name='bilgiler.txt' mode='w' encoding='UTF-8'> şeklinde bir dosya ofisi geldi
#açmak istediğimiz dosya kipi w
#bilgiler txt adlı bir dosya oluşturdum ve bunu yazdım
file = open("bilgiler.txt","w")
#dosyayla işimiz bitince kapatmamız gerekir
file.close() #kapatır
file = open("/Users/ferdaozturk/Desktop/bilgiler.txt","w")
file = open("bilgiler.txt","w", encoding ="utf-8")
# encoding utf 8 dosyya ferda öztürk yazınca türkçe karakter var diye kabul etmiyodu
#bu encodingle onu ayarlamış olduk
print(file.write("ferda öztürk")) #12 yani 12 baytlık yer kapplar 11 harf var + space
#türkçe karakter kabul ediyo artık
file.close()

file = open("bilgiler.txt","w", encoding ="utf-8")
#dosyayı bidaha açtık
file.close()
#dosyayı kapattık
#şimdi noldu
#dosyadaki tüm bilgiler silindi
# w kipi dosyada bi şey varsa onları silip yeniden yazıyo
#w kipi kullancaksan dosyan aslında yok oluyo

# PEKİ BİZ BULUNAN BİR DOSYAYA SÜREKLİ YAZMA İŞLEMİ YAPMAK İSTİYORSAK HANGİ KİPİ KULLANCAZ
#yani dosyaya sürekli yazmak istiyoruz

"""#   a KİPİ (APPEND)
# a kipi dosya yksa oluşturur varsa da yazmaya devam ettirir
file = open("bilgiler.txt","a", encoding ="utf-8")
file.write("Ferda Öztürk")
file.close()
#hala ferda öztğrk yazıyo dosyada silinmeid sadece ekleme yaptık
file = open("bilgiler.txt","a", encoding ="utf-8")
file.write("fre")
file.close() #Ferda Öztürkfre yazdı dosyada
file = open("bilgiler.txt","a",encoding="utf-8")
file.write("mamates") #Ferda Öztürkfremamates
#bunları alttalta yazdırmak istiyorum

file.close()
file = open("bilgiler.txt","a",encoding="utf-8")
file.write("Ferda Öztürk\n")
file.close()
file = open ("bilgiler.txt","a",encoding="utf-8")
file.write("Fre\n")
file.close()"""

#     R KİPİ read
#read dosyaya yazdığımız şeyleri okumaya yarıyor
#okuyup buraya bastırabiliyoruz


"""
file = open("bilgiler2.txt","r")

#file değilkeni dosya üzerinde gezinebilen bir imleç görevi görüyor

file.close() #FileNotFoundError: [Errno 2] No such file or directory: 'bilgiler2.txt'

ozaman try exceptle hatayı yakalayalım

"""
"""
try:
    file = open("bilgiler2.txt", "r")
except FileNotFoundError:
    print("Dosya bulunamadi...")

file = open("bilgiler.txt","r", encoding="utf-8")
#for döngüsüyle dosya okumak
for i in file:
    print(i, end = "")#print(i)yazında print sonuna\n koyuyo biz de dosya işlemi sırası koyduruştuk
#iki tane satır atlıyor bunu engellemek için sonuna  koymama işlemi yaptırdık

#Ferda ÖztürkfremamatesFerda Öztürk
#Fre

file.close()

#read() fonksiyonu
file = open("bilgiler.txt","r", encoding="utf-8")
icerik = file.read()
print("dosyanın içeriği: ")
print(icerik)
#dosyanın içeriği:
#Ferda ÖztürkfremamatesFerda Öztürk
#Fre

file = open("bilgiler.txt","r", encoding="utf-8")
icerik = file.read()
print("dosyanın içeriği: ")
print(icerik)
print("dosyanın içeriği 2: ")
icerik2 = file.read()
print(icerik2)
#dosyanın içeriği:
#Ferda ÖztürkfremamatesFerda Öztürk
#Fre

#dosyanın içeriği 2:
#içerik 2 boş çünkü içerik 1 i okuu dosyanın sonuna gitti file imleç görevi gördüğünden
#o yuzden bi şey yazmıyo

#          redaline() fonksiyionu
#dosyanın sadece bir satırını okur

file = open("bilgiler.txt","r",encoding="utf-8")

print(file.readline())
file.close()#Ferda ÖztürkfremamatesFerda Öztürk

file = open("bilgiler.txt","r",encoding="utf-8")

print(file.readline())#Ferda ÖztürkfremamatesFerda Öztürk
print(file.readline())#Fre
print(file.readline())#
file.close()

#          redalines() fonksiyionu

file = open("bilgiler.txt","r",encoding="utf-8")

liste = file.readlines()
print(liste)
file.close()#['Ferda ÖztürkfremamatesFerda Öztürk\n', 'Fre\n']


#    dosyaları otomatik kapatma

with open("bilgiler.txt","r",encoding="utf-8") as file:
    for i in file:
        print(i)


# dosyalardaki metodlar

#     DOSYALARI İLERİ GERİ SARMAK
#imleci istediğimiz yere götürebiliriz

#seek() fonksiyyonu ile imleci istediğimiz yere götürebiliriz
#tell() fonksiyonu imlecin hangi byteta olduğunu söylüyor

with open("bilgiler.txt","r",encoding="utf-8") as file:
    print(file.tell())#0 (hiçbi işlem yapmadığımız için 0.byteta yani soyanın en başında
with open("bilgiler.txt","r",encoding="utf-8") as file:
    print(file.tell())#0
    file.seek(20) #file değişkeniin yeri 20.byte'a gidiyor
    print(file.tell()) #20

#dosyanın 5.byteına gidip 10 karakterlik yer okumak istiyorum
with open("bilgiler.txt","r",encoding="utf-8") as file:
    file.seek(5) #5.bytetan başla
    icerik = file.read(10) #10luk yer oku
    print(icerik)# Öztürkfre


with open("bilgiler.txt","r",encoding="utf-8") as file:
    file.seek(5) #5.bytetan başla
    icerik = file.read(10) #10luk yer oku
    file.seek(0)#dosyanın en başına dön
    print(icerik)# Öztürkfre

#       DOSYALARDA DEĞİŞİKLİK YAPMAK

# r+ DOSYA KİPİ write+read

with open("bilgiler.txt","r+",encoding="utf-8") as file:
    file.seek(14)
    file.write("Servet Öztürk\n")
with open("bilgiler.txt", "r+", encoding="utf-8") as file:
    print(file.read())#Ferda ÖztürkfremDenemeFerda Öztürk
#Fre

#dosyanın sonunda değişiklik yapmak
with open("bilgiler.txt", "a", encoding="utf-8") as file:
    file.write("Esra Öztürk\n")
with open("bilgiler.txt", "a", encoding="utf-8") as file:
    file.write("Reyyan Öztürk\n")
with open("bilgiler.txt", "r+", encoding="utf-8") as file:
    print(file.read())

#başa bir satır eklemek
with open("bilgiler.txt", "r+", encoding="utf-8") as file:
    print(file.read())
with open("bilgiler.txt", "r+", encoding="utf-8") as file:
    icerik = file.read()
    icerik = "İdris Öztürk\n" + icerik
    print(icerik )
    file.seek(0)#dosyada ilk karaktere gitti
    file.write(icerik)#ve dosyaya yazdı
#dosyaya tekrar bi bakalım
with open("bilgiler.txt", "r+", encoding="utf-8") as file:
    print(file.read())

#dosyanın ortasında değişiklik yapmak
#readlines her bir satırı bir liste halinde bize veriyordu
with open("bilgiler.txt", "r+", encoding="utf-8") as file:
    liste = file.readlines()
#   print(liste)#['İdris Öztürk\n', 'Ferda ÖztürkServet Öztürk\n', 'Öztürk\n', 'Fre\n', 'Esra Öztürk\n', 'Reyyan Öztürk\n']
#frenin üstüne bi şey eklicem
#insert methoduunu kullanabilirim
    liste.insert(3, "İbrahim Tayyip İşler\n")
#    print(liste)
#['İdris Öztürk\n', 'Ferda ÖztürkServet Öztürk\n', 'Öztürk\n', 'İbrahim Tayyip İşler\n', 'Fre\n', 'Esra Öztürk\n', 'Reyyan Öztürk\n']
    file.seek(0)
    for i in liste:
        file.write(i)
with open("bilgiler.txt", "r+", encoding="utf-8") as file:
    print(file.read())
#İdris Öztürk
#Ferda ÖztürkServet Öztürk
#Öztürk
#İbrahim Tayyip İşler
#Fre
#Esra Öztürk
#Reyyan Öztürk

with open("bilgiler.txt", "r+", encoding="utf-8") as file:
    liste = file.readlines()
    liste.insert(3,"Elif Serra Yıldırım\n")
    file.seek(0)
    file.writelines(liste) #forlu döngü yerine bununla da yazabiliriz
with open("bilgiler.txt", "r+", encoding="utf-8") as file:
    print(file.read())"""
#İdris Öztürk
#Ferda ÖztürkServet Öztürk
#Öztürk
#Elif Serra Yıldırım
#İbrahim Tayyip İşler
#Fre
#Esra Öztürk
#Reyyan Öztürk

#           GÖMÜLÜ FONKSİYONLAR

#MAP FONKSİYONU
#2 parametre alıyor ilki fonksiyon objesi ikincisi,
#ikincisi fonksiyonu her bir eleman üzerinde uygulayacak elemanlar


def double(x):
    return x*2

map(double,[1,2,3,4,5])

list(map(double,[1,2,3,4,5]))
print(list(map(double,[1,2,3,4,5]))) #[2, 4, 6, 8, 10]

#fonksiyonu lambdayla da tanımlayabiliriz
print(list(map(lambda x: x**2,(1,2,3,4,5,6))))#[1, 4, 9, 16, 25, 36]

liste1 = [1,2,3,4]
liste2 = [5,6,7,8]
liste3 = [9,10,11,12,13]

print(list(map(lambda x,y,z : x*y*z,liste1,liste2,liste3)))#[45, 120, 231, 384]

#REDUCE FONKSİYONU
#Reduce(function,iterasyn yapılabilen veritipi(liste vb.)
#fonksiyonu listenin ilk2 elemanına uygular sonra çıkan sonucu 3.elemana uygular liste bitince bir tane değğer döner

from functools import reduce
def toplama(x,y):
    return x+y
print(reduce(toplama,[12,18,20,10]))#60
#12+18 =30
#30+20=50
#50+10=60

print(reduce(lambda x,y :x*y,[1,2,3,4])) #24 4ün faktoriyelini bulduk

def maksimum(x,y):
    if (x>y):
        return x
    else:
        return y
print(reduce(maksimum,[-2,3,1,4])) #4


#FILTER FONKSİYONU
#filter(fonksiyon,iterasyon yapılabilecek veritipi(liste vb.))
#fonksiyon objesi MUTLAKA true ya da false dönmeli

filter(lambda x: x%2 == 0, [1,2,3,4,5,6,7,8])
print(list(filter(lambda x: x%2==0, [1,2,3,4,5,6,7,8])))#[2, 4, 6, 8]

def asal_mi(x):
    i=2

    if(x==1):
        return False
    elif (x==2):
        return True
    else:
        while(i<x):
            if(x%i == 0):
                return False
            i += 1
        return True

print(list(filter(asal_mi,range(1,100))))
#[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

#ZİP FONKSİYONU
liste1 = [1,2,3,4,5]
liste2 = [6,7,8,9,10,11]
#sonucu[(1,6),(2,7),(3,8),(4,9),(5,10)] yapmaya çalışalım

i=0

sonuc = list()
while(i < len(liste1) and i < len(liste2)):
    sonuc.append((liste1[i],liste2[i]))
    i+=1
print(sonuc)
#[(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]

#zip bunu yapıyor
print(list(zip(liste1,liste2)))
#[(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]

liste1 = [1,2,3,4,5]
liste2 = [6,7,8,9,10,11]
liste3 = ["python","java","php"]

print(list(zip(liste1,liste2,liste3)))
#[(1, 6, 'python'), (2, 7, 'java'), (3, 8, 'php')]

#aynı anda iki liste üzerinde gezinmek için çok yararlı bşr fonk

liste1 = [6,7,8,9,10,11]
liste2 = ["python","java","php"]

for i,j in zip (liste1,liste2):
    print(i,j)
#6 python
#7 java
#8 php

sozluk1 = {"elma":1, "armut":2, "kiraz":3}
sozluk2 = {"sifir":0,"bir":1,"iki":2}
print(list(zip(sozluk1,sozluk2))) #[('elma', 'sifir'), ('armut', 'bir'), ('kiraz', 'iki')]

#ENUMERATE FONKSİYONU
#herbir elemanı indeksleyerek numara verir

liste = ["elma","armut","muz","kiraz"]

i = 0
sonuc = list()
while (i<len(liste)):
    sonuc.append((i,liste[i]))
    i+=1
print(sonuc) #[(0, 'elma'), (1, 'armut'), (2, 'muz'), (3, 'kiraz')]

print(list(enumerate(liste))) #[(0, 'elma'), (1, 'armut'), (2, 'muz'), (3, 'kiraz')]

for i,j in enumerate(liste):
    print(i,j)
#0 elma
#1 armut
#2 muz
#3 kiraz

liste = ["a","b","c","d","e","f","g"]
for i,j in enumerate(liste):
    if(i%2 ==0):#indeks no çift olanları bastırcam
        print(j) # a,c,e,g


#ALL ve ANY FONKSİYONLARI

def hepsi(liste):
    for i in liste:
        if not i:
            return False
    return True
liste = [True,False,True,False,True]

print(hepsi(liste))#listemde iki tan efalse var o zama değer false çıkmalı
#False

liste=[1,2,3,4,5] #bunların hepsi true demek
print(hepsi(liste)) #true

def herhangi(liste):
    for i in liste:
        if i:
            return True
    return False
print(herhangi([True,False,True,False,True]))#true
liste=[0,0,0,0,0,0]
print(herhangi(liste))#false

#all() bütün değerler true ise true en az bi false varsa false değer döndürür

liste = [True,False,True,False,True]
print(all([True,True,True])) #true

#any() bütün değerler false ise false en az bi true varsa true varsa değer döndürür

print(any([True,False,True,False,True])) #true
print(any([False,False,False])) #False

#         İLERİ SEVİYE KÜMELER VE KÜME METODLARI (SETS)

x = {1,2,3}
print(type(x)) #set

x = set() #boş küme tanımlamak

liste = [1,2,3,3,1,1,2,2,2]
x = set(liste)
print (x) #{1, 2, 3}
x = set("python Programlama dili")
print(x)
#{'r', ' ', 'm', 'y', 'g', 'd', 'l', 'o', 'n', 'a', 'i', 't', 'p', 'h', 'P'}

x = {"Python", "php","Python"}
print(x) #{'php', 'Python'}

italya = {"Siena", "Portofino", "Lecce", "Floransa","Palermo","Pisa"}

for i in italya:
    print(i) #Pisa Siena Lecce Palermo Portofino Floransa
#print(italya{0}) böyle ulaşamayız küme elemanlarına
#nasıl ulaşcaz? listeye atayabiliriz
liste = list(italya)
print(liste) #['Portofino', 'Siena', 'Floransa', 'Palermo', 'Lecce', 'Pisa']

#kümelerin metodları

#add() metodu

x = {1,2,3}
x.add(4)
print(x) #{1, 2, 3, 4}

#difference() metodu
#kume 1de olan kume 2 de olmayan A fark B
kume1 = {1,2,3,10,34,100,-2}
kume2 = {1,2,23,34,-1}

print(kume1.difference(kume2)) #{10, 3, 100, -2}

#kume 1 in kume ikiden farkı neymiş öğrendik onları kume 1 e tekrar atamak için difference update kullanıyoruz
kume1.difference_update(kume2)
print(kume1) #{3, 100, 10, -2}

#kumeden eleman çıkartmak için
#discard() metodu

x = {1,2,3,4,5,6}
x.discard(2)
print(x) #{1, 3, 4, 5, 6}

#kğmelerin kesişimleri için
#intersection ()

kume1 = {1,2,3,10,34,100,-2}
kume2 = {1,2,23,34,-1}

print(kume1.intersection(kume2)) #{1, 2, 34}

#kume kesişimleri guncelleme işlemi
kume1.intersection_update(kume2)
print(kume1) #{1, 2, 34}

#kumeler ayrık kume mi ?
#isdisjoint() metodu
#kesişim kumem boşsa True, doluysa False döner
kume1 = {1,2,3,10,34,100,-2}
kume2 = {1,2,23,34,-1}
kume3 = {30,40,50}

print(kume1.isdisjoint(kume2)) #False

#alt kümesi mi?
#ssubset() metodu
#alt kumeyse true
kume1 = {1,2,3}
kume2 = {1,2,3,4}
kume3 = {30,40,50}
print(kume1.issubset(kume2)) #true

#union metodu
#birleşim kumesi
kume1 = {1,2,3,10,34,100,-2}
kume2 = {1,2,23,34,-1}
kume1.union(kume2)
#update metodu
kume1.update(kume2)
print(kume1) #{1, 2, 3, 34, 100, 10, -1, 23, -2}

#ileri seviye listeler ve listelerin metodları
#bir listeden başka bir listeye eleman aktarmak
liste1 = [1,2,3,4,5]
liste2 = [4,5,6,3,9]
liste1.extend(liste2)
print(liste1) #[1, 2, 3, 4, 5, 4, 5, 6, 3, 9]

#insert
#listenin herhangi bi yerine eklemek
liste = [1,2,3,4,5]
liste.insert(2,"java")
print(liste)#[1, 2, 'java', 3, 4, 5]

liste = [1,2,3,4,5]
liste.pop(2) #2.indexi atıyo
liste.pop() #sondaki elemanı atıyo
liste =["java","php","python"]
liste.remove("python")
#poptan farkı indexi yazmıyoruz elemanın ismini yazıyoruz
#index()
#3 ilk olarak kaçıncı indexte görülür onu söylüyo
liste = [1,3,4,4,5,2,3,5,3,3]
print(liste.index(3)) #1
#ama 6 ve 8.indexlerde de var o zaman onlardan başlayarak ara diyebiliriz biz
print(liste.index(3,3)) #3.indexten başlayarak 3 ü ara diyoruz

#count()
liste = [1,3,4,4,5,2,3,5,3,3]
print(liste.count(3)) #4

#sort()
liste = [1,-3,4,4,5,2,3,5,3,3]
liste.sort()
print(liste)
#[-3, 1, 2, 3, 3, 3, 4, 4, 5, 5]
liste.sort(reverse = True)
print(liste) #[5, 5, 4, 4, 3, 3, 3, 2, 1, -3]

"""Kütüphane Projesi"""
"""
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

        self.cursor.execute(sorgu,(kitaplar.isim, kitap.yazar,kitap,yayinevi,kitap.tur,kitap.baski))
        self.baglanti.commit() #bunu yapmazsak veritabanına bağlantımız gitmicektir yani güncellenmicek

    def kitap_sil(self,isim):

        sorgu= "Delete From Kitaplar where isim = ?"

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
"""
#Decoratorlar ve İç içe fonksiyonlar
"""import time

def zaman_hesapla(func):
    def wrapper (sayilar): #decorator olabilrmesi için wrapper ı eklememiz gerekli
        baslama =time.time() #zaman hesaplama işlemlerimizi bu kısımda yapıyoruz
        sonuc = func(sayilar)
        bitis = time.time()
        print(func.__name__ + " " + str(bitis - baslama) + "saniye sürdü.") #böyle dediğimde fonksiyonun ismin, bize veriyor
        return sonuc
    return wrapper


@zaman_hesapla #decorate etmek istediğim fonksiyonumun üstüne @zaman_hesapla yazıyorum
def kareleri_hesapla(sayilar):
    sonuc = []

    for i in sayilar:
        sonuc.append(i ** 2)
    return sonuc

@zaman_hesapla
def kupleri_hesapla(sayilar):
    sonuc = []

    for i in sayilar:
        sonuc.append(i ** 3)

    return sonuc
print(kareleri_hesapla(range(100000)))
print(kupleri_hesapla(range(100000)))
"""
#decorator fonksiyon örneği

"""def ekstra(fonk):

    def wrapper(sayilar):
        cift_toplami = 0
        cift_sayilar = 0
        tek_toplami = 0
        tek_sayilar = 0

        for sayi in sayilar:
            if(sayi % 2 == 0):
                cift_toplami += sayi
                cift_sayilar += 1
            else:
                tek_toplami += sayi
                tek_sayilar += 1
        print("Teklerin Ortalamasi:",tek_toplami / tek_sayilar)
        print("Çiftlerin Ortalamasi:", cift_toplami / cift_sayilar)

        fonk(sayilar)
    return wrapper

@ekstra
def ortalamabul(sayilar):
    toplam=0
    for i in sayilar:
        toplam+=i
    print ("genel ortalama:",toplam/len(sayilar))

ortalamabul([1,2,3,4,34,60,63,32,100,105])

#iteratorlar
liste = [1,2,3,4,5]

iterator = iter(liste)
print(iterator) #<list_iterator object at 0x10e727590>
print(next(iterator)) #1
print(next(iterator) )#2
print(next(iterator)) #3
print(next(iterator)) #4
print(next(iterator)) #5

for i in liste:
    print(i)

#bu for döngüsü aslında şu işlemi yapıyor:

iterator =iter(liste)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
class Kumanda():
    def __init__(self,kanal_listesi):
        self.kanal_listesi= kanal_listesi
        self.index = -1
    def __iter__(self):
        return self #self beni objemi ifade ediyo return self demek beni objemi iterator a atamak demek
    def __next__(self):
        self.index += 1
        if self.index <= len(self.kanal_listesi):
            return self.kanal_listesi[self.index]
        else:
            self.index = -1
            raise StopIteration

kumanda = Kumanda(["atv","trt","fox","kanald","bloomberg"]) #kumanada sınıfından bir tane obje oluşturup içine veri göndercem

iterator = iter(kumanda)
print(next(iterator)) #atv
print(next(iterator)) #trt
print(next(iterator)) #fox
print(next(iterator)) #kanald
print(next(iterator)) #bloomberg
"""
#                    Generators

#iterable objeleri oluşturmka için kullanılan objelerdir
#bellekte herhangi bir yer kaplamıyorlar
#yani fonksiyonları generatorla yazarsan bellekte yer kaplamak çok kullanışlı

"""def kareleri_al():
    sonuc = []

    for i in range(1,6):
        sonuc.append(i**2)
    return sonuc
print(kareleri_al()) """#[1, 4, 9, 16, 25] 5 saı bellekte saklandı
#range arta bellekte çok yer kaplancak
#generatorlarla yazalım o zaman

#generator version
"""
def kareleri_al():
    for i in range(1,6):
        yield i**2 #burada değerler henüz üreetilmedi
#bu değerler sadece biz onlara erişmek istediğimizde üretilecek
generator = kareleri_al()
print(generator) #<generator object kareleri_al at 0x109530650>

#şimdi değerlerimize erişmek isiyoruz
iterator = iter(generator)
print(next(iterator)) #1 generatorın bir sonraki değerine erişmek istiyoruz yani ilk değeri istiyoruz
print(next(iterator)) #4 bunu yazınca 1 tarihe karıştı
print(next(iterator)) #9 burdada 4 tarihe karıştı yani bi yerde deplanmıyor
print(next(iterator))
print(next(iterator))
iterator2 = iter(generator)
print(next(iterator2)) #stop iteration hatası çünkü değerleri ürettik yeni iterasyoniçin yeni bir generator gerekil

#peki ben bir tane listcompherisonıı generatora nasıl çevirebilirim

liste = [i*3 for i in range(5)]

print(liste)

generator = (i*3 for i in range (5))

print(generator)
iterator = iter(generator)
print(next(iterator))
"""
#carpım tablosu örneği

def carpimtablosu():
    for i in range(1,11):
        for j in range (1,11):
            yield("{}x{}={}".format(i,j,i*j))
for i in carpimtablosu():
    print(i)

# Fibonacci Örneği iterator ile

class Kuvvet3():
    def __init__(self,max = 0 ):
        self.max = max
        self.kuvvet=0
    def __iter__(self):
        return self
    def __next__(self):
        if (self.kuvvet <= self.max):
            sonuc = 3 ** self.kuvvet
            self.kuvvet += 1

            return sonuc
        else:
            self.kuvvet = 0
            raise StopIteration

kuvvet = Kuvvet3(6)
"""
iterator = iter(kuvvet)
print(next(iterator)) #1
print(next(iterator)) #3
print(next(iterator)) #9"""

for i in kuvvet:
    print(i) #1 3 9 27 81 243 729
for j in kuvvet:
    print(j) #1 3 9 27 81 243 729


#Fibonacci Örneği generator ile
"""
def fibonacci():
    a=1
    b=1
    yield a
    yield b

    while True:
        a,b = b,a+b
        yield b

for sayi in fibonacci():
    if(sayi>1000):
        break
    print(sayi)

class kareler():
    def __init__(self,max = 0):
        self.max = max
    def __iter__(self):
        return self
    def __next__(self):
        if (self)




class Kuvvet3():
    def __init__(self, max=0):
        self.max = max
        self.kuvvet = 0

    def __iter__(self):
        return self

    def __next__(self):
        if (self.kuvvet <= self.max):
            sonuc = 3 ** self.kuvvet
            self.kuvvet += 1

            return sonuc
        else:
            self.kuvvet = 0
            raise StopIteration

kuvvet = Kuvvet3(6)"""

# DATATIME MODULÜ
#tarih işlemlerini yapmamı sağlıyor

"""
from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL,"")


print(datetime.now()) #datetime ın içindeki now fonksiyonunu kullanabilirim
#2020-07-01 17:30:43.481774
#şuanki zamanı almış olduk

#bu fonksityonu birtane objeye atamak istersem?

su_an = datetime.now()


print(su_an.year) #2020
print(su_an.month) #7
print(su_an.hour) #17

print(datetime.ctime(su_an)) #Wed Jul  1 17:34:07 2020
print(datetime.strftime(su_an,"%Y")) #2020
print(datetime.strftime(su_an,"%B")) #July AY
print(datetime.strftime(su_an,"%D")) #07/01/20
print(datetime.strftime(su_an,"%B %Y")) #July 2020

#internette b d y  gibi şeyler çok araşrıe
print(datetime.strftime(su_an,"%B %Y %A")) #July 2020 Wednesday

#türkçe yapmak içim import locale  setlocale yaz

saniye = datetime.timestamp(su_an)
print(saniye) #1593614383.002984 şu anki zamanın saniye cinsinden değeri

su_an2 = datetime.fromtimestamp(saniye) #saniyeyi datetime a çevirir
#2020-07-01 17:40:46.057177
print(su_an2)

su_an = datetime.fromtimestamp(0)
print(su_an) #1970-01-01 02:00:00
#1970 epoch time 1970 milatmiş bilgisayarcılar kabul etmiş
#ARAŞTIRR

#belli iki tane tarihin farkını bulmak

tarih = datetime(2019,12,1)
su_an = datetime.now()

print(su_an-tarih) #213 days, 17:44:47.406355
"""
"""
import os
os.chdir("/Users/ferdaozturk/Desktop")
#print(os.getcwd())
for i in os.listdir():
    print(i) #masaustumde bulunan şeyleri listeliyo

"""

import os
from datetime import datetime
print(os.getcwd())

print(os.stat("bilgiler.txt")) #os.stat_result(st_mode=33188, st_ino=17241685, st_dev=16777220, st_nlink=1, st_uid=501, st_gid=20, st_size=0, st_atime=1590274635, st_mtime=1593619804, st_ctime=1593619804)
#burdaki stm time dosyanın değiştirilme zamanı

print(datetime.fromtimestamp(os.stat("bilgiler.txt").st_mtime)) #2020-07-01 19:12:06.087036


#os.mkdir("Deneme1") #pycharmda klasör oluşturuyo pycharmda

#os.mkdir("Deneme2/Deneme3")

#bu yukardaki hata verir çünkü henüz deneme 2 oluşadığından altına deneme 3 ü yerleştiremiyr
#ama bu işlevi gören bir fonksiyonumuz var
#os.makedirs("Deneme2/Deneme3")#/Users/ferdaozturk/PycharmProjects/udemy

#deneme 3 ü silmek istiyorum
#os.rmdir("Deneme2/Deneme3") #denem3 ü sildi

#os.mkdir("Deneme2/Deneme3")

#os.rmdir("Deneme1")
#os.removedirs("Deneme2/Deneme3") #deneme 2 ve deneme 3 ü sildi
"""
for klasor_yolu, klasor_isimleri,dosya_isimleri in os.walk("/Users/ferdaozturk/Desktop"):

    for i in dosya_isimleri:
        print(i)
"""
"""#peki sadece txt dosyalarını almka istersem naparım?
for klasor_yolu, klasor_isimleri,dosya_isimleri in os.walk("/Users/ferdaozturk/Desktop"):
    for i in dosya_isimleri:
        if (i.endswith(".txt")):
            print(i)"""


for klasor_yolu, klasor_isimleri,dosya_isimleri in os.walk("/Users/ferdaozturk/Desktop"):

    print("Klasor Yolu", klasor_yolu)
    print("Klasor isimler", klasor_isimleri)
    print("Dosya isimleri", dosya_isimleri)
    print("************************************")

# sys MODÜLÜ

"""import sys

print(dir(sys))

a = int (input("a:"))
a = int (input("b:"))

sys.exit() #bunu yazınca altında yazan hiçbir kod çalışmaz

c = int(input("c:"))

#stderr ve stdout nedir?
#bunlar dosyalardır
#stdin: kullanıcıdan input almasını sağlar
#stdout: işlemimizin çıktı vermsisni sağlar
#stderr: işlemşmşzşn hata mesajını çıktı olarka vermek için kullanılır

#aslında print yazınca stdout dosyası kullanılıyor
#input yazınca da stdin dosyası kullanılıyor
"""
"""import sys
sys.stderr.write("bu bir hata mesajıdır\n")

sys.stderr.flush()#aslında bunu yazmasak da yazar mesajımızı ama büyük dosyalarda anında buffera yazdırdığımızı görmek için bunu kullanırız
#flush bufferı direk boşaltıyor ve bunu ekrana yazdırmış oluyoruz
#bu bir hata mesajıdır dedi kırmızı bir şekilde

sys.stdout.write("bu normal bir yazıdır\n")
#bu normal bir yazıdır kırmızı yazmadı

print(sys.argv) #['/Users/ferdaozturk/PycharmProjects/udemy/ude.py']
#dosyanın pcdeki pathi
"""






























