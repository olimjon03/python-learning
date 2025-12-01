#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 00:17:50 2025

@author: tojiboevolimjon
"""


#modeldan id raqam olish

from uuid import uuid4


#!!!inkapsulatsiya
#inkapsulatsiya-U obyektning ichki ma’lumotlarini yashirish
# va ularga faqat maxsus metodlar orqali kirishga ruxsat berishni anglatadi.

class Avto :
    """avtomobil klassi"""
    #bu ozgaruvchilar faqat klassga tegishli boladi
    __num_avto=0
    PI=3.14159
    def __init__(self,company,model,color,year,km=0):
        self.company=company
        self.model =model
        self.color=color
        self.year=year
        
        #inkapsulatsiya qilish
        self.__km=km
        self.__id=uuid4()
        
        
        #bunda classga kiritilgan obyekt malumotlarni hisoblaydi
        
        Avto.__num_avto+=1
        
        # num_avtodan malumot olish
    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto
        
        
    #inkapsulatsiyadan malumot olish
    def get_km(self):
        return self.__km
    
    def get_id(self):
        return self.__id
    def add_km(self,km):
        if km>=0:
            self.__km+=km
        else:
            print('you can only add km')
        


        
avto1=Avto('kia','morning','black',2010,90000)
avto2=Avto('hyundai','sonata','white',2018,8000)
avto3=Avto('mers','class500','black',2024,2000)

avto1.get_km()
avto1.get_id()
avto1.add_km(1000)
avto1.get_km()

#PRACTICE (amaliyot)







# 1.Avvalgi darslarimizda yaratgan Shaxs va 
#Talaba klasslariga yopiq xususiyatlar qo'shing va ularning qiymatini ko'rsatuvchi
# va o'zgartiruvchi metodlar yozing.

class User ():
    """foydalanuvchi klassi"""
    #2. klasslarga talabalar_soni va odamlar_soni degan klassga oid xususiyatlar qo'shing.

    __number_user=0
    
    def __init__(self,name,surname,b_year,passport):
        self.name=name.title()
        self.surname=surname
        self.b_year=b_year
        self.__passport=passport
        self.__id_num=uuid4()
        User.__number_user+=1
        
        
        
    #3.Klassga oid xususiyatlar bilan ishlash uchun maxsus @classmethod lar yozing    
    @classmethod
    def get_user_num(cls):
        return cls.__number_user
    
    #passport raqamini korish
    def get_passport(self):
        return self.__passport
    
    def get_id_user(self):
        return self.__id_num
        
    def get_info(self):
        info=f"Full name: {self.name} {self.surname.title()}"
        info+=f" Passport {self.passport} ,bearth year :{self.b_year}"
        return info
    def get_age(self ,b_year):
        by=2025-self.b_year
        return by

    
user1=User('ali','shamhiev',2003,'fa232222')
user2=User('husan','ergashev',2013,'fa112222')
user1.get_passport()    
user1.get_id_user()
user1.get_user_num()



  






























