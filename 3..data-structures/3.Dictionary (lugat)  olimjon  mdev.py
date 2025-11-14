#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 00:07:59 2025

@author: tojiboevolimjon
"""

##!!! dictionary(lugat)

##moshina haqida malumot berish 

car_info={'model':'spark','color':'red','year':2025,'cost':'2000$'}
print(car_info)

print(car_info['model'])
print(car_info['color'])

#kichik koreyscha lugat

kor_uz={'책':'kitob','펜':'ruchka','연필':'qalam','아이':'bola'}
print(kor_uz['책'])
print(kor_uz['펜'])


#!!!mini project by myself))
#!!!It determines the prices of the products and displays the total cost.
#!!!mahsulot narxalari aniqlab ummumiy narxni chiqarib beradi!!!


total=[]
num=int(input('how many product do you want to buy? ...:'))

cost={'apple':2000,
      'banana':1500,
      'bread':3000,
      'water':1000
      }

for a in range(num):
    product=input(f'{a+1}-product:').lower()
    if product in cost:
        print(f'{product}:{cost[product]} won')
        total.append(cost[product])
    else:
        print(' sorry not found')

print(f'tatol cost is:{sum(total)}')


#!!!dictionary turli malumotlar saqlash mumkin 

student_info={'name':'Olimjon','birthday':26.03,'age':23}

#' \' orqali alohida qatorda yozish mumkin


print(f"{student_info['name'].title()},\
      {student_info['birthday']} da tugulgan kuni,\
     {student_info['age']} yoshda")
          
    
    
#!!! dictionaryga yangi key qoshish


costt1={'apple':2000,'banana':1500,'bread':3000}   

    
costt1['cola']=4000
costt1['energy']=5000
costt1['wine']='none'

print(costt1)
          

#!!!bosh dictionaryga key qoshish

student1={}

student1['name']='ali'
student1['age']=25
student1['univer']='chonnam'

print(student1)
         
#!!! dictionarydan keyni ochirish

costt1={'apple': 2000, 'banana': 1500, 'bread': 3000, 'cola': 4000, 'energy': 5000, 'wine': 'none'}

del costt1['wine']
del costt1['bread']

print(costt1)

#!!! dictionaryni bir nechta qatorga yozish

phones={
        'ali':'iphone',
        'hasan':'samsung',
        'jhon':'none',
        'feruz':'redme'
        }


print(phones) 

#!!! " .get() " metodi (dictionaryda biror key yoq bolsa orniga habar chiqaradi)

costt3={'apple': 2000, 'banana': 1500, 'bread': 3000, 'cola': 4000, 'energy': 5000, 'wine': 'none'}

cost2=costt1.get('alcohol', 'there is no alcohol')

print(cost2)

cost4=costt1.get('choco')#agar ',' dan keyin soz kiritilmasa 'none' chiqadi
print(cost4)




###!!!PRACTICE (Amaliyot)


# 1.otam (onam, akam, ukam, va hokazo) degan lug'at yarating va 
# lug'atga shu inson haqida kamida 3 ta m'alumot kiriting 
# (ismi, tu'gilgan yili, shahri, manzili va hokazo). 
# Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring: 
# Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan


my_dad={'name':'Mahkamboy','age':69,'work':'retired','live':'namangan'}

print(f"my father's name is {my_dad['name']}\
      my father is {my_dad['age']} years old\
        he is {my_dad['work']}\
    he lives in {my_dad['live']}")






#2. Oila a'zolaringizning sevimli taomlari lug'atini tuzing. 
#Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin.
# Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh

fam_food={
    'mybro':'osh',
    'mymom':'manti',
    'mydad':'dimlama',
    'mybro2':'shorva',
    'me':'roltin'}
print(f"my bro likes {fam_food['mybro']}")
print(f"my mom likes {fam_food['mymom']}")
print(f"my dad likes {fam_food['mydad']}")





#3. Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting
# (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.

pydic={
       'int':'butun son',
       'float':'onlik son',
       'str':'matn',
       'bool':'True\False',
       'list':'royhat',
       'tuple':'ozgarmas royhat',
       'dict':'lugat',
       'range':'ketma ket son',
       'NoneType':'bosh qiymat'
       }







#4. Foydalanuvchidan biror so'z kiritishni so'rang va
# so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering.
# Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.


pydic={
       'int':'butun son',
       'float':'onlik son',
       'str':'matn',
       'bool':'True\False',
       'list':'royhat',
       'tuple':'ozgarmas royhat',
       'dict':'lugat',
       'range':'ketma ket son',
       'NoneType':'bosh qiymat'
       }

word=input('pythondagi key wordlardan birortasini yozing \n>>>')
name=pydic[word]
if word in pydic:
    print(f"'{word}'- ning manosi: '{name}'")
else:
    print("bunday so'z topilmadi")





















