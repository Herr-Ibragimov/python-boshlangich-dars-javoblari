print(10%3)

from queue import PriorityQueue
from xmlrpc.client import Boolean


def a(soat_haq, ish_soat):
    HAFTALIK_HAQ=soat_haq*ish_soat*5
    return HAFTALIK_HAQ
hisobla = a(15,8)
print("haftalik oladigan ish haqi =",hisobla)

x=14
print(x)
print(type(x))
#type() kiritgan sonimiz qaysi turda, (int) ekanligini bildiradi

nearly_pi = 22/7
print(nearly_pi)
print(type(nearly_pi))
# float, qoldiqli sonlar

rounded_pi=round(nearly_pi,5)
print(rounded_pi)
print(type(rounded_pi))
#round() chiqadigan sonimizni nechinchidur xonagacha yaxlitlab beradi

z1=(1<2) #z1=true
print(not z1)  #natijani teskari qiladi not true = flase
print(type(z1))
#mantiqiy bo'lsa bool

y="Salom dunyo"
print(y)
print(type(y))
#Yozuvli uchun str (string)

print(len(y)) # len()yozilgan belgilar soni

raqam="1.34" #kiritilgan raqamni tekst sifatida ko'radi
print(raqam)
print(type(raqam))

yangi_raqam=float(raqam)   #tekst  turidagi raqamni, float raqamiga o'tqazadi
print(type(yangi_raqam))

yozuv = "abc" + "def"    #yozuvni ketma ket yozib beradi
print(yozuv)
print(type(yozuv))

yangi_yozuv = "abc" * 3  #yozuvni 3 marta ko'paytirib beradi
print(yangi_yozuv)
print(type(yangi_yozuv))

print(3 * False)                #False = 0    True =1
print(-3.1 * True)
print(type("abc" * False))
print(len("abc" * True))

def uy(beds, baths, has_basement):
    value = 80000+beds*30000+baths*10000+has_basement*40000
    return value

