import cmath
import math


planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
print(planets[0], planets[1], planets[-1], '\n',     planets[0:4], '\n',     planets[3:])
#     planets[0] - Mercury
#     planets[1] - Venus
#     planets[-1] - Neptune     #oxirgi element
#     planets[0:4] = planets[:4] - 1-elementdan 4-elementgacha (Marsgacha) ['Mercury', 'Venus', 'Earth']
#     planets[3:0] = planets[3:] - 3-elementdan keyin oxirgi elementgacha (marsdan)
#     ['Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']


# (list quyidagi ko'rinishda, bir nechta qatorda yozish ham mumkin, ikala holat bir xil)
hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'], # (oxirgi  elementdan keyin vergul quyish ixtiyoriy)
]
print(hands)


planets[3] = 'Malacandra'   #4-elementni Marsni Malacandra ga o'zgartiradi
len(planets)    #planetalar soni - listdagi elementlar soni
sorted(planets)     #alfabet bo'yicha ketma-ket taxlash
planets.append('Pluto')    #list oxiriga pluto degan element qo'shib beradi
planets.pop()       #oxirgi elementni o'chiradi
planets.index('Earth')      #earth nechinchi indexda turganini ko'rsatadi
"Earth" in planets  #True   Earth degan element bormi?
"Calbefraques" in planets   #false



primes=[2,3,5,7]
sum(primes)     #elementlari yig'indisi 17
max(primes)     #elementlar eng kattasi 7
#primes.mean()  #mean() o'rtacha qiymatini xisoblaydi
x = 0.125
x.as_integer_ratio()       #0.125=1/8 shuni 1,8 deb ko'rsatadi

x = 12
# x haqiqiy son, uning imag qismi 0
print(x.imag)
# c murakkab son. uning img qismi 37. j dan oldin yozilgan son
c = 12 + 37j
print(c.imag)

a = 1
b = 0
a, b = b, a
print(a, b)
#---------------------------------------------------------------------------------------

def purple_shell(racers):
    # >>> r = ["Mario", "Bowser", "Luigi"]
    # >>> purple_shell(r)
    # >>> r
    # ["Luigi", "Bowser", "Mario"]
    temp = racers[0]
    racers[0] = racers[-1]
    racers[-1] = temp
    return  racers

abc=["Mario", "Bowser", "Luigi"]
print(purple_shell(abc))
# birinchi element oxiriga, oxirgi element birinchiga
#-------------------------------------------------------------------------------------

def fashionably_late(arrivals, name):
    """arrivals listida mehmonlar ro'yxati beriladi. name kechikib kelgan bo'lsa True qaytarsin
    """
    order=arrivals.index(name)
    return order >= len(arrivals)/2 and order!= len(arrivals)-1

arri=['asd','qwe','ert','asa','opq','123']
if  fashionably_late(arri,'opq') == True :
    print("ha kechikib kelgan")
else: print("yo'q kechikmagan")