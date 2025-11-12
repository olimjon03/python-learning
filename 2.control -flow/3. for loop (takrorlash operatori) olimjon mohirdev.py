#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  7 23:17:04 2025

@author: tojiboevolimjon
"""

#!!!For loop (takrorlash operatori)

friends=['ali','jhon','beki','jek','lely']
for dostlar in friends:
    print('hello my friend,',dostlar)
    print('good bye my friend,',dostlar)
     
relativs=['rasul','husan','hasan','aziz','abror']
for qarindosh in relativs:
    print(f"hurmatli {qarindosh}, sizni 10 noyabr kuni yigilishga taklif qilamiz!!")
    print('hurmat bilan ..lar oilasi\n')

#!!! with Numbers (sonlar bilan ishlash)

numbers=list(range(1,11))

for son in numbers:
    print(f">>{son} ning kvadrati {son**2} ga teng")
    print(f">>{son} ning kubi {son**3} ga teng\n")

    
number2=list(range(1,16))
sonlar_kvadrati=[]
for son in number2:
    sonlar_kvadrati.append(son**2)
print(number2)
print(sonlar_kvadrati)

#!!! kichik project(for operatori va input() funktsiyasini jamlab, ro'yxatni foydalanuvchidan olingan qiymatlar bilan to'ldirish mumkin:)

d=list(range(1,11))
dostlar=[]
print(' 10 ta dostingizni belgilang\n')
for a in d :
    dostlar.append(input(f"{a} - dostingizni ismini kiriting\n>>"))
print('sizning dostlaringiz ;',dostlar)
        
#!!!!Practice (AMALIYOT)

#1.Create a list called ismlar with at least 5 elements, and print a repeated message for each name in the list

ismlar=['ali','jhon','bek','alex','david','lilly']
for name in ismlar:
    print(f'hello my friend {name} !!!' )


#2.After the loop ends, print a message saying “The code was repeated n times” (replace n with the actual number of repetitions) 

ismlar=['ali','jhon','bek','alex','david','lilly']
for name in ismlar:
    print(f'hello my friend {name} !!!' )
print(f'kod {len(ismlar)} marta takrorlanadi')


#3.Create a list of odd numbers from 10 to 100. Print the cube of each element in the list on a new line to the console.

num= list(range(11,101,2))

for n in num:
    print(f"{n} , ning kubi {n**3} ga teng")
    
    
#4.Ask the user to enter their 5 favorite movies and store them in a list called kinolar. Then, print the result to the console.  

kinolar=[] 
b=list(range(1,6))
print ('5 ta eng sevimli kinoyingiz \n>>>')
 
for a in b:
    kinolar.append(input(f"{a}-kinoyingiz \n>> "))
print("sizning kinolar royhatingiz",kinolar)

#5.Ask the user how many people they met (talked to) today, then ask for each person’s name one by one and store them in a list. Finally, print the list to the console.

n_people=int(input('bugun nechta odam bilan uchrashdingiz?\n>>>:'))
people=[]
a=list(range(n_people))
print('Bugun nechta odam bilan uchrashdingiz?')
for person in a:
    people.append(input(f'{person+1}-odam:'))
print(f'siz {people} lar bilan uchrashgansiz')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    