#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 06:03:25 2025

@author: tojiboevolimjon
"""
#!!!"return" funksiya ichidagi argument qiymatiini qaytaradi.

def full_name(name,surname):
    """fullname function"""
    name=f"{name} {surname}"
    return name

person=full_name('olimjon','tojiboev')
print(person)


#!!! yuqoridagi kod uchun print ishlatsak qanday boladi.
def full_name(name,surname):
    """fullname function"""
    print(f"{name} {surname}")
    

person=full_name('olimjon','tojiboev')
print(person)# natija "None "chiqadi yani funksiya argument nomini ozgartirganda None chiqaradi return ishlatmasa




#!!!"return" misollar


def full_name(name,surname):
    """fullname function"""
    name=f"{name} {surname}"
    return name

student1=full_name('olimjon','tojiboev')
student2=full_name('ali','ergashev')
student3=full_name('hasan','aliyev')

print(f"{student1} is come today\n"
      f"{student2} is  not come today\n"
      f"{student3} is come today")
      


#!!!optional argument (ixtiyoriy argument)

def full_name(name,surname,middle_name=''):#ixtiyoriy argument yaratish uchun argumentni biror qiymatga tenglab qoyish kerak.

    """fullname function"""
    if middle_name:
        name=f"ismi :{name}\n surname :{surname}  \n middle name : {middle_name}"
    else:
        name=f"ismi :{name}\n surname :{surname} "
        
    return name.title()

person1=full_name('olimjon', 'tojiboev ', 'mahkamboy ugli')
person2=full_name('ali', 'ergashev ')

print(person1,person2)


#!!!!return with dictionary.

def cars(model,name,color,year,cost,sale=None):
    """information about cars """
    car={'model':model,
         'name':name,
         'color':color,
         'year':year,
         'cost':cost,
         'sale':sale}
    return car

car1=cars('bmw','m4','black',2025,50000)
car2=cars('hyundai','sonata','white',2015,3000,500)
car3=cars('kia','morning','red',2010,2000,200)

print(car1)
car1['model']
car2['year']
avtos=[car1,car2,car3]

for avto in avtos:
    if avto['sale']:
        sale=avto['sale']
    else:
        sale='no discount'
    print(f"{avto['model']} {avto['cost']}$ sale:{sale} $")


      
      
#!!! "return with  range() "   .
#return orqali range() funksiyasini yasash.

def distance(min,max):
    """range vazifasini bajaruvchi funksiya"""
    num=[]
    while min<max:
      num.append(min)
      min+=1
    return num
      
      
print(distance(0,10))      
print(distance(12,20))     
      
#!!!adding range step  (by myself)   



def distance(min,max,step=1):
    """range  step vazifasini bajaruvchi funksiya"""
    num=[]
    if step:
        while min<max:
          num.append(min)
          min+=step
    else:
        min+=1
        
    return num
          
        
print(distance(2,50,4))    
       

#!!!funksiya orqali listga malumotlar qoshish.


def cars(model,name,color,year,cost,sale=None):
    """information about cars """
    car={'model':model,
         'name':name,
         'color':color,
         'year':year,
         'cost':cost,
         'sale':sale}
    return car

print('avto companiyadagi avtolar royhatini tuzish!!')

avtolar=[]
while True:
    print('quyidagi malumotlarni kiriting ')
    model=input('moshina modeli:')
    name=input('moshina nomi:')
    color=input('moshina rangi:')
    year=input('moshina yili:')
    sale=input('moshina chegirmasi:')
    cost=input('moshina narxi:')
    stop=input('boshqa royhat tuzasimi:yes/no')
    avtolar.append(cars(model,name,color,year,cost,sale))
    if stop=='no':
        break
print('avtolar royhati:')
for avto in avtos:
    if avto['sale']:
        sale=avto['sale']
    else:
        sale='no discount'
print(f"model:{model}, year:{year} , cost :{cost}")
      
 
      
#!!!PRACTICE (amaliyot)
      

#1. Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, 
#email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya yozing.
# Lug'atda foydalanuvchu yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)

def infouser(name,surname,b_year,address,email='',phone=None):
    """user information function"""
    
    info={'ism':name,
          'familiya':surname,
          'tugulgan yil':b_year,
          'adresi':address,
          'email':email,
          'tel raqami':phone,
          'yoshi':2025-b_year
          }
    
    return info

      
    
   

user1=infouser('olimjon','tojiboev',2003,'namangan','olimjon@gmail.com')

print(user1)




# 2.Yuqoridagi funksiyani while yordamida bir necha bor chaqiring,
# va mijozlar degan ro'yxatni shakllantiring. Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring.


def infouser(name,surname,b_year,address,email=None,phone=None):
    """user information function"""
    
    info={'ism':name,
          'familiya':surname,
          'tugulgan yil':b_year,
          'adresi':address,
          'email':email,
          'tel raqami':phone,
         
          }
    
    return info

      
user1=infouser('olimjon','tojiboev',2003,'namangan','olimjon@gmail.com')

print(user1)

mijozlar=[]
print('iltimos malumotizni kiriting:')

while True:
    name=input('ismingiz:')
    surname=input('familiyangiz:')
    b_year=input('tugulgan yilingiz:')
    address=input('adresingiz:')
    email=input('emailingiz:')
    phone=input('tel raqamingiz:')
    
    mijozlar.append(infouser(name,surname,b_year,address,email=None,phone=None))
    stop=input('keyingi shaxs malumotini kiritasizmi?ha /yoq:')
    if stop=='yoq':
        break

for mijoz in mijozlar:
    if mijoz['email']:
        email=mijoz['email']
    elif mijoz['tel raqami']:
        phone=mijoz['tel raqami']
        


print(mijozlar)        
    
    







# 3.Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing

def number(x,y,z):
    """eng katta son """
    if z<y<x:
        print(x)
    elif z<x<y:
        print(y)
    elif z<x<z:
        print(z)
        
number(2,45,1)






# 4.Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini,
# diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing

def hisoblash(radius):
    """aylana radiusi,diametri ,peremetri """
    
    aylana ={
        'aylana radiusi':radius,
             'aylana diametri':2*radius,
             'aylana peremetri':2*radius*3.14,
             'aylana yuzi':3.14*radius**2
             }
    

    return aylana
















































      
      