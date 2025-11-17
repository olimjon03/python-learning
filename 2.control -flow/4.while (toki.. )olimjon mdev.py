#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 15 06:09:02 2025

@author: tojiboevolimjon
"""

#input (mustahkamlash)
ism = input('what\'s your name?:')
savol=(f'salom ,{ism.title()} . how old are you?' )
age =input(savol)

type(age)
age=int(age)
type(age)


#!!! 'while ' (toki.../ shart bajarilguncha davom etadi)

son=1 #songa 1 qiymatini beramiz
while son<=5:# toki son 5 kichik yoki teng ekan..
    print(son)# sonni konsolga chiqaramiz
    son=son+1 #songa 1 qoshamiz
    #son+=1 #yuqoridagi son=son+1 bilan bir hil

print('dastur tugadi')


#!!! while and input   

print ('istalgan sonni kvadrati va kubini hisoblovchi datur:\n')

savol='istalgan son kiriting :\n'
savol+='{dasturni toxtatish uchun "exit" kiriting}'
qiymat=''
while qiymat!='exit':
    qiymat=input(savol)
    
    if qiymat!='exit':
        print(float(qiymat)**2)
        
    
print('dastur tugadi')



#!!! while and True/ False

print ('istalgan sonni kvadrati va kubini hisoblovchi datur:\n')

savol='istalgan son kiriting :\n'
savol+='{dasturni toxtatish uchun "exit" kiriting}'
ishora=True
while ishora:
    qiymat=input(savol)
    if qiymat=='exit':
        ishora=False
    else:
        print(float(qiymat)**2)
        
    
print('dastur tugadi')
      
    
#!!!! break while
    
print ('istalgan sonni kvadrati va kubini hisoblovchi datur:\n')

savol='istalgan son kiriting :\n'
savol+='{dasturni toxtatish uchun "exit" kiriting}'

while True: # abadiy sikl 
    qiymat=input(savol)
    if qiymat=='exit':
        break
        
    else:
        print(float(qiymat)**2)
        
    
print('dastur tugadi')
      
#!!! break for

num=list(range(1,11))
 
for num1 in num:
    if num1==6:
        break
    print(f"{num1} ning kvadrati {num1**2} ga teng ")
    
    
#!!! continue for    
    
num=list(range(1,11))
 
for num1 in num:
    if num1==6:
        continue #bunda num1 6 ga teng bolgani uchun 6 ni tashlab davom etadi.
    print(f"{num1} ning kvadrati {num1**2} ga teng ")   
    
    
#!!!! continue while   
    
number=0
while number <10:
    number+=1
    if number%2==0:
        continue
    else:
        print(number)
        
        
        
        
        
        
        
        
    
#!!!PRACTICE (amaliyot)

#Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang.
# Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating

book=input('yaxshi korgan kitoblarizni yozing:')
kitob=True
while kitob:
    
    book=input('yaxshi korgan kitoblarizni yozing:')
    if book=='stop':
        kitob=False
    else:
        print(book)
print('dastur tugadi')


   


# Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 
 #7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm,
# 65 dan kattalarga bepul. Shunday while tsikl yozingki, 
#dastur foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin.
# Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).




savol="how old are you ? :"

while True:
    qiymat1=input(savol)
    if  qiymat1=='exit' or qiymat1=='quit':
        print('dastur tugadi')             
        break
        
    age=int(qiymat1)
    
    
    if age<7:
        print('chipta narxi:',2000,'so\'m')
    elif  age<18:
        print('chipta narxi:',3000,'so\'m')
    elif  age<65:
        print('chipta narxi:',10000,'so\'m')
    elif  age>65:
        print('siz uchun bepul')
    
        
    

    
# Quyidagi dasturda bir nechta mantiqiy xatolar bor.
# Jumladan, xusisiy holatlarda tsikl abadiy qaytarilib qolmoqda. Xatolarni to'g'rilay olasizmi?
    
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = int(input(savol))
    if qiymat=='Exit':
        break
    elif float(qiymat)<0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    