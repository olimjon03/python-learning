#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 27 02:05:03 2025

@author: tojiboevolimjon
"""


#!!!obyekt class ga qoshimcha harakter qoshish.


class Student:
    """tudentlar haqida malumot olish"""
    def __init__(self,name,surname,age):
        self.name=name
        self.surname=surname
        self.age=age
        self.level=2 #qoshimcha harakter
    def get_info(self) :
        return f" name :{self.name} surname:{self.surname}"
    
    #qoshimcha harakterni ozgartirish.
    
    def set_level(self,new_level):# 1 usuli
        self.level=new_level
        
    def update_level(self):#2 usuli har yangilanganda 1 qoshadi 
        self.level+=1
        
     #agar har bir hususiyat haqida alohida malumot olmoqchi bolsak har biridan metod yasagan afzal boladi!!!
     # bunday qilishga sabab metodlarni ozgartirish oson boladi  
    def get_name(self):
         return self.name
    def get_surname(self):
         return self.surname
    def get_age(self):
         return self.age


student1=Student('olimjon','tojiboev',23) #1 usul
student1.set_level(3)

student1.get_info()

student1.update_level() #2 usul

student1.get_info()






class Course():
    def __init__(self,subject):
        self.subject=subject
        self.students_num=0
        self.students=[]
        
        
        
    def add_student(self,student):#coursega student qoshish
        """add students to course"""
        self.students.append(student)
        self.students_num+=1
        
        
        
    #har bir talabadan malumot olib royhatga joylash
    def get_students(self):
        return[x.get_info() for x in self.students]
        
        



math=Course('Mathematic')

#studentlar

student1=Student('olimjon','tojiboev',23)
student2=Student('ali','tojiboev',24)
student3=Student("olimjon","tojiboev",23)
student4=Student("ali","ergashev",33)
student5=Student("hasan","tojiddinov",29)

#studentlarni qoshish

math.add_student(student2)
math.add_student(student3)
math.add_student(student4)




math.students_num
math.get_students()


#!!! class  ichidagi metodlarni tekshirish
#class ichidagi metodlarni " dir " orqali tekshiriladi
dir(Student)

#ortiqcha metodlarni ochirish

def see_methods(klass):
    return[method for method in dir(klass) if not method.startswith('__')]

see_methods(Course)

see_methods(Student)
  

#!!!PRACTICE (amaliyot)
# 1.Avto degan yangi klass yarating. Unga avtomobillarga doir bo'lgan bir nechta xususiyatlar 
#(model, rang, korobka, narh va hokazo) qo'shing. Ayrim xususiyatlarga standart qiymat bering (masalan, kilometer=0)

# 2.Avto ga oid obyektning xususiyatlarini qaytaradigan metodlar yozing
# get_info() metodi avto haqida to'liq ma'lumotni matn ko'rinishida qaytarsin

class Avto():
    def __init__(self,model,color,cost,year):
        self.model=model
        self.color=color
        self.cost=0
        self.year=year
        self.km=0
        
        
#2.Avto ga oid obyektning xususiyatlarini qaytaradigan metodlar yozing
# get_info() metodi avto haqida to'liq ma'lumotni matn ko'rinishida qaytarsin 

       
    def get_newinfo(self):
        return f"model;{self.model} cost:{self.cost} color: {self.color} year:{self.year} ,km:{self.km}"
    
# 3..Avto ga oid obyektning xususiyatlarini yangilaydigan metodlar yozing.
# update_km() metodi son qabul qilib olib, avtomobilning yurgan kilometrajini yangilab borsin
    def update_km(self,new_km):
        self.km+=new_km
    

# 4.Yangi, Avtosalon degan klass yarating va kerakli xususiyatlar bilan to'ldiring 
#(salon nomi, manzili, sotuvdagi avtomobillar va hokazo)

class AvtoSalon():
    def __init__(self,company_name,address):
        self.name=company_name
        self.address=address
        self.newcars=[]
        


# 5.Avtosalonga yangi avtomobillar qo'shish uchun metod yozing
    def add_cars(self,car):
        self.newcars.append(car)
        
        
# 6.Avtosalondagi avtomobillar haqida ma'lumot qaytaruvchi metod yozing

    def get_carinfo(self):
        return[a.get_newinfo() for a in self.newcars]




# 7.Yuqoridagi obyektlar va ularga tegishli metodlarni tekshirib ko'ring

kia=AvtoSalon("kia",'korea',)

car1=Avto('Kia','red',20000,2025)
car1.update_km(20000)
kia.add_cars(car1)
kia.get_carinfo()

# 8.dir() funksyasi va __dict__ metodi yordamida o'zingiz yozgan va 
#Pythondagi turli klass va obyektlarning xususiyatlari va metodlarini toping (dir(str), dir(int) va hokazo)

dir(AvtoSalon)
dir(Avto)

















