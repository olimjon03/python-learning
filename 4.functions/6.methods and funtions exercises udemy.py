#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 25 04:48:06 2025

@author: tojiboevolimjon
"""
#1.Write a function that computes the volume of a sphere given its radius.
from math import pi

def hajm(radius):
    valume=(4/3)*pi*(radius**3)
    return valume


hajm(45)


#2.Write a function that checks whether a number is in a given range (inclusive of high and low)

def numin(num1,num2,num3):
    if num1<=num2<=num3 or num1>=num2>=num3:
        return num2
    elif num2<=num1<=num3 or num2>=num1>=num3:
        return num1
    elif num2<=num3<=num1 or num2>=num3>=num1:
        return num3




numin(2,3,4)




numin(5,11,7)


#3
#Write a Python function that takes a list and returns a new list with unique elements of the first list.

numlist=[1,2,2,2,4,4,4,5,1,1,1,6,6,7,7,7,3,3,3,]



def sortnum(numlist):
    
    return set( numlist)

sortnum(numlist)


#4.Write a Python function to multiply all the numbers in a list.



numbers=[2,3,4]
        
def numb(numbers):
    result=1
    for n in numbers:
        result*=n
    return result

numb(numbers)










