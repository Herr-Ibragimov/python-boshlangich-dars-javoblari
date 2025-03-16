def get_grade(score):
    if  score >= 90:
        grade = "A"
    elif  score>=80:
        grade = "B"
    elif score>=70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade
#
# score = input("Bahoyingizni kiriting: ")
# a=get_grade((int(score)))
# print("Sizning bahoyingiz harfda: ",a)

# TODO Edit the function to return the correct bill for different
# #values of num_gallons
# def get_water_bill(num_gallons):
#     if num_gallons<=8000:
#         bill = num_gallons*5/1000
#     elif    num_gallons<=22000:
#         bill = num_gallons*6/1000
#     elif    num_gallons<=30000:
#         bill = num_gallons*7/1000
#     else:   bill = num_gallons*10/1000
#     return bill
# num_gallons = input("nechta gallon: ")
# a=get_water_bill(int(num_gallons))
# print(a)

def get_phone_bill(gb):
    if  gb<=15:
        bill = 100
    else:
        bill = 100+(gb-15)*100
    return bill