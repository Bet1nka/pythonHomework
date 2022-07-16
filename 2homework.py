#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
number=float(input('input number '))
def sum_of_digits(num:float):
    sum=0
    while num%10!=0:
        num*=10
    while num>0:
        lastdigit=num%10
        sum+=lastdigit
        num//=10
    print(sum)
    return sum
sum_of_digits(number)
'''
#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
n = int(input('input number '))
def factorial(num:int):
 startf=1
 for i in range(num):
   startf += startf * i
   print(startf)
factorial(n)
'''