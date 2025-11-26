#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 26 09:08:25 2025

@author: tojiboevolimjon
"""

#!!! "OOP"(object oriented programming)


#!!!""class""

#class yaratish.

class Student:
    def __init__(self,name,surname,birthyear):#self  class ichidagi funksiyaga obyektni uzatish uchun ishlatiladi
        #__init__ obyekt yaratilganda avtomatik ishlaydi
	    #self — obyektning o‘zini bildiradi
    
        self.name=name.title()
        self.surname=surname.title()
        self.birthyear=birthyear 
        
    #metod yaratish
    def get_name(self):
        return self.name
    def get_age(self,yil):
        return yil- self.birthyear
        
        
        
    def introduce(self):
        return f"Full name : {self.name} {self.surname} .bd :{self.birthyear}"

#obyekt yaratish

student1=Student('olimjon','tojiboev',2003)
student2=Student('ali','ergashev',2003)
student3=Student('jhon','turdiyev',2004)



student1.name
student1.surname
student1.birthyear

student2.name
student3.name


student1.introduce()
student2.get_name()

student1.get_age(2025)

class car:
    def __init__(self,model,year):
        self.model=model
        self.year=year
    
    def start(self):
        return f"{self.model} is ready "



car1=car('kia',2025)
car2=car('sonata',2018)


car1.start()

car2.start()

#!!! PRACTICE (amaliyot)

# 1Web sahifangiz uchun foydalanuvchi (user) klassini tuzing.
# Klassning xususiyatlari sifatida odatda ijtimoiy tarmoqlar talab qiladigan ma'lumotlarni kiriting (ism, foydalanuvchi ismi, email, va hokazo)

class User :
    def __init__(self,name,age,email):
        self.name=name.title
        self.age=age
        self.email=email
    


user1=User('olimjon',23,'olimjon@gmail.com')

user1.name()






# 2.Klassga bir nechta metodlar qo'shing, jumladan get_info() metodi foydalanuvchi haqida yig'ilgan ma'lumotlarni chiroyli qilib chiqarsin
# (masalan: "Foydalanuvchi: alijon1994, ismi: Alijon Valiyev, email: alijon1994@gmail.com).


class User :
    def __init__(self,userid,name,age,email):
        self.userid=userid
        self.name=name.title()
        self.age=age
        self.email=email
    def get_info(self):
        return f"userid: {self.userid} ,name :{self.name} ,email: {self.email}"


user2=User('olimjon2603','olimjon',23,'olimjon@gmail.com')

user2.get_info()


#3.

class Animal:
      
    def sound(self):
        return " animal sound"


class Dog(Animal):
    def sound(self):
        return "Vov vov"

dog1=Dog()


print((dog1.sound()))



#4 Mini project ATM

class Bankaccount:
    def __init__(self,owner,balance):
        self.owner=owner.title()
        self.balance=balance
        
    def deposit(self,amount):
        self.balance+=amount
        return f"{amount} won deposit .total balance :{self.balance}"
    
    def withdraw(self,amount):
        if self.balance< amount:
            return('not enough balance')
        self.balance-=amount
        return f"{amount} won withdraw .total balance :{self.balance}"
            
    
    def info(self):
        print(f"owner :{self.owner} ")
        
        print(f"total balance :{self.balance} won ")
        
owner1=Bankaccount('olimjon',20000)   

owner1.deposit(2000)

owner1.withdraw(5000)

owner1.info()













