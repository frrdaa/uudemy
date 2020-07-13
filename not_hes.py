def not_hesapla(satir):


    satir = satir[:-1]#fazladan olan\n i kaldırıyor

    liste = satir.split(",") #['Süleyman Koçyiğit','100','10','60']

    isim = liste[0] #listenin 0.elemanı isim

    not1 = int(liste[1])

    not2 = int(liste[2])

    not3 = int(liste[3])

    son_not = not1 * (3/10) + not2 * (3/10) + not3 * (4/10)

    if (son_not >= 90):
        harf = "AA"
    elif (son_not >= 85):
        harf = "BA"
    elif (son_not >= 80):
        harf = "BB"
    elif (son_not >= 75):
        harf = "CB"
    elif (son_not >= 70):
        harf = "CC"
    elif (son_not >= 65):
        harf = "DC"
    elif (son_not >= 60):
        harf = "DD"
    elif (son_not >= 55):
        harf = "FD"
    else:
        harf = "FF"

    return isim + "------------------> " + harf + "\n"

def kalanlar(satir):

    satir = satir[:-1]#fazladan olan\n i kaldırıyor

    liste = satir.split(",") #['Süleyman Koçyiğit','100','10','60']

    isim = liste[0] #listenin 0.elemanı isim

    not1 = int(liste[1])

    not2 = int(liste[2])

    not3 = int(liste[3])

    son_not = not1 * (3/10) + not2 * (3/10) + not3 * (4/10)

    if (son_not >= 90):
        harf = "AA"
    elif (son_not >= 85):
        harf = "BA"
    elif (son_not >= 80):
        harf = "BB"
    elif (son_not >= 75):
        harf = "CB"
    elif (son_not >= 70):
        harf = "CC"
    elif (son_not >= 65):
        harf = "DC"
    elif (son_not >= 60):
        harf = "DD"
    elif (son_not >= 55):
        harf = "FD"
    else:
        harf = "FF"

    if harf == "FD" or harf == "FF":
        return isim + "---->" + harf + "\n"

def gecenler(satir):

    satir = satir[:-1]#fazladan olan\n i kaldırıyor

    liste = satir.split(",") #['Süleyman Koçyiğit','100','10','60']

    isim = liste[0] #listenin 0.elemanı isim

    not1 = int(liste[1])

    not2 = int(liste[2])

    not3 = int(liste[3])

    son_not = not1 * (3/10) + not2 * (3/10) + not3 * (4/10)

    if (son_not >= 90):
        harf = "AA"
    elif (son_not >= 85):
        harf = "BA"
    elif (son_not >= 80):
        harf = "BB"
    elif (son_not >= 75):
        harf = "CB"
    elif (son_not >= 70):
        harf = "CC"
    elif (son_not >= 65):
        harf = "DC"
    elif (son_not >= 60):
        harf = "DD"
    elif (son_not >= 55):
        harf = "FD"
    else:
        harf = "FF"

    if (harf != "FD" and harf != "FF"):
        return isim + "---->" + harf + "\n"






with open("notlar.txt", "r", encoding="utf-8") as file:

    gecenler_listesi = []
    eklenecekler_listesi = []
    kalanlar_listesi = []

    for i in file:
        eklenecekler_listesi.append(not_hesapla(i))
    for i in file:
        kalanlar_listesi.append(kalanlar(i))
    for i in file:
        gecenler_listesi.append(gecenler(i))


    with open("notlar.txt","w",encoding="utf-8") as file2:

        for i in eklenecekler_listesi:
            file2.write(i)
    with open("kalanlar.txt","w", encoding="utf-8") as file3:

        for i in kalanlar_listesi:
            file3.write(i)
    with open("gecenler.txt","w", encoding="utf-8") as file4:

        for i in gecenler_listesi:
            file4.write(i)
