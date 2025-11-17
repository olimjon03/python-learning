#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 03:44:02 2025

@author: tojiboevolimjon
"""

#!!! while and list

#user kitgan malumotni while orqali listga qoshish

cars=[]
n=1

while True:
  savol=input(f'{n} -write your cars:')
  cars.append(savol)
  stop=input('do you want to stop ? yes or no\n:')
  n+=1
  
  if stop=='yes':
      break
  
print(f'your cars\n{cars}') 



#!!! list ichidan while orqali elementlarni ochirish


names=['ali','jhon','alex','david','ali','husan','ali','alex']

while 'ali' in names:
    names.remove('ali')

print(names)

#

names=['ali','jhon','alex','david','ali','husan','ali','alex']
name='jhon'
while name in names:
    names.remove(name)

print(names)
   

   

#!!! while and dictionary

friends={}

sign=True
while sign:
    name=input('write your friend name :')
    age=input('write your friend age:')
    age=int(age)
    friends[name]=age
    stop=input('do you want to stop ? yes or no:')
    if stop=='yes':
        sign=False
        
print(friends)

#!!!while / list and dictionary
#while yordamida listdagi elementlarga malumot kiritib dictionary qoshish.

countries=['usa','uzbekistan','korea','china','russia']
info={}

while countries:    
    davlat=countries.pop()
    capital=input(f'{davlat} ning poytaxti :')
    info[davlat]=capital
#
print(countries)
    


#!!!PRACTICE (amaliyot)

# 1.Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing.
#Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.

order=[]
num=1

while True:
    name=input(f'{num}-buyurtma nomi :')
    order.append(name)
    
    stop=input('buyurtma tugadimi? yes or no :')
    num+=1
    if stop=='yes':
        break
        
print(order)   










#2. e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing.
 #Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.
 
products={}

while True:
    name =input('write name of product :')
    cost=input('write cost of product :')
    cost=int(cost)
    products[name]=cost
    stop=input('do you want to stop : (yes /no ):')
    if stop == 'yes':
        break
 
 
for name,cost in products.items():
    print(f"{name}- ning narxi :{cost}")
 
 
 
# 3.Yuqoridagi ikki dasturni jamlaymiz.
# Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni e-bozordagi mahsulotlar bilan solishitiring 
#(tayyor ro'yxat ishlatishingiz mumkin). Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring,
# aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.

order=['non', 'sabzi','kartoshka','piyoz']    
products={'non': 1000, 'sabzi': 2400, 'kitob': 5000}

name2=input('mahsulot nomini kiriting :')


while name2 in products.keys():
    print(products[name2])
    name2=input('mahsulot nomini kiriting :')
    
    if name2 not in products.keys():
        break
    
    
    
print('bunday mahsulot yoq!')
    
    


























