#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  8 01:04:00 2025

@author: tojiboevolimjon
"""
#!!! " IF - ELSE "
cars = ['audi','bmw','volvo','kia','hyundai','damas']
for avto in cars: # cars ichidadi har bir avto uchun ...
    if avto == 'bmw':  # ... agar avto bmw ga teng bo'lsa ...
        print(avto.upper()) # avto nomini hamma harflarini katta bilan yoz.
    else: # aks holda ... 
        print(avto.title()) # avto nomini faqat birinchi harfini katta bilann yoz.
        
#!!! " True / False "

name='ali'
name=='ali' #True
name=='vali' #False

name='Alex'
name.lower()=='alex'

name='alex'
name.title()=='Alex'

#!!! "!= " not equal (qiymat teng emasligini tekshirish)

2!=3
10!=20

15!=15

#!!!example for " != " not equal

name1 = input('what is your name?\n>>>') # Foydalanuvchi ismini so'raymiz
if name1.lower() != 'ali': # Agar ism Aliga teng bo'lmasa ...
    print(f"sorry, {name1.title()} we are waiting for Ali.") # quyidagi xabar chiqadi
else:
    print("Hello, Ali")

#!!! comparing Numbers (sonlarni solishtirish)

18>15
20<30
12>=10
40<=51

#example 

age = int(input("Yoshingiz nechida?>>>"))
if age>=18: # yosh 18 dan katta yoki teng bo'lsa
    print('Xush kelibsiz!')
else: # ask holda
    print('Kirish mumkin emas!')
    

#login uzunligini tekshirish

login=input('write your new login :')
if len(login)>=5:
    print('login created')
else:
    print('it should be minimum 5 characters')


#!!! one line if /else ( bir qatorda yozish )

age1=int(input('how old are you?:'))
if age1>65:print('Covid-19 is risk for you')


x, y = 25, 50 # x=25 and y=50
print("x>y") if x>y else print("x<y")

#!!! Practice ( amaliyot)

#1.Create a new list called cars2 = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'], and print each element to the console with the first letter capitalized. For GM, make both letters uppercase.

cars2 = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars2:
    if car=='gm':
        print(car.upper())
    else:
        print(car.title())
    
#2.Complete the above exercise using the “not equal to” (!=) operator


cars2 = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars2:
    if car!='gm':
        print(car.title())
    else:
        print(car.upper())

#3.Ask the user for their login name.If the login is admin, print the message:
#“Welcome, Admin. Would you like to see the list of users?”Otherwise, print:“Welcome, {username}!


name=input('please write your login:')
if name=='admin':
    print(f'welcome,{name.title()}\n do you want see user lists')
else:
    print(f'welcome:{name}')

#4.Ask the user to enter 2 numbers. If the two numbers are equal, display the message “The numbers are equal” on the console.


print('write any 2 numbers:')
a=input('first number:')
b=input('second number:')
if a==b:
    print('the numbers are equal')


#5.Ask the user to enter any number. If the number is negative, display “Negative number” on the console; if it is positive, display “Positive number

number=int(input('write any number:'))
if number>=0:
    print(f'{number} is positive')
else:
    print(f"{number} is negative")

#6Ask the user to enter a number.If the number is positive, calculate its square root and display it on the console.
#If the number is negative, display the message “Enter a positive number”.
  

num2=float(input('write any number:'))  
if num2>=0:
    print(f'the {num2} square root is :{num2**0.5}')
else:
    print('please write a positive number')
    
    
    
    
    
    
    




