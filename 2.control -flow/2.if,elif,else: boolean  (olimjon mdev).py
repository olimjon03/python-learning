#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  8 15:43:07 2025

@author: tojiboevolimjon
"""
#!!!  " if / elif /else "
num=-30
if num<0:
    print('manfiy son')
else:
    print ('musbat son')

ogirlik=int(input('siz necha kg siz?\n>>>'))
age = int(input('sizning yoshingiz nechi?'))
if ogirlik>=50:
    print('no mumkinmas')
elif ogirlik>=40:
     print('yaxshi')
    
else:
    print('welcome')

yosh=int(input ('yoshingizni kiriting\n>>>'))
if yosh<=4:
    print('siz uchun kirish bepul')
elif yosh<=12:
    print('siz uchun kirish 2000 som')

elif yosh<=18:
    print('siz uchun kirish 4000')
else:
    print('siz uchun 6000 som')
    
age = int(input ('how old are you?\n>>>'))
cost=0
if age<=4:
    cost=0
elif age<=12:
    cost=3000
elif age<=18:
    cost=5000
else:
    cost<=7000
print(f'siz uchun kirish narhi : {cost} sum')


#!!! OR \ AND

day=input('what day is today ?\n>>>')
if day.lower()=='friday' or day.lower()=='sunday' or day.lower()=='saturday':
    print(f" bugun {day.title()}  dam olish kuni")
else : 
    
    print(f'bugun {day.title()} ish kuni')

age=int(input('yoshingizni yozing\n>>>'))
davlat=input('davlatingizni yozing\n>>>')
if davlat=='uzbek'or davlat.lower()=='usa' and age>=18:
    print('siz uchun mumkin')
elif davlat=='korea' and age>=19:
    print('siz uchun mumkin')
else :
    print('siz uchun mumkinmas')

#!!!BOOLEAN

cost=5000 # cafe 5000 songa toam oldi
suv=True # qoshimcha suv oldi
non=False # non olmadi 

if suv and non:
    cost=cost+2000
elif suv or non:
    cost=cost+1000
print(f'jami narh : {cost}')




cost=5000 # cafe 5000 songa toam oldi
suv=True # qoshimcha suv oldi
non=True # non olmadi 

if suv and non:
    cost=cost+2000
elif suv or non:
    cost=cost+1000
print(f'jami narh : {cost}')

#!!! IN

numbers=[1,2,3,4,5,6,7,8,9,10]
12 in numbers
9 in numbers

menu=['osh','kabob','mastava','chuchvara','somsa']
ovqat=input('nima buyurasiz\n...')
if ovqat.lower() in menu:
    print(f'{ovqat.title()}ka buyurtmasi qabul qilindi')
else:
    print(f'{ovqat.title()} menuda  yoq!!')

#!!! NOT IN

numbers=[1,2,3,4,5,6,7,8,9,10]
12 not in numbers
9 in numbers



#!!!menudan buyurtma berilgan ovqatlar bor yoqligini tekshirish:
    
menu=['osh','somsa','manti','dimlama','kebab','shorva']
buyurtmalar=['somsa','osh','non']
for ovqat in buyurtmalar:
    if ovqat in menu:
        print(f" menuda {ovqat} bor")
    else:
        print(f"menuda {ovqat} yoq")


#!!! royhat bosh yoki boshmasligini tekshirish

menu=['osh','somsa','manti','dimlama','kebab','shorva']
buyurtmalar=['somsa','osh','non']

if buyurtmalar:
    print(f'royhatda  {len(buyurtmalar)} ta ovqat bor')

 #!!!  Practice  (AMALIYOT) !!!

#1.Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
 
son=int(input('juft son kiriting\n...'))
if son%2==0:
    print('bu juft son')
else:
    print(' bu juft son emas')

#2.Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
#Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
#Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
#Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm



age=int(input('yoshingizni kiriting\n...'))
narx=0
if age<=4 or age>=60:
    narx=('bepul')
elif age<=18:
    narx=10000 
elif age>=18:
    narx= 20000
print(f'siz uchun  :{narx}')


#3.Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring



son=int(input('ikkita son kiriting \n birinchi son ...'))
son1=int(input('ikkinchi son...'))
if son==son1:
    print('bu son teng')
else:
    print('bu son teng emas ')

#!!!4.mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting.
#Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. 
#Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.

products=['non','qaymoq','sut','suv','pepsi','kola','gosht','muzqaymoq','kofe']
savat=[]
savat2=[]

print('beshta mahsulot kiriting')
for n in range(1,6):
    product=input(f' {n} -')
    savat.append(product)
    if product in products:
        
        print(f'{savat} dokonda bor')
    else:
        savat.remove(product)
        savat2.append(product)
        print(f'{savat2} dokonda yoq')
   
print(f'{savat} dokonda bor')
print(f'{savat2} dokonda yoq')       


#!!!5.foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. 
#Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.

users=['olimjon','ali','abror','jhon','alex']
login=input('yangi login kiriting:')
if login.lower() not in users:
    print(f'welcome,new user :{login.title()}')
else:
    print('login is busy sorry')

#!!!6.Foydalanuvchidan biror butun son kiritishni so'rang. 
#Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.


num=int(input('istalgan son kiriting:'))
for n in range(1,10):
    
    if not(num%n):
        
        print(f'{num} soni {n}ga qoldiqsiz bolinadi')
        


    


