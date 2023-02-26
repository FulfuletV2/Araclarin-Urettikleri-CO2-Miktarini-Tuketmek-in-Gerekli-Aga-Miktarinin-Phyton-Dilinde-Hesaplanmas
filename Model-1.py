import math

#Notlar
#İstanbul araç miktarı = 3162884
#Türkiye araç miktarı = 14113925

#Girdi verisi olan araç miktarı

aracmiktari = int(input("Araç miktarını giriniz:"))

#Marka başı yakıt türü oranları

lpg = 0.353
dizel =0.371
benzin = 0.264
elektrikli = 0.009

diger = 0.003

#Sabitler
 
senelikalinanyol = 15000

markaorani = 0

#Araçların markaları oranları ve bunların benzin&dizel CO2 emisyonları

renult = [0.158 , 209.5 , 182.5]
volkswogen = [0.108 , 243 ,207]
fiat = [0.111 , 157 , 154.5]
dacia = [0.043 , 120 , 93]
opel = [0.055 , 259.5 , 129]
hyundai = [0.06 , 182 , 170.5]
ford = [0.066 , 181.5 , 156.5]
toyota = [0.051 , 161.5 , 189.5] 
mercedesbenz = [0.043 , 265.5 , 214.5]
nissan = [0.042 , 217 , 216]

digermarkalar = [0.263 , 209.5 , 182.5]

markalar =[renult, volkswogen, fiat, dacia, opel, hyundai, ford, toyota, mercedesbenz, nissan, digermarkalar]

#marka başı CO2 salınım fonksiyonu(kg)

def markaco2salinimi(list):

    markaorani = list[0]
    markabasiarac = aracmiktari * markaorani 

    benzinorani = markabasiarac * benzin * list[1] 
    dizelorani = markabasiarac * dizel * list[2] 

    lpgorani = markabasiarac * lpg * list[1] * 4/5
    elektrikliorani = markabasiarac * elektrikli * list[1] * 95/100

    digersabitorani = markabasiarac * diger * 209.5  * 4/5

    sonuc = (benzinorani + lpgorani + dizelorani + elektrikliorani + digersabitorani) / 1000 *senelikalinanyol

    return(sonuc)

#Toplam CO2 salınımısenelik (kg)

def totalco2salinimi():
    toplam = 0
    i = 0
    while(i< len(markalar)):

        toplam = toplam + markaco2salinimi(markalar[i])
        i = i + 1

        #print(toplam)

    return(toplam)


def gerekliagacmiktari():
#yılık güneşenme = 2604 saat ağaç başı saatlik tüketim = 2.5 kg
    
    print( "Gerekli minimum ağaç miktarı" , math.ceil( totalco2salinimi() / 2604 * 2.5 ))


gerekliagacmiktari()



    

