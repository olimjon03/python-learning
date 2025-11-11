#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 00:35:17 2025

@author: tojiboevolimjon
"""
#!!!!!Alifbo tarzida joylash

cars=['matiz','spark','malibu','jentra','nexia']
cars.sort()
print(cars)
cars=['Matiz','spark','malibu','jentra','nexia']

#!!!!!royhatni teskari tarzida yaratish

cars=['matiz','spark','malibu','jentra','nexia']
cars.sort(reverse=True)
cars

#!!!!!tartiblangan royhat chiqarish

print(sorted(cars))
cars
print(sorted(cars,reverse=True))

numbers=[1,5,6,4,7,2,3,9,8,11,10]
print(sorted(numbers))
print(sorted(numbers,reverse=True))
numbers


cars.reverse()

#!!!! " len() " royhatni uzunligini korish

len(cars)
len(numbers)

#!!!! "range()" (tartibli raqam royhat tuzish)

num=list(range(0,11))
num
list(range(20,31))
toq_sonlar=list(range(0,10,3))

juft_sonlar=list(range(0,10,2))

numbers2=list(range(0,101,10))

max_qiymat=max(numbers2)
min_qiymat=min(numbers2)

#!!!! " sum() " (listda yigindisi topish)

narxlar=[1200,1500,900,2000,100,500,300]
sum(narxlar)

narxlar=[1200,1500,900,2000,100,500,300]
arzon=min(narxlar)
qimmat=max(narxlar)
jami=sum(narxlar)
print(f'eng arzoni {arzon} ,eng qimmati {qimmat},jami {jami}')

#!!!!listni malum bir qismini ajratish

print(cars[0:3])
print(cars[:3])
print(cars[1:3])
print(cars[1:])

#!!!listdan nusxa olish
cars1=['tiko','matiz','spark','malibu','jentra','nexia']
cars2=cars1[:]
cars2
cars1
cars1.append('damas')
print(cars1)
print(cars2)

#!!! Revision (takrorlash)

cars.insert(2,'kamaz')
print(cars)
cars[2]='avtobus'
cars 
cars.reverse()
cars.sort()
cars.sort(reverse=True)
cars 
print(sorted(cars))
cars
print(sorted(cars,reverse=True))

#!!!  TUPLES (o'zgarmas royhat(list)) !!!

toys=('bear','teddy','lion','cars')
print(toys[0])
toys[-1]
toys[1:4]

#!!! tuplesni listga o'zgartish

toys=list(toys)
type(toys)
toys.append('wolf')
toys=tuple(toys)
type(toys)

#!!!Practice (amaliyot)
#1.Create a list of countries that you know and print the list to the console

countries=['germany','USA','korea','Uzb','france']

#2.Print the length of the list to the console

len(countries)

#3.Print the list in sorted order to the console using the sorted() function

print(sorted(countries))

#4.Print the list in reverse order to the console using the sorted() function

print(sorted(countries,reverse=True))
countries
countries.sort()

#5.Print the list in reverse order using the reverse() method

countries.sort(reverse=True)
countries

#6.Create a list of even numbers from 120 to 1200:
    
numb=list(range(120,1200,2))

#7.Calculate the sum of the numbers in the list and print it to the console:
    
numb1=sum(numb)

#8.Calculate the difference between the largest and smallest numbers in the list and print it to the console

numb2=max(numb)-min(numb)

len(numb)

#9.Print the first 20, middle 20, and last 20 values of the list to the console:
    
numb[0:20]
numb[30:50]
numb[-20:]

#10.Create a list called taomlar and add any 5 foods of your choice to it

taomlar=['osh','manti','mastava','chuchvara']

#11.Copy the taomlar list into a new list called nonushta
nonushta=taomlar[:]

#12.In the new list, keep only the foods suitable for breakfast and add 2 more foods to it
nonushta.remove('chuchvara')
nonushta.append('dimlama')
nonushta.append('non')

#13.Convert the above nonushta list into an immutable list (tuple) and try to assign a new value with nonushta[0] = "qaymoq va non"
nonushta=tuple(nonushta)
nonushta[0]='qaymoq va non'














