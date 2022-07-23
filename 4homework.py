'''
Вычислить результат деления двух чисел c заданной точностью d

Пример:

- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
 3 (необязательное). 
Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и 
выводит на стандартный вывод сводную таблицу результатов всех матчей.
За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число nn — количество завершенных игр.
После этого идет nn строк, в которых записаны результаты игры в следующем формате:
Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой

Вывод программы необходимо оформить следующим образом:
Команда:Всегоигр Побед Ничьих Поражений Всегоочков

Конкретный пример ввода-вывода приведён ниже.

Порядок вывода команд произвольный.

Sample Input:

3
Спартак;9;Зенит;10
Локомотив;12;Зенит;3
Спартак;8;Локомотив;15
Sample Output:

Спарт:2 0 0 2 0
Зенит:2 1 0 1 3
Локов:2 2 0 0 6

x1,x2,number=float(input('firstnumber - ')),float(input('secondnumber - ')),int(input('number- '))
def div(a,b,num): # если пользователь вводит колличество символов после запятых к примеру 3-0.001(или отрицвтльную степнь 10)
 divx=a/b
 return(round(divx,num))
print(div(x1,x2,number))

x1,x2,number=float(input('firstnumber - ')),float(input('secondnumber - ')),str(input('number- '))
def div1(a,b,num): #если пользователь вводит 0.0001 
 divx=a/b
 n1=num.replace('.','')
 count=0
 for i in n1:
    count+=1
 return(round(divx,count-1))
print(div1(x1,x2,number))

x=int(input('input number - '))
def simple_mnozhitel(num):
    simple=2
    mnozh=[]
    while simple*simple<=num:
        if num%simple==0:
         mnozh.append(simple)
         num=num//simple         
        else: simple = simple+1
    if num>1:
        mnozh.append(num)
    return mnozh
print(simple_mnozhitel(x))
'''
sumofgame= int(input('how many games you watch-> '))
resultofgame = []
dictdata = {}

for i in range(sumofgame):
         res=input('input name of team and goals(example: a;3;b;2)-> ')
         gameresult=res.split(';')
         gameresult[1],gameresult[3]=int(gameresult[1]),int(gameresult[3])#from str to int goals
         resultofgame.append(gameresult)
         x=dictdata.fromkeys([gameresult[0], gameresult[2]],[0,0,0,0,0])
         dictdata.update(x)#dictianoty of games
         for key in dictdata:
            if gameresult[1]>gameresult[3]:
                dictdata[gameresult[0]][0]+=1#счетчик игр
                dictdata[gameresult[2]][0]+=1#game counter
                dictdata[gameresult[0]][1]+=3#счтчик очков
                dictdata[gameresult[2]][1]+=0#counter point
                dictdata[gameresult[0]][2]+=1#счтчик побед
                dictdata[gameresult[2]][3]+=1#cчетчик поражений
            elif gameresult[1]==gameresult[3]:
                dictdata[gameresult[0]][0]+=1#counter game
                dictdata[gameresult[2]][0]+=1#gamecounter
                dictdata[gameresult[0]][1]+=1#point count
                dictdata[gameresult[2]][1]+=1#pointcount
                dictdata[gameresult[0]][4]+=1#счтчик ничей
                dictdata[gameresult[2]][4]+=1#count =
            elif gameresult[1]<gameresult[3]:
                dictdata[gameresult[0]][0]+=1#gamecount
                dictdata[gameresult[2]][0]+=1 #gamecount
                dictdata[gameresult[0]][1]+=0#point count
                dictdata[gameresult[2]][1]+=3#pointcount
                dictdata[gameresult[0]][3]+=1#счтчик поражений
                dictdata[gameresult[2]][2]+=1#countwin

print(dictdata)

                
         



