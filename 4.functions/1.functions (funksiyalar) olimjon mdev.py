#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 06:18:52 2025

@author: tojiboevolimjon
"""

#!!!functions (funksiyalar)
def say_hello():
    """salom beruvchi funksiya""" #funksiya nomini kiritiladi.
    print('Assalomu aleykum')
    
say_hello()


def say_hello(name):
    """ it says hello with name """
    print('Assalomu aleykum ,',name.title())
    
say_hello('olimjon')
say_hello('ali')
    
#!!!funksiya haqida malumot olish>
print(say_hello.__doc__)
print(print.__doc__)

#

def full_name(name,surname):#funksiya qiymat kritishda tartib boyicha kiritish kerak
                              #yani name ga ism surname ga familiya aks holda tartib boyicha ishlamaydi
    """it says name and surname"""
    print(f'user name :{name.title()}\n user surname:{surname.title()}')

full_name('olimjon', 'tojiboev')


#!!!tugulgan kuni hisoblaydigan funksiya


def b_day(name ,b_year):
    """calculate the age"""
    print(f'{name.title()}  : {2025-b_year}  years old')

b_day('olimjon',2003)

#agar b_day ga birinchi tugulgan yil keyin ism kiritsak kod ishlamaydi.

b_day(2003,'olimjon')#X X X X 


b_day(b_year=2003,name='olimjon')# shu usul orqali argumentlarni ornini almashtirish mumkin .

full_name(surname='tojiboev',name='olimjon')



def call_age(b_year2,thisyear=2025):
    """calculate age 2"""
    print(f"you are {thisyear-b_year2}  years old !")
    
    
    
call_age(2003,2025)

call_age(2003)# agar argumentlarni qiymatini berib ketsak keyin yozish shart emas.



#!!! PRACTICE (amaliyot)


#1. Foydalanuvchi ismi va yoshini so'rab, 
#uning tug'ilgan yilini hisoblaydigan funksiya yozing.

def ismyosh(name,age):
    """tugulgan yilini hisoblaydigan funksiya"""
    print(f"{name.title()} :siz {2025-age} yilda tugulgansiz !")

ismyosh('olimjon',22)



# 2.Foydalanuvchidan son olib,
# uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.

def numkv(number):
    """sonni kvadrati va kubini hisoblovchi funksiya"""
    print(f"{number} ning kvadrati :{number**2} \n {number} ning kubi :{number**3}")
    
numkv(2)



# 3.Foydalanuvchidan son olib,
# son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.

def numb(number2):
    """sonni juft yoki toqligini aniqlovchi funksiya"""
    if number2%2==0:
        print(f"{number2} :juft son")
    else:
        print(f"{number2} :toq son")
   

numb(3)
numb(2)




# 4.Foydalanuvchidan ikkita son olib, 
#ulardan kattasini konsolga chiqaruvchi funksiya yozing.
# Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.

def numeq(num1,num2):
    """sonlarni taqqoslovchi funksiya"""
    if num1<num2:
        print(num2)
    elif num1>num2:
        print(num1)
    elif num1==num2:
        print('sonlar teng')

numeq(12,15)


# 5.Foydalanuvchidan x va y sonlarini olib,
# x^y ni konsolga chiqaruvchi funksiya yozing.



def numkvd(x,y):
    """sonni darajasini aniqlovchi funksiya"""
    print(f"{x} ning {y} darajasi {x**y} ga teng")

numkvd(2,4)



# 6.Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.


def numkvd(x,y=[2,3]):
    """sonni darajasini aniqlovchi funksiya"""
    print(f"{x} ning {y} darajasi {x**y} ga teng")

numkvd(2,4)






# 7.Foydalanuvchidan son qabul qilib, 
#sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya yozing. 
#Natijalarni konsolga chiqaring.
a=list(range(2,11))

def son2(numerr):
    """sonni qoldiqsiz bolinishini tekshiruvchi funksiya"""
    for b in a:
        if numerr%b==0:
            print(f"{numerr} : { b} ga qoldiqsiz bolinadi.")
    
     





