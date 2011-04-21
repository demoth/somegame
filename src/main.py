# -*- coding: utf-8 -*-

#Пт. 25 марта 2011 20:59:31 
##1 2 3 4 5 6 7 8
#x = 5
#y = x ** 2
##9
#x = -1.5
##10
#summa = 0
##11
#n = 1
#n = n + 1
##12
#counter = 4
#counter = counter - 2
##13
#avg = (y + x) / 2
##14
#y = -2.7 * x ** 3 + 0.23 * x ** 2 - 1.4
##15
#y = 1 / (x ** 2)
##16
#funts = 200
#kilos = funts * 0.4095
##17
#versts = 9333
#kilometers = versts * 1.0668
##18
#s = x * y
##19
#a = 3
#h = 5
#s = 0.5 * a * h
##20
#b = 4
#s = 0.5 * (a + b) * h
##21
#import math
#r = 4
#s = math.pi * r ** 2
##22
#s = 2 * math.pi * r * (h + r)
#v = math.pi * r ** 2 * h
##23
#v = a * b * h
##24
#v = 0.75 * math.pi * r ** 3
#s = 4 * math.pi * r ** 2
##25
#v = math.pi * r ** 2 * h
##26
#v = math.pi * h * (a ** 2 - b ** 2)
##27
#s = 1 / 3 * math.pi * r ** 2 * h
##28 = #25
##29
#u = 4
#r = 30.0
#i = u / r
##30
#r = u / i
##31
#r1 = 3
#r2 = 5
#r3 = 9
#r = r1 + r2 + r3
##32
#r = r1 * r2 / (r1 + r2)
##34
#kiloom = 0.001 * r
##35
#applePrice = 40
#tomatoPrice = 60
#cucumberPrice = 100
#price = 0.5 * applePrice + 1.0 * tomatoPrice + 2 * cucumberPrice
#
##36
#print(u"Даниил Бубнов")
##37
#print("Python 2.6.6") #; print("Turbo Pascal 7.0")
##38
#print(u"Унылая пора! Очей очарованье!\nПриятна мне твоя прощальная краса -\nЛюблю я пышное природы увяданье,\nВ багрец и золото одетые леса.\n\t\tА.С. Пушкин")
##39
#a = 3.523
#print("{0:.5}".format(43.234))
##40
##41
#print("{0:.5}  {1:.5}  {2:.5}".format(235.23, 23.351, 53.612))
##42
#print("{0:.5} \n{1:.5} \n{2:.5}".format(635.23, 63.351, 66.612))
##43
#print("x1=" + repr(25.3) + "\nx2=" + repr(53))
##44 
##45
#
##46
## radius = input()
#
##47
## u  = input()
## r = input()
#
##48 O_o
##49
#print("Type in 'r' and 'h'")
## r = input()
## h = input()
#print("\nVolume is " + repr(math.pi * r ** 2 * h))

#50
#print("Type in notebooks:")
#n1 = input()
#print("Type in notebook price:")
#p1 = input()
#print("Type in pencils:")
#n2 = input()
#print("Type in pencil price:")
#p2 = input()
#print("Price is " + repr(n1 * p1 + n2 * p2))

#51
#print(u"Вычисление площади прямоугольника.")
#print(u"Введите исходные данные:")
#print(u"Высота")
#heigth = input()
#print(u"Ширина")
#width = input()
#print(u"Площадь прямоугольника:" + repr(heigth * width))

#52
#print(u"Вычисление площади параллелепипеда.")
#print(u"Введите исходные данные:")
#print(u"Высота")
#heigth = input()
#print(u"Ширина")
#width = input()
#print(u"Глубина")
#depth = input()
#print(u"Объём параллелепипеда:" + repr(heigth * width * depth))
# and so on till 

#72
#print(u"Интервал в минутах")
#mins = input()
#hours = mins / 60
#remainder = mins - hours * 60
#print(repr(hours) + u" ч. " + repr(remainder) + u" мин.")  

#76
#print(u"Деление")
#x = input()
#y = input()
#if y == 0:
#    print(u"Деление на ноль!")
#else:
#    print((x + 0.0) / y)

#88
#import random
#a = int(100 * random.random())
#b = int(100 * random.random())
#c = a - b
#print(u"Сколько будет " + repr(a) + "-" + repr(b) + "?")
#answer = input()
#if answer == c:
#    print(u"Верно")
#else:
#    print(u"Не верно! Правильный ответ:" + repr(c))

#92
#print(u"Введите рост (см) и вес (кг)")
#height = input()
#weight = input()
#diff = height - weight - 100
#if diff > 0:
#    print(u"Надо поправиться на " + repr(diff) + u" кг.")
#elif diff < 0:
#    print(u"Надо сбросить " + repr(diff) + u" кг.")
#else:
#    print(u"Ваш вес и рост в порядке")

#96
#print(u"Введите стоимость:")
#p = input()
#if p % 10 == 1:
#    suff = u"рубль"
#elif 2 <= p % 10 <= 4 and p > 20 or 2 <= p <= 4:
#    suff = u"рубля"
#else:
#    suff = u"рублей"
#print(repr(p) + " " + suff)

#99
#for i in range(10):
#    print(u"Даниил Бубнов")

#100
#for i in range(10):
#    print("{0:5} {1:5}".format(i,i ** 2))
    
#103
#n = input()
#sum = 0
#for i in range(n*2):
#    if i % 2 == 0:
#        sum = sum + i
#print(repr(sum))

#121
#for i in range(1,11):
#    line = " "
#    for j in range(1,11):
#        line = line +  "{0:5}".format(repr(i * j))
#    print(line)
