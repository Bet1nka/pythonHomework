
'''
from random import randint
def game_candies_bot(name):
    print('start game')
    candies = 2021
    start_pl = randint(1,2)
    bot_name = 'computer'
    print(f'first turn: {start_pl}')
    while candies > 1:
        if start_pl == 1:
            print(f'{candies} - candies on the table , {name} your turn')
            minus = int(input('how many candies yoy want(0-28)?\n'))
            while minus < 1 or minus > 29:
                minus = int(input('incorrect\n how many candies yoy want(0-28)?\n'))
            candies = candies - minus
            print(f'{candies} - candies on the table')
            if candies < 1:
                print(f'game over, {name} win'),
                return
            start_pl += 1
        if start_pl == 2:
            if candies > 0:bot_choise = randint(1,28)
            candies = candies - bot_choise
            print(f'computer take {bot_choise} candies')
            start_pl-= 1
            if candies < 0: print(f'game over, computer win')
name = input('input your name: ')
print(game_candies_bot(name))

dаны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов. Это не просто сумма всех коэффициентов.
Сумма многочленов равна многочлену, членами которого являются все члены данных многочленов.
например, в 1 файле было 3x^3 + 5x^2+10x+11, в другом 7x^2+55
то в итоге будет, 3x^3 + 12x^2+10*x+66
'''
with open('1.txt', 'r') as f: 
    chlen=f.readline()
with open('2.txt','r') as f1:
    chlen1=f1.readline()
print(chlen, chlen1)
def mnogochlen(a,b):
    chleny=[]
    chleny1=[]
    res=[]
    a=a.split('+')
    b=b.split('+')
    for i in a:
        if 'x' in i:
         elements =i.split('x')         
         chlen=[int(elements[0]),elements[1]]
         chleny.append(chlen)
        else: num = int(i)
    for j in b:
         if 'x' in j:
          elements1 = j.split('x')
          chlen1=[int(elements1[0]),elements1[1]]
          chleny1.append(chlen1)
         else: num1=int(j)
    for k in chleny:
        for j in chleny1:
         if k[1]!=j[1]:
            new1=[k[0],'x',k[1],'+']
            res.append(new1)
         elif k[1]==j[1]:
              e=k[0]+j[0]
              new=[e,'x',k[1],'+']
              res.append(new)
    res.append(num+num1)        
    return res
print(mnogochlen(chlen,chlen1))
'''
#Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
a = [1, 6, 2, 3, 5, 4, 1, 7]
def func(ar):
    res=[]
    res.append(min(ar))
    temp=min(ar)
    for i in range(len(ar)):
        for i in range(len(ar)):
         if temp+1==ar[i]:
            res.append(ar[i])
            temp+=1
    return min(res),max(res)
print(func(a))
'''    







