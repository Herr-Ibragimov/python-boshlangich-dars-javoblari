

print(10//3)    #butun qismi
print(10%3)     #qoldiq qismi
print(10**3)    #darajasi

#help(round(-2.01))

print('\n')     #chiqadigan natijada 3 ta qator joy tashlab beradi


def least_difference(a, b, c):
    """a b c orasidagi eng kichik qiymatni ko'rsatadi. misol:
    >>> least_difference(1, 5, -5)
    4
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)
print(least_difference(1,5,-5))
#help(least_difference)


print('\n')
print(1,2,3,sep=' < ')


def greet(who="Colin"):
    print("Hello,", who)
greet()
greet(who="Kaggle")
greet("world")
# (obyektni yozishimiz shart emas, natija bir xil chiqadi)


def mod_5(x):
    """5ga bolgandagi qoldiqni korsatadi"""
    return x % 5
print(
    'Eng katta son?',
    max(100, 51, 14),
    'sonni 5ga bolganda eng katta qoldiq qoladigan son?',
    max(100, 51, 14, key=mod_5),
    sep='\n',
)
print('\n')



