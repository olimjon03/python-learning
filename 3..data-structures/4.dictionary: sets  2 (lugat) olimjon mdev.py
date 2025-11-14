#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 08:57:25 2025

@author: tojiboevolimjon
"""
 #!!!  ".items()" lugatdagi elementlarni chiqaradi
 
student={
     'name':'ali',
     'age':'24',
     'level':'3',
     'major':'computer',
     'live':'korea'
     }

print(student.items())

#lugatdagi elementlarni tartibli joylashtirish

for key,value in student.items():
    print(f'{key} - {value}')
    
    for k,v in student.items():
        print(f'{k}-{v.title()}')
        
        
#!!! " .keys()" diictionarydagi kalit sozlarni chiqarib beradi.

phones={
    'iphone':'america',
    'samsung':'korea',
    'redme':'china',
    'nokia':'finland',
    'iphonex':'america'}

print(phones.keys())

for a in phones.keys():
    print(a.upper())


#yuqoridagi kodda ".keys"ni ishlatmasa ham bir hil natija chiqadi

for a in phones:
    print(a.upper())
    
#dictionarydagi key larni boshqa listdan foydalananib dictionaryda bor yoki 
#yoqligini tekshirish

phones_cost={
    'iphone':1000,
    'samsung':900,
    'redme':400,
    'nokia':200,
    'iphonex':500}


products=['samsung','motorolla','fly','lenux','iphone']

#agar listdagi productlar dictionaryda bolsa uni narxini chiqaradi

for item in phones_cost:
    if item in products:
        print(f'{item.title()} ning narxi {phones_cost[item]}')
        
# agar listdagi productlar dictionaryda bolmasa  chiqaradi

for item in phones_cost:
    if item not in products:
        print(f'{item.title()} dokonda yoq ')
        
#!!! " sorted () " dictionarydagi keysni tartib bilan joylash alifbo tartibida


fruits={
        'banana':2000,
        'ananas':5000,
        'cherry':4000,
        'kakos':3500,
        'mandarin':6000
        }

for a in sorted( fruits):
    print(a.title())


#!!! ".values()" dictionarydagi kalitning qiymatlarini chiqaradi.


phones={
    'iphone':'america',
    'samsung':'korea',
    'redme':'china',
    'nokia':'finland',
    'iphonex':'america'}

print(phones.values())

print('telefonlar chiqarilgan davlatlar')

for tel in phones.values():
    print(tel)

#!!! " set() " dictionarydagi yoki boshqa roydagi takrorlangan elementlarni olib tashlaydi


fruits2={
        'banana':2000,
        'banana':2000,
        'ananas':5000,
        'cherry':4000,
        'kakos':3500,
        'mandarin':6000,
        'kakos':3500,
        }
for meva in set (fruits):
    print(meva)

#!!! "set()" ham malumot turi huddi list dictionary kabi.

cars={'spark','sonata','damas','tiko','nexia'}
type(cars)


# set ichidagi elementlar takrorlangan bolsa console ga chiqarmaydi faqat bittasi olib qoladi



cars={'spark','sonata','spark','damas','tiko','tiko','nexia'}
print(cars)


#!!! PRACTICE (amaliyot)


# Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. 
#Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring.


dic={
     'apple':'olma',
     'cat':'mushuk',
     'book':'kitob',
     'pencil':'qalam',
     'onion':'piyoz',
     'food':'ovqat',
     'dog':'it',
     'home':'uy',
     'school':'maktab'
     }
for key ,val in sorted(dic.items()):
    print(f" {key.title()} : {val.title()}")


# Davlatlar va ularning poytaxtlari lug'atini tuzing.
# Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring.

countries={
    'uzbekistan':'tashkent',
    'korea':'seoul',
    'france':'paris',
    'china':'pekin',
    'usa':"washington"
    }

for item in sorted(countries.keys()):
    print(item.title())

for item in sorted (countries.values()):
    print(item.title())

# Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring.
# Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.


name=input('write any country name  : ')

if name in countries:
    print(f'{name}- ning poytaxti {countries[name]}:')
else:
    print(f"{name} davlatlar royhatida topilmadi")
    





# Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). 
#Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, 
#agar taom menuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.

menu={
      'osh':12000,
      'shashlik':20000,
      'shorva':10000,
      'dimlama':9000,
      'somsa':5000,
      'mastava':8000,
      'norin':11000,
      'tandir':20000,
      'non':2000,
      'spagetti':13000
      }


soni=int(input('nechta ovqat zakaz berasiz :'))
for item in range(soni):
    name=input(f"{item+1}-ovqat :")
    if name in menu:
       
        
        print(f'{name} ning narxi {menu[name]}' )
    else:
        print(f"{name} menu da topilmadi" )














