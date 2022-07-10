'''
#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
def weekend(d):
    if (d==6 or d==7):
        return True
    else:
        return False
day=int(input('input number of day from 1 to 7 '))
print(f'this day is weekend - { weekend(day)}')

#Напишите программу, которая принимает на вход координаты точки (X и Y), 
#причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
x=float(input('input x'))
y=float(input('input y'))
def x_y_quatro(a,b):
    if (x==0 and y ==0):
        print('sorry use other coordinats')
    elif(x>0 and y>0):
        print(' 1 part')
    elif(x<0 and y>0):
        print(' 2 part')
    elif(x<0 and y<0):
        print(' 3 part')
    elif(x>0 and y<0):
        print(' 4 part')
    elif(x==0):
        print(' your point on x')
    elif(y==0):
        print(' your point on y')
x_y_quatro(x,y)
'''