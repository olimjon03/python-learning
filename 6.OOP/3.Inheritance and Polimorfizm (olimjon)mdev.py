#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 11:30:13 2025

@author: tojiboevolimjon
"""
#!!! "Inheritance"

# Vorislik (Inheritance)
# Ta’rif:
# Vorislik — bu bitta klassning boshqa klassdagi xususiyat va metodlarni meros qilib olishi.
# Ma’nosi:Koddan qayta foydalanishga yordam beradi va klasslar o‘rtasida ierarxiya yaratadi.
# Misol: Car klassi umumiy Vehicle klassidan voris bo‘lishi mumkin.


#object 1

class User ():
    def __init__(self,name,surname,b_year,passport):
        self.name=name.title()
        self.surname=surname
        self.b_year=b_year
        self.passport=passport
    def get_info(self):
        info=f"Full name: {self.name} {self.surname.title()}"
        info+=f" Passport {self.passport} ,bearth year :{self.b_year}"
        return info
    def get_age(self ,b_year):
        by=2025-self.b_year
        return by
        
user1=User("olimjon",'tojiboev',2003,"fa123455")        
        
user1.get_info()

user1.get_age(2003)


#!!! object1 dan meros olish 

class Student(User):
    """student classi"""
    def __init__(self,name,surname,passport,b_year,id_number,major):
        
        #super classdagi malumotlardan nusxa olish
        super().__init__(name,surname,passport,b_year)
        self.id_number=id_number
        self.major=major
    def get_id(self):
        return self.id_number
    def add_major(self):
        return self.major
    
    #polimorfizm classdagi model nomlari bir hil bolishiga aytiladi
    
    
    def get_info(self):
        info=f"Full name: {self.name} {self.surname.title()} , id number :{self.id_number}"
        info+=f" Passport {self.passport} ,bearth year :{self.b_year} , major :{self.major}"
        return info
  
    
  
    
  
student1=Student('ali','ergashev','fa385238',2003,'233222','computer')
student1.add_major()
student1.get_id()
student1.get_info()

#!!! PRACTICE (amaliyot)


# 1.Talaba klassiga yana bir, fanlar degan xususiyat qo'shing. 
#Bu xususiyat parametr sifatida uzatilmasin va obyekt yaratilganida bo'sh ro'yxatdan iborat bo'lsin (self.fanlar=[])
class Student(User):
    """student classi"""
    def __init__(self,name,surname,passport,b_year,id_number,major):
        
        #super classdagi malumotlardan nusxa olish
        super().__init__(name,surname,passport,b_year)
        self.id_number=id_number
        self.major=major
        self.subjects=[]
    def get_id(self):
        return self.id_number
    def add_major(self):
        return self.major
    
# 3.Talaba klassiga fanga_yozil() degan yangi metod yozing. 
#Bu metod parametr sifatida Fan klassiga tegishli obyektlarni qabul qilib olsin va 
#talabaning fanlar ro'yxatiga qo'shib qo'ysin.
        
    def register_subject(self,subject):
        self.subjects.append(subject)
        
# 4.Talabaning fanlari ro'yxatidan biror fanni o'chirib tashlash uchun remove_fan() metodini yozing. 
#Agar bu metodga ro'yxatda yo'q fan uzatilsa "Siz bu fanga yozilmagansiz" xabarini qaytarsin.

    def  remove_fan(self,subj) :
        
        if subj in self.subjects:
            self.subjects.remove(subj)
        else:
            
            return "siz bu fanga yozilmagansiz"
         
    
    def get_info(self):
        sub=", ".join([fan.name for fan in self.subjects])
        info=f"Full name: {self.name} {self.surname.title()} , id number :{self.id_number}"
        info+=f" Passport {self.passport} ,bearth year :{self.b_year} , major :{self.major} subject : {sub}"
        return info


#2. Fan degan yangi klass yarating va bu klassdan turli fanlar uchun alohida obyektlar yarating.
#!!! class 2

class Subject():
    """fanlar uchun class"""
    def __init__(self,name):
        self.name=name.title()
       
    def get_info(self):
        return f"fan name : {self.name}  "


math=Subject('mathematic1',)
eng=Subject('english ',)
ai=Subject('Artificial Intelligence')
math.get_info()

student2=Student('husan','husanov','fa385238',2005,'233232','engeneering')
student2.register_subject(math)
student2.get_info()


















