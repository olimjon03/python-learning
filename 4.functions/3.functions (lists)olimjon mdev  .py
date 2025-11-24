#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 21 01:51:09 2025

@author: tojiboevolimjon
"""

 #!!!function /lists
 
def grade(students):
    infostudents={}
    while students:
        name=students.pop()
        baho=input(f'pls,grade the student  {name.title()}:')
        infostudents[name]=int(baho)
    return infostudents
        

students=['ali','olimjon','husan','hasan','abror']
info=grade(students)# bunda funksiya list (royhat)ni ozida foydalanadi va qayta ishlatganda royhat bosh boladi


print(info)

#royhatdan nusxa olish uchun

info=grade(students[:])
 
 
print(info)



#!!!PRACTICE(amalliyot)


#1. Matnlardan iborat ro'yxat qabul qilib, 
#ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgatiruvchi funksiya yozing.

def text(royhat):
    """royhatdagi matni kattta harf bilan yozib beruvchi funcsiya"""
    newtext=[]
    for matn in royhat:
        
        newtext.append(matn.title())
        
        
        
    return newtext




royhat=['hello my name is olimjon','good morning','good afternoon']

mant=text(royhat[:])   
        
    
    







#2. Yuqoridagi funksiyani asl ro'yxatni o'zgartirmaydigan
# va yangi ro'yxat qaytaradigan qilib o'zgartiring

def text(royhat):
    """royhatdagi matni kattta harf bilan yozib beruvchi funcsiya"""
    newtext=[]
    for matn in royhat:
        
        newtext.append(matn)
        
        
        
    return newtext




royhat=['hello my name is olimjon','good morning','good afternoon']

mant=text(royhat[:])   











#3. Darsimiz davomida yozgan bahola funksiyasini .pop() metodidan foydalanmasdan 
#va asl ro'yxatga o'zgartirish kiritmasdan faqat lug'at qaytaradigan qilib yozing.
 
 
 
 
def grade(students):
    infostudents={}
    for matn in students:
        name=matn
        baho=input(f'pls,grade the student  {name.title()}:')
        infostudents[name]=int(baho)
    return infostudents
        

students=['ali','olimjon','husan','hasan','abror']

info=grade(students[:])
 
 
print(info)

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 