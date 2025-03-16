print('09','12','2016', sep='-', end='year')  #sep har bir elementni orasiga - quyib beradi, end element oxirida 09-12-2016year
print('\n')

multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:      #multiplicands ichidagi elementlarni navbat navbat mult ga o'zlashtiradi
    product = product * mult    #mult elementlarini ketma ket ko'paytirib keturadi va productga yuklaydi p=1*2; p=2*2; p=4*2; p=8*3; p=24*3; p=72*5
print(product)
#------------------------------------------------------------------------------------------------------------------------>>>>>>>>>>>>>

s = 'katta Harf  bilan Boshlanganlarni, Faqatgina Katta harflarini CHIQARADI'
for katta in s:
    if katta.isupper():      #Katta harflarni o'zlashtirish
        print(katta, end=' ')
print('\n')
#------------------------------------------------------------------------------------------------------------------------>>>>>>>>>>>>>

for i in range(5):          #range funksiyasi raqamlar ketma ketligini qaytaradi. 0dan boshlaydi va oxiri 4 boladi hozir
    print("qiymat oladi. i =", i)

sonlar=list(range(3,11))    #sonni 3 dan boshlaydi
print(sonlar)
#------------------------------------------------------------------------------------------------------------------------>>>>>>>>>>>>>





