
'''#Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
listtest=[123, 'privet', '123', 1, 'hello']
x=int(input())
def find_number (list1, number):
    for i in list1:
        if i==number:
         print(x,' - yes')
    print(x,'-NO')
find_number(listtest,x)

# #Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

list3= ["qwe", "asd", "zxc", "qwe", "ertqwe"]
string3 = input()
def second_in(listx,element):
    count=0
    for i in range(len(listx)):
        if listx[i]==element:
            count=count+1
            if count==2:
                return f'yes:{i}'
    return 'NO'
print(second_in(list3,string3))
'''
'''
3* (необзательная).
Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком количестве используется в этой книге.
Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова, разделённые пробелом и вывести получившуюся статистику.
Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального слова в этой строке число его повторений (без учёта регистра) в формате "слово количество" (см. пример вывода).
Порядок вывода слов может быть произвольным, каждое уникальное слово﻿ должно выводиться только один раз.
Sample Input 1:
a aa abC aa ac abc bcd a
Sample Output 1:
ac 1
a 2
abc 2
bcd 1
aa 2
Sample Input 2:
a A a
Sample Output 2:
a 3
'''


str_x=[input().lower().split()]#вводим текст
def tex_finder(str1):
   uniq_words={}#создаем пустой словарь для уникальных слов
   for word in str1:#просматриваем слова в тексте
    if word not in uniq_words:#если слово не в словаре уникальных строк
        uniq_words.append(word)#добавляем его в словарь уникальных слов
    for element in uniq_words:#перебирем элементы словаря уникальных слов по тексту?
        count=0
    if element in str1:
        count=count+1
        uniq_words[i]=[element:count]
    return count
             
print(tex_finder(str_x))
    