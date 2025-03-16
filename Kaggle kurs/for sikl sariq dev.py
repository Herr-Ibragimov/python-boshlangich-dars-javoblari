from lib2to3.fixer_util import does_tree_import

mehmonlar=['Ali','Asu','Lalo', 'Azi']
for funk in mehmonlar:
    print('sizga xabar', funk)
    print(f"xurmatli {funk}, sizni tuyga taklif qilamiz\n")   #Ikki (va undan ko'p) matn ko'rinishidagi o'zgaruvchilarni birlashtirish uchun f-string usulidan foydalanasa bo'ladi
print("xurmat bilan palonchiyevlar oilasi\n")

#------------------------------------------------------------------------------------------------------------------------>>>>>>>>>>>>>

raqamlar=list(range(11))    #11gacha bo'lgan sonlar, oxiri 10
raqamlar_kvadrati=[]        #bo'sh list
for kv in raqamlar:         #raqamlar ichidagi 10gacha bo'lgan sonlarni kv ga o'zlashtir
    raqamlar_kvadrati.append(kv**2)     #raqamlar_kvadrati listiga kv ning darajalarini qo'sh

print('\n',raqamlar)
print(raqamlar_kvadrati)

#------------------------------------------------------------------------------------------------------------------------>>>>>>>>>>>>>

dostlar=[]      #dostlar nomli bosh list
print("5ta eng yaqin do'stingiz kim?")
for n in range(5):      #0 dan 5 gacha (4gacha) qiymatni navbat navbat n ga o'zlashtir
    dostlar.append(input(f"{n+1}-do'stingiz ismini kiriting: "))    #dostlar listiga o'zlashtir: kiritiladigan qiymatni
print('\n',dostlar)
