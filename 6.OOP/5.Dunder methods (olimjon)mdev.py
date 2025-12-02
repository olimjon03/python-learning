#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 02:43:36 2025

@author: tojiboevolimjon
"""


class Avto :
    """avtomobil klassi"""
    #bu ozgaruvchilar faqat klassga tegishli boladi
    
    
    def __init__(self,company,model,color,year,cost,km=0):
        self.company=company
        self.model =model
        self.color=color
        self.year=year
        self.cost=cost
        #inkapsulatsiya qilish
        self.km=km
        #bunda classga kiritilgan obyekt malumotlarni hisoblaydi
        
        
        
        #!!!!1. obyektni print qilganda biror malumot chiqarish
        
    def __str__(self):
        return f"Avto : {self.model} ,{self.company}" 
    
    def __repr__(self):#__str__ bilan bir hil lekin kop funksiyalar bilan ishlay oladi
        return f"Avto : {self.model} ,{self.company}" 
    
    
    #!!!2. obyektlarni taqqoslash
    def __eq__(self,x): #taqqoslash == :
        return self.cost==x.cost
    
    
    def __lt__(self,x):# kichikligini taqqoslash X<Y
    
        return self.km<x.km
    
    
    def __le__(self,x):# kichik yoki tengligini taqqoslash X<=Y
    
        return self.cost<x.cost
    
   
    
    
    





avto1=Avto('kia','morning','black',2010,2000,90000)
avto2=Avto('hyundai','sonata','white',2018,2000,8000)
avto3=Avto('mers','class500','black',2024,8000,2000)


#!!!1. obyektni print qilganda biror malumot chiqarish

print(avto1)
print(avto2)

str(avto1)
repr(avto1)

#!!!2. obyektlarni taqqoslash

avto1==avto3

avto1==avto2

# kichikligini taqqoslash X<Y
avto1<avto2
avto3<avto1
# kichik yoki tengligini taqqoslash X<=Y
avto1<=avto2




 #!!!#3.obyekt uzunligini olchash.
 
class AvtoSalon:
    def __init__(self,name):
        self.name=name
        self.avtos=[]
        
    def __repr__(self):
        return f"{self.name} avtocompany."
    
    #!!! royhat uzunligini olchash
    
    def __len__(self):
        return len(self.avtos)
    
    
    def __getitem__(self,index):#!!!royhatdagi indexlarni qaytaradi
        return self.avtos[index]
    
    def __setitem__(self,index,change_item): #!!!royhatdagi indexlarni almashtiradi
        self.avtos[index]= change_item
        
        
    #!!! parametrlarsiz chaqirish
    
    def __call__(self):
        return [avto for avto in self.avtos]
    
    
    
     
    def add_avto(self,*qiymat):
        # !!isinstance object classga tegishli ekanini tekshiradi
        for avto in qiymat:
            if isinstance (avto,Avto):
                self.avtos.append(avto)
            else:
                print('you can add only avto group')
            
            
avto1=Avto('kia','morning','black',2010,2000,90000)
avto2=Avto('hyundai','sonata','white',2018,2000,8000)
avto3=Avto('mers','class500','black',2024,8000,2000)     
        
salon1=AvtoSalon('Hyundai')
salon1.add_avto(avto1,avto2,avto3)


#royhatdagi indexlarni qaytarish

salon1[0]
salon1[:]


#royhatdagi indexlarni almashtirish
salon1[1]=Avto('bmw',"x8",'black',2025,9000,1000)
len(salon1)


#parametrlarsiz chaqirish

salon2=AvtoSalon('maxauto')
salon2.add_avto(avto1,avto2,avto3)


salon2()




#!!!PRAcTICE(amaliyot)

# 1.Avvalga darslarda yaratilgan obyektlarga (Shaxs, Talaba) turli dunder metodlarni qo'shishni mashq qiling.
# Obyekt haqida ma'lumot (__rerp__)
# Talabalarni bosqichi bo'yicha solishtirish (__lt__, __eg__ va hokazo)
from uuid import uuid4


class Student:
    """student classi"""
    def __init__(self,name,surname,passport,level):
        self.name=name
        self.surname=surname
        self.passport=passport
        self.id_number=uuid4
        self.level=level
        
        #obyekt haqida malumot
    def __repr__(self):
        return f" student name :{self.name} , surname:{self.surname}"
    
    def __lt__(self,student_level):
        return self.level<student_level.level
    
student1 = Student('olimjon','tojiboev','fa12344566',4)
student2 = Student('li','kim','fa12344566',2)
student3 = Student('son','min','fa1232466',3)
student4=Student('ronaldo','cristiano','fa1232466',1)
student1>student2
        
# 2.Fan degan yangi klass yarating. Fan obyetklari tarkibida shu fanga yozilgan talabalarning ro'yxati saqlansin. Buning uchun Fanga add_student(), __getitem__, __setitem__, __len__ kabi metodlarni qo'shing.

class Subject:
    """fanlar uchun class"""
    def __init__(self,name):
        self.name=name.title()
        self.students=[]
    
    def add_student(self,*students):
        for student in students:
            if isinstance(student,Student):
                self.students.append(student)
            else:
                print('add only students list')
            
        
    def __getitem__(self,index):
        return self.students[index]
    def __setitem__(self,index,student):
        self.students[index]=student
    def __len__(self):
        return len(self.students)
    
    # 3.Fanga qo'shish + operatori yordamida talaba qo'shish metodini yozing
    
    def __add__(self,student):
        
        self.students.append(student)
        return self
    
    # 4.Minus (-) operatori yordamida fandan talaba olib tashlash metodini yozing 
    #(bunda talabaning passport raqami yoki ID raqami bo'yicha topib, olib tashlash mumkin)
    def __sub__(self,student):
        
            
        self.students.remove(student)
            
                
        
        
        
math1=Subject('mathematic')
math1.add_student(student1,student2,student3)
math1.students
math1+student4
math1.students
math1-student4
math1[:]



#5

class Point:
    def __init__(self,x1,y1):
        self.x1=x1
        self.y1=y1
    def __repr__(self):
        return f" {self.x1},{self.y1}"
    
    
    def __add__(self,other):
        return Point(self.x1+other.x1,self.y1+other.y1)
    def __sub__(self,other):
        return Point(self.x1-other.x1,self.y1-other.y1)

v1=Point(10,20)
v2=Point(10,20)

print(v1+v2)
print(v1-v2)
print(v1,v2)

#6

class Student ():
    def __init__(self,name,id_num,gpa):
        self.name=name
        self.id_num=id_num
        self.gpa=gpa
        
    def __repr__(self):
        return f"name :{self.name} id_num :{self.id_num}"
    def __lt__(self,student):
        return self.gpa < student.gpa

student1 =Student('ali',232343,4)

student2 =Student('ali',232233,3)

student1>student2

#7
class Group():
    def __init__(self,name):
        self.name=name
        self.studentss=[]
    def __repr__(self):
        return f" leaders : {self.studentss}"
    def __add__(self,student):
         self.studentss.append(student)
         return self
    
    def __sub__(self,name):
        for student in self.studentss:
            if student.name==name:
                self.studentss.remove(student)
                return self
        print('bunday ism topilmadi')
        return self
        
    def __len__(self):
        return len(self.studentss)
    def __contains__(self,student):
        return student in self.studentss

    

gr1=Group('leaders')
gr1
gr1+student1
gr1-'ali'
gr1-'vali'

    



















