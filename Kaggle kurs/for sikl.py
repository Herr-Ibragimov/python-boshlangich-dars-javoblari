#for bilan ishlash
#while bilan ishlash
#Katta harflar bilan yozilganlarni chiqarish misol
#range funksiyasiga misol
#listga nechtadur qiymat kiritamiz (istalgancha). listni ko'rsatadi va uni kvadratini hisoblab beradigan dastur
#harflari 6 tadan kam bo'lgan elementlarni ko'rsatadigan dastur
#nechta manfiy son qatnashganini sanab beradigan dastur


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

#While operatorini for dan farqi,
#for biror oraliq yoki shartlar asosida takrorlaydi. bu ro'yxat, oraliq uchun qulay
#while esa ma'lum bir shart bajarilguncha takrorlanadi. shartning to'g'ri bo'lishini kutadi va shart noto'g'ri bo'lsa, takrorlash to'xtaydi

i = 0
while i < 10:
    print(i, end=' ')
    i += 1 # qiymatini 1 ga oshiradi

#------------------------------------------------------------------------------------------------------------------------>>>>>>>>>>>>>
#listga o'zimiz qiymat berishni ko'rib chiqamiz
squares=[]      #bo'sh ro'yxat yaratamiz
print("Ro'yxatga qiymatlar kiritishni boshlang. To'xtatish uchun bo'sh qiymat bosing.")
for i in range(100):  # 100 ta qiymat kiritishga imkon beradi (o'zgartirish mumkin)
    value = input(f"{i+1}-chi qiymatni kiriting: ")
    if value == "":  # Agar foydalanuvchi bo'sh qiymat kiritsa, siklni to'xtatadi
        print("Qiymat kiritish tugatildi.")
        break
    squares.append(int(value))  # Kiritilgan qiymatni ro'yxatga qo'shamiz

print("Kiritilgan ro'yxat:", squares)

#endi kiritgan elementlarimiz kvadratini chiqaramiz
for n in squares:
    print(f"{n} ning kvadrati: {int(n**2)}")

 # ------------------------------------------------------------------------------------------------------------------------>>>>>>>>>>>>>
# kvadrat = [n**2 for n in range(10)]
# print(kvadrat)
#         ================ xuddi shu kodni biz pastdagi ko'rinishda yozamiz
# kvadrat = []
# for n in range(10):
#     kvadrat.append(n**2)
# print(kvadrat)
#------------------------------------------------------------------------------------------------------------------------>>>>>>>>>>>>>
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
short_planets = [planet for planet in planets if len(planet) < 6]   #agar sayyora nomi 6ta harfdan kam bo'lsa ko'rsatadi
print(short_planets)


#------------------------------------------------------------------------------------------------------------------------>>>>>>>>>>>>>

def count_negatives(nums):
    """listdagi nechta manfiy sonlar qatnashganini topuvchi dastur >>> count_negatives([5, -1, -2, 0, 3])  >>>  2 """

    n_negative = 0
    for num in nums:
        if num < 0:
            n_negative = n_negative + 1
    return n_negative

# def count_negatives(nums):
#     return len([num for num in nums if num < 0])  numsga kiritilgan qiymatlar 0 dan kichkina bo'lsa sanab ketaveradi
#
# def count_negatives(nums):
#     return sum([num < 0 for num in nums])     agar elementlar 0 dan kichkina bo'lsa, True qiymat beradi va sanab ketaveradi
#     #  True + True + False + True qiymati 3ga teng. shu kabi hisoblaydi

def menu_is_boring(meals):
    """meals dagi elementlar ketma ket bir xil bo'lsa (1-va 2- element ['asd','asd']) True qaytar aks xolda False"""

    for i in range(len(meals)-1):
        if meals[i] == meals[i+1]:
            return True
    return False