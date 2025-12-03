#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 22:35:07 2025

@author: tojiboevolimjon
"""

#!!! fileni ochib yopish

file =open('/Users/tojiboevolimjon/Downloads/mynewfile.txt')
PI=file.read()
print(PI)
file.close()


#!!! fileni xavfsiz usulda ochish


with open ('/Users/tojiboevolimjon/Downloads/mynewfile.txt') as file:
    PI=file.read()
    

print(PI)



type(PI)
 
PI=PI.rstrip()
PI=PI.replace('\n','')
PI


#!!!file ichidagi matnlarni har bir qatorini alohida qilib chiqarish
filename='/Users/tojiboevolimjon/Downloads/mynewfile.txt'

with open (filename) as file:
    for line in file:
        print(line)
    


#!!! textlarni royhatga joylash


with open (filename) as file:
    newtext=file.readlines()
    print(newtext)

newtext=[text.rstrip() for text in newtext]

print (newtext)
    
#!!! filega yangi matn yozish

newfile='/Users/tojiboevolimjon/Downloads/newfile2.txt'
name="olimjon Tojiboev"
year=2003

#!!! bunda agar file mavjud bolsa ochadi va yangi file yoziladi

with open (newfile,'w') as file2: 
    file2.write(name.title()+'\n') # file matnlarni faqat bir qatorga yozgani uchun \n ishlatilgan
    file2.write(str(year)+'\n') # file matnlarni faqat str da qabul qilgani uchun int da str otqazish kerak
    
       
   
    


with open (newfile,'r') as rfile:
    rd=rfile.read()
    print(rd)

#!!! yozilgan filega matn qoshish
# 'a'- append

with open (newfile,'a') as file:
    file.write('Hello'+'\n')
    file.write('good morning '+'\n')


with open (newfile,'r') as rfile:
    rd=rfile.read()
    print(rd)

#!!!o'zgaruvchilarni matnga saqlash list ,dictionary


student1={'name':'olimjon','age':23,'country':'uzbek'}
student2={'name':'ali','age':27,'country':'uzbek'}

import pickle #1. modulni chaqirib olinadi



#'wb' - write binary

with open (newfile,'wb') as file:
    pickle.dump(student1,file)
    pickle.dump(student2,file)#pickle.dump() → obyektni faylga saqlaydi


with open (newfile,'rb') as file:
    data1=pickle.load(file)
    data2=pickle.load(file)#pickle.load() → obyektni fayldan o‘qiydi
    print(data1)
    print(data2)


#!!! PRACTICE (amaliyot)
# 1. Sizning tug'ilgan kuningiz  𝜋  soni tarkibida uchraydimi yoki 
#yo'q ekanligini aniqlovchi funksiya yozing. Misol uchun, tug'ilgan 
#sanangiz 25 Fevral, 2000-yil bo'lsa, 25022000 ketma-ketligi yuqoridagi 
#matnda uchraydimi yo'q toping.

pifile='/Users/tojiboevolimjon/Downloads/pimln.txt'
with open (pifile ,'r') as file :
    rdfile=str(file.read().strip())
    num='03'
    if num in rdfile:
        print(f"we found the number : {num}")
    else:
        print('error')




# 2.Foydalanuvchidan turli hil ma'lumotlarni so'rab, har bir kiritilgan 
#ma'lumotni yangi qatordan faylga yozib boruvchi dastur tuzing.
# Dastur qayta chaqirilganida yangi ma'lumotlar fayl oxiridan qo'shilib borsin (yangi faylga emas).      




newfile='/Users/tojiboevolimjon/Downloads/mynewfile.txt'
def addtxt(newfile):
    """malumotlarni filega qoshuvchi funksiya"""
    text=input('please write your text :')
    with open(newfile,'a') as file:
        file.write(text + '\n')
    with open (newfile,'r') as file:
        return file.read()
        
    
print(addtxt(newfile))  
    

    


    
   










