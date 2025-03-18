x = 'Pluto is a planet'     #''-bitta qo'shtirnoq ichida yozilgan
y = "Pluto is a planet"     #" "-ikta qo'shtirnoq ichida yozilgan
x == y      #True ikalasi bir xil. xohla 2talik. xohla 1talik bilan yoz
""" ichida qanday yozsak, xuddi shunday ko'rsatadi. Ya'ni \n yozmasdan, 3talik qo'shtirnoq ishlatib enterni bosamiz
    va keyingi so'zlarimiz yangi qatorga tushgan xolatda ko'rsatadi"""
'Pluto\'s a planet!'    # ' ' ichida malumot yozilyapti. 's dagi ' ko'rinishi, yani qolishi uchun \ foydalaniladi
                        # \' = '    \" = "   \\  = \    \n = ↩

claim = "Pluto is a planet!"
claim.upper()   #hammasini katta harfga o'zgartiradi
claim.lower()   #hammasini kichik harfga o'zgartiradi
claim.index('plan')     #claimdagi plan so'zining birinchi indexi joylashgan joyi (soni) ni topib beradi
words = claim.split()   #Claim dagi probel bilan ajratilgan so'zlarni alohida alohdia, list elementlari qilib beradi ['Pluto', 'is', 'a', 'planet!']
date = '1956-01-31'
year, month, day = date.split('-')   #date dagi - bilan ajratilgan elementlarni 1956 ni year ga,  01 ni month ga, 31 ni day ga o'zlashtiradi
'*'.join([month, day, year])    #elementlar orasiga * belgisini quyib beradi  01*31*1956

#-------------------------------------------------------------------------------------------------------------------------->>>

planet='Pluto'
position=9
out=planet + ", you'll always be the " + str(position) + "th planet to me."     #barchasi bir xil turda string bo'lishi kerak
out1="{}, you'll always be the {}th planet to me.".format(planet, position)    #out va out1 bir xil .format orqali orasiga qo'shamiz
print(out,'\n',out1)

#-------------------------------------------------------------------------------------------------------------------------->>>

pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
#  nuqtadan keyin 2ta   nuqtadan keyin 3 ta sonni, %foizda     vergul bilan ajratib yoz
nat="{} ning og'irligi taxminan {:.2} kilogram va Yerning ({:.3%} massasiga teng). Bu  {:,} Plutonianlar uchun uy degani.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population,)
print(nat)
#1-{} ichi bo'sh va formatda birinchi argument planetni {}ga joylashtiradi
#2-{} ichida :.2 bor va .formatda 2-argument sifatida pluto_mass ni olib, uni nuqtadan keyin 2ta son ko'rinadigan darajada yaxlitlaydi
#3-{} ichida :.3% bor va .formatda 3-argumentda plutoni earthga bo'ladi va chiqqan natijani nuqtadan keyin 3 son darajasida yaxlitlab, foiz ko'rinishida chiqaradi
#4-{} ichida :, bor va formatda 4-argument populationni oladi va mingliklar orasini , vergul bilan ajratib chiqaradi
#Pluto ning og'irligi taxminan 1.3e+22 kilogram va Yerning (0.218% massasiga teng). Bu  52,910,390 Plutonianlar uchun uy degani.

#-------------------------------------------------------------------------------------------------------------------------->>>

numbers = {'one':15, 'two':25, 'three':35}  #one so'zining qiymati 15 ga, two so'zining qiymati 25 ga, three niki 35 ga teng
print(numbers['one'])       #--->>> 15
#numbers['one'] = 'Pluto'   #--->>> {'one': 'Pluto', 'two': 2, 'three': 3,}
for k in numbers:
    print("{} = {}".format(k, numbers[k]))
    #--->>>one = 15    two = 25 three = 35

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {sayyora: sayyora[0] for sayyora in planets}   #planetsdagi har bir elementni navbat navbat sayyoraga o'zlashtiradi.
                                                    # Sayyorani nomidan keyin : va uning 0-elementi (1-harfini) chiqaradi
print(planet_to_initial)        #{'Mercury': 'M', 'Venus': 'V', 'Earth': 'E', 'Mars': 'M', 'Jupiter': 'J', 'Saturn': 'S', 'Uranus': 'U', 'Neptune': 'N'}
print('\n')

for planet, initial in planet_to_initial.items():   #planet_to_initial dagi : dan keyingi qiymatlarni initialga o'zlashtiradi. planetni natijaga chiqaradi va davomidan initial
    print("{} begins with \"{}\"".format(planet.rjust(10), initial))    #avval planetani nomini chiqaradi
                                                    # begins with chiqadi va initialga o'zlashtirgan natijani chiqaradi
        #'Mercury':'M' demak Mercury ni qiymati M. uni items orqali initial ga o'zlashtiradi

def word_search(doc_list, keyword):
    indices = []
    # Hujjatlarning indekslari (i) va elementlari (doc) orqali takrorlang
    for i, doc in enumerate(doc_list):
        #Satr hujjatini so'zlar ro'yxatiga bo'ling (bo'shliqqa ko'ra)
        tokens = doc.split()
        # O'zgartirilgan ro'yxat tuzing, unda biz moslashishni osonlashtirish uchun har bir so'zni "normallashtiramiz".
        #  Nuqta va vergul har bir soʻz oxiridan olib tashlanadi va u barcha kichik harflarga oʻrnatiladi.
        normalized = [token.rstrip('.,').lower() for token in tokens]
        # Is there a match? If so, update the list of matching indices.
        if keyword.lower() in normalized:
            indices.append(i)
    return indices