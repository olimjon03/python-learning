#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 02:13:04 2025

@author: tojiboevolimjon
"""


#!!!moduls


import math #matematik amallar moduli
x=400
print(math.sqrt(x))#sonni ildizini hisoblaydi
print(math.pow(5,3))#sonni darajasini hisoblaydi.
print(math.pi)# pi ni qiymati
print(math.log2(3))#logorifmni hisoblaydi

#!!!modul nomini ozgartirish


import math as m #matematik amallar moduli
x=400
print(m.sqrt(x))#sonni ildizini hisoblaydi
print(m.pow(5,3))#sonni darajasini hisoblaydi.
print(m.pi)# pi ni qiymati
print(m.log2(3))#logorifmni hisoblaydi



#!!! 'random' moduli.
import random
number=random.randint(0,100)#sonlarni random qilib tanlaydi.

print(number)




#choice()# listlar orasidan random qilib tanlaydi.
ismlar=['olimjon','anvar','hasan','husan']
ism=random.choice(ismlar)
print(ism)




x=list(range(0,100,5))
print(x)
print(random.choice(x))



#shuffle()

a=list(range(20))
random.shuffle(a)
print(a)







