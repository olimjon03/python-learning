#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 21:58:11 2025

@author: tojiboevolimjon
"""

#!!! "nesting" bir funksiyalar (list,dictionary.etc)  ichida boshqa funfsiyalarni saqlash.

car1={
      'model':'spark',
      'year':2025,
      'km':1000,
      'color':'white',
      "cost":2000,
      'type':'mechanic'
      }

car2={
      'model':'sonata',
      'year':2020,
      'km':50000,
      'color':'black',
      "cost":3000,
      'type':'avtomat'
      }

car3={
      'model':'damas',
      'year':2018,
      'km':80000,
      'color':'white',
      "cost":1800,
      'type':'machanic'
      }

car4={
      'model':'hyundai',
      'year':2024,
      'km':8000,
      'color':'gray',
      "cost":4000,
      'type':'avtomat'
      }

car=car2

print(f"{car['model'].title()},"
      f"{car['year']}year,"
      f"{car['color']} color,")

car=car3

print(f"{car['model'].title()},"
      f"{car['year']}year,"
      f"{car['color']} color,")


car=car4

print(f"{car['model'].title()},"
      f"{car['year']}year,"
      f"{car['color']} color,")

#!!!yuqoridagi uzun kodlarni qisqartirish.

cars=[car1,car2,car3,car4]
for car in cars:
    print(f"{car['model'].title()},"
          f"{car['year']}year,"
          f"{car['color']} color,")

#!!!yuqoridagi kod ichidagi elementlarni alohida  chiqarish.

cars[0]['model']
cars[2]['color']

#!!! yuqoridagidek malumotlarni bosh royhatga qoshish.

sparks=[]
for item in range(10):
    newcars={
          'model':'spark',
          'year':2025,
          'km':0,
          'color':None,# rangi noaniq 
          "cost":None,
          'type':'mechanic'
          }
    sparks.append(newcars)


print(sparks)


# shu 10 ta royhatdagi har bir elementlarni ozgartirish

for item in sparks[:3]:
    item['color']='red'


for item in sparks[5:11]:
    item['color']='red'

for item in sparks[5:11]:
    item['type']='avtomat'

for item in sparks:
    if item['type']=='avtomat':
        item['cost']=4000
    else:
        item['cost']=3000
        
#!!! Lists in dictionary (lugat ichida royhat)        

coders={
        'ali':['python','c++','java'],
        'jhon':['html','css','js'],
        'alex':['php','sql','c#'],
        'david':['java','python','html']
        }

print(coders)

#yuqorudagi kodga key va uni qiymatlarini chiqarish

for name,code in coders.items():
    print(f"{name.title()} : quyidagi dasturlash tillarni biladi") 
    for cod1 in  code:
        print(cod1.upper())



#!!!dictionary,list in dictionary (lugat ichiga lugat,list kiritish) majbur bolmasa ishlatish shart emas

infor={
       'ali':{'name':'tojiboev',
              'age':23,
              'live':'uzb',
              'study':'tashme',
              'code':['python','java','html']
              },
       'husan':{'name':'ergashev',
                'live':'russia',
                'age':23,
                'study':'mosk',
                'code':['python','java','html']
                },
       'jhon':{'name':'mister',
              'age':25,
              'live':'korea',
              'study':'chonnam',
              'code':['python','java','html']}
       }


for name,info in infor.items():
    print(f"{name.title()} ning familyasi : {info['name'].title()}")
    print(f"{info['live'].title()} da yashaydi")
    print(f"yoshi : {info['age']}")



#!!! PRACTICE  (amaliyot)

#1 Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi ma'lumotlarni lug'at ko'rinishida saqlang. 
#Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.

a_navoiy={
    'ismi':'a navoiy',
    'b.year':1441,
    'kim':'shoir',
    'd.year':1501
    }

a_temur={
    'ismi':' a temur',
    'b.year':1336,
    'kim':'sarkarda',
    'd.year':1405
    }
z_bobur={
    'ismi':'zbobur',
     'b.year':1483,
     'kim':'sarkarda,shoir',
     'd.year':1530
     }
ibn_sino={
    'ismi':'ibn sino',
     'b.year':980,
     'kim':'tabib',
     'd.year':1037
     }
shaxslar=[a_navoiy,a_temur,z_bobur,ibn_sino]
for item  in shaxslar:
    print(f"{item['ismi'].title()} :")
    print(f"{item['b.year']} da tugulgan")
    print(f"{item['kim']} ")
    print(f"{item['d.year']} da vafot etgan")





#2.Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing.
# For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.


a_navoiy={
    'ismi':'a navoiy',
    'b.year':1441,
    'kim':'shoir',
    'd.year':1501,
    'asarlar':['laylatul abror','farhod ca shirin']
    }

a_temur={
    'ismi':' a temur',
    'b.year':1336,
    'kim':'sarkarda',
    'd.year':1405,
    'asarlar':['temuriylar','temur tuzuklari']
    }
z_bobur={
    'ismi':'zbobur',
     'b.year':1483,
     'kim':'sarkarda,shoir',
     'd.year':1530,
     'asarlar':['boburnoma','devon']
     }
ibn_sino={
    'ismi':'ibn sino',
     'b.year':980,
     'kim':'tabib',
     'd.year':1037,
     'asarlar':['tib qonunlari','najot']
     }


shaxslar=[a_navoiy,a_temur,z_bobur,ibn_sino]

for shaxs in shaxslar:
    print(f"{shaxs['ismi'].title()} ning asarlari:\n"
          f"{shaxs['asarlar']}")
          










#3. Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang. 
#Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida lug'artga saqlang. Natijani konsolga chiqaring.


friends_cinema={
    'ali':['ujas','squid games','darkess'],
    'husan':['zombie','wrong turn','darkess'],
    'vali':['chegara','wrong turn','darkess'],
    }

print(friends_cinema)










#4.Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida ma'lumotlarni lug'at ko'rinishida saqlang.
# Har bir davlat haqida ma'lumotni konsolga chiqaring.





countries={
    'uzb':{'population':"37mln",
           'langugae':'uzbek',
           'location':'asia',
           'capital':'tashkent'},
    "usa":{'population':"100mln",
           'langugae':'english',
           'location':'amira',
           'capital':'washington'},
    "korea":{'population':"50mln",
           'langugae':'korean',
           'location':'asia',
           'capital':'seul'}
    }

countries

for a,b in countries.items():
    print(f"{a.title()} haqida malumot:\n"
          f"{b}")



#5. Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, 
#foydalanuvchi so'ragan davlat haqida ma'lumot bering.
# Agar davlat sizning lug'atingizda mavjud bo'lmasa, "Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.

countries={
    'uzb':{'population':"37mln",
           'langugae':'uzbek',
           'location':'asia',
           'capital':'tashkent'},
    "usa":{'population':"100mln",
           'langugae':'english',
           'location':'amira',
           'capital':'washington'},
    "korea":{'population':"50mln",
           'langugae':'korean',
           'location':'asia',
           'capital':'seul'}
    }


user=input('davlat nomini kiriting : ')

for name,info in countries.items():
    if user in name:
        print(f"{name.title()} haqida malumot:\n"
              f"{info}")
    else:
        print('bunday davlat royhatdan topilmadi')

        
    




















  