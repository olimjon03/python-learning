#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 03:20:03 2025

@author: tojiboevolimjon
"""

#!!!Lists(royhatlar)

fruits=['apple','banana','ananas','pineapple']
print(fruits)

numbers=[12,13,14,15,16,17,181,90,-1,2.5]

wordnum=[12,13,15,'hello','world']

space=[]

print(fruits[0])
print(fruits[3])
fruits[-2]
print(fruits[1].upper())
print(fruits[2].title())

numbers[0]+numbers[3]
numbers[1]+13

fruits[0]='olma'
fruits [1]='banan'


#!!! " .append() " ( oxirgi qismga object qoshish)

fruits.append('cherry')
print(fruits)
fruits.append('o\'rik') 
fruits

#!!! " .insert()" (ro'yhotni belgilangan qismiga object qo'shish)

fruits.insert(1,'orange')
print(fruits)
fruits.insert(-2,'behi')
print(fruits)

#!!! " del " (ro'yhatdan tartib raqami orqali o'chirish)

cars=['damas','matiz','nexia']
del cars [1]
print(cars)

#!!!  ".remove() " (ro'yhatdan nomi orqali o'chiradi)
cars=['damas','matiz','nexia']
cars.remove('nexia')
cars

#!!! ".pop() " (royhat 1 elementni chiqarib olish)

products=['un','non','yog','suv','cola','pepsi']  
newproduct=products.pop(1)
print(newproduct)

#!!!Practice (amaliyot)


#1. Create a list called 'names' and add at least 3 of your close friends' names
names = ["Alice", "Bob", "Charlie"]

#2.Write a short message to each friend in the list and print it to the console.

print('salom '+names[0]+', bugun choyxona bormi?\n'+names[1]+',choyxonaga boramizmi?')

#3.Create a list called ‘sonlar’ and fill it with different numbers (positive, negative, integer, decimal).

sonlar=[1,23,-2,2.3,15]

#4.Perform various arithmetic operations on the numbers in the list above. Change the value of some numbers in the list, and replace others.

sonlar[2]+sonlar[1]
sonlar[1]=20
print(sonlar)
sonlar.append(-20)
sonlar.insert(2, 25)
sonlar 

#5.Create two lists: in one, put the names of historical figures you respect the most, and in the other, put the names of living people from our time.

ajdodlar=['alisher navoiy','bobur','amir temur','beruniy']
hozirgilar=['elon mask','bill gates']

print('men tarixiy shaxslardan '+ajdodlar.pop(2)+'  bilan,zamonaviy shaxslardan esa '+hozirgilar.pop(0)+'  bilan suhbat qilishni istardim')

#6.Create an empty list called friends and use .append() to add 5-6 friends you want to invite to a gathering.

friends=[]
friends.append('ali')
friends.append('alex')
friends.append('jhon')
friends.append('bek')
friends.append('husan')
print(friends)

#7.from the list above, remove the people who cannot come to the gathering using the .remove() method.

friends.remove('ali')
friends.remove('husan')

#8.Create an empty list called new_guests. Using the .pop() and .append() methods, take the names of friends who came to the gathering from the friends list and add them to the new_guests list.

new_guests=[]
new_guests.append(friends.pop(1))
new_guests.append(friends.pop(0))
print(new_guests)






















