#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 02:58:01 2025

@author: tojiboevolimjon
"""
#!!!Numbers (sonlar)

a=20
b=5.5
temp=36.5
type(temp)

population=7_354_234_456

x,y,z=10,12,15

c=a*b

d=52//2
radius=20
PI=3.14159
diametr=2*radius

print('aylana uzunligi=',PI*diametr) 

name='olimjon'
age=23

info=name+' ' + str(age) + ' yoshda'
print(info)

#!!!
birthday=int(input('when is your birthday?/n>>>'))
age=2025-birthday
print('you are',age ,'years old')


a=int('10')
b=float('10')
c=str(10.0)



#!!!Practice (amaliyot)


#Write and run each of the following programs as a separate file:

#1. A program that takes a number entered by the user and prints its square and cube to the console.

number=int(input('write a number\n...'))
print(f'the square of {number} is {number**2}\n the kube of {number} is {number**3}')


#2.A program that asks the user for their age, calculates their year of birth, and prints it to the console.


a=int(input('how old are you?\n>>>'))
b=2025-a
print('you were born in ',b)

#3.• A program that asks the user to enter two numbers and then prints the sum, difference, product, and quotient of those numbers.

number1=int(input('write any 2 numbers !\n 1st number : '))
number2=int(input('2nd number :'))
print(f"{number1}+{number2}=",number1+number2)
print(f"{number1}-{number2}=",number1-number2)
print(f"{number1}*{number2}=",number1*number2)
print(f"{number1}/{number2}=",number1/number2)















