#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 21 03:23:49 2025

@author: tojiboevolimjon
"""

#!!! "*args"(arguments)

#fuksiya ichiga istalgancha argument qo'shish imkonini beradi.


def summa(*numbers):#bunda numbers tuple() holatda boladi yani ozgarmas royhat 
    """sonlar yigindisini hisoblaydigan function"""
    yigindi=0
    for num in numbers:
        yigindi+=num
        
    return yigindi


summa(2,3,4,5,6,7)#bunda user numbers yani tuple()ga qiymat kiritadi
result=summa(2,3,4,56,6,7,)
print(result)


###yuqoridagi kodni yaxshiroq varianti

def summa(*numbers):
    return sum(numbers)

summa (3,3,3)


#majburiy argument kiritish


def summa(a,b,*numbers):#bunda *args ni oxiriga qoyish kerak va majburiy argumetnlarni ham kiritish shart
    return sum(numbers)

summa ('hello','olimjon',1,2,3,4,5,6,7,8,9)

#!!! **kwargs(keyword arguments)

#!bunda funksiyaga key and words berishimiz kerak yani kalit soz va uning qiymati.
#**kwargs bilan funksiya ishlashi :user key and word kiritadi va bundan **kwargs(**lugat) lugat yaratadi.



def info(**kwargs):
    for key,words in kwargs.items():
        print(f"{key} : {words}")
        
info(name='olimjon',age=26,hobby='chess')


#!!! majburiy argumentlar qoshish.
#
def car_info(company,model,**info):
    info['companiya']=company
    info['modeli']=model
    return info
    
car1=car_info('mersedes','class500',color='red',year=2025)      
car2=car_info('hyudai','sonata',color='black',cost=2000,year=2010)


print(car1)
print(car2)


#PRACTICE(amaliyot)

#1.Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing
def cal_num(*number):
    numb=1
    for num in number:
        numb*=num
        
    return numb

cal_num(2,3,4)




#2.Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing.
# Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.

def students_info(name,surname,**information):
    information['ismi']=name.title()
    information['familiyasi']=surname.title()
    return information

student1=students_info('olimjon','tojiboev',age=20,school='chonnam')
print(student1)  
    


































