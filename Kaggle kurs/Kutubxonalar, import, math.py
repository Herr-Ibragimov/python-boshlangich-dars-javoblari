import math as mt   #import math orqali matematik kutubxonani chaqirdik va as mt orqali uni mt ga o'zlashtirdik #import pandas as pd
from math import pi, log
import numpy
# import math
# mt = math   bu yuqoridagi kutubxona chaqirish bilan bir xil

print("It's math! It has type {}".format(type(mt)))     #Math modulini (kutubxonasini) elementlarini ko'rsatadi

print(dir(mt))
print(round(mt.pi,4))     #math.pi da pi ni qiymati bor
print("4-xonagacha yaxlitlangan pi = {:.4}".format(mt.pi))

#log=mt.log(32,2) #Logorifm uchun ishlatiladi. Log 2asosga kora 32. --->>> 5

#from math import *      #bu orqali matematik kutubxonani umumiy chaqirishimiz mumkin. Faqat bittasini chaqirishimiz mumkin.
#from numpy import *    #iktasini bu ko'rinishda yoza olmaymiz, faqat bittasi qatnashishi mumkin
#from math import log, pi       #mana shu ko'rinishda iktasini yozib olishimiz mumkin
#from numpy import asarray      #ikta kutubxona yozib olish uchun
#print('pi ning miqdori =', pi,'\n', "logarifm 2 asosga ko'ra 32 teng:", log(32, 2))   #endi avavalgidek print uchun math ni chaqirish shart emas.


#print("numpy.random is a", type(numpy.random))      #numpy ni turi
#print("it contains names such as...", dir(numpy.random)[-15:])  #dir() funksiyasi biror ob'ektning barcha atributlarini yoki metodlarini ro'yxatga olish uchun ishlatiladi
rolls=numpy.random.randint(low=1, high=6, size=10)     #1 dan 6 gacha bo'lgan sonlar orasidan, 10ta dona ixtiyoriy son chiqarib beradi
#print(type(rolls))     #rolls ni turi      --->>> <class 'numpy.ndarray'>
#print(dir(rolls))      #rolls ni barcha atributlari va metodlari

print(rolls.mean())     #mean() o'rtacha qiymatini xisoblaydi

#[3, 4, 1, 2, 2, 1] + 10     #bu xato     --->>> can only concatenate list (not "int") to list
#rolls + 10                  #bu to'g'ri   --->>>  array([13, 14, 13, 14, 15, 15, 12, 11, 13, 13])

