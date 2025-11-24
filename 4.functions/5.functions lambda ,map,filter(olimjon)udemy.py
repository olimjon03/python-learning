#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 06:56:19 2025

@author: tojiboevolimjon
"""

#!!! "map" map(func,*iterables) har bir elementga function ni qollaydi.

# function — har bir elementga qo‘llanadigan funksiya
# 	•	iterable — list, tuple, string va h.k.
# 	•	map() natijasi → map object → list() bilan o‘giriladi

def square(num):
    return num**2
mynum=[1,2,3,4,5]

#map(square,mynum) #mapni bu tarzda ishlatib bolmaydi uni biror keyword list, forloop...larga boglab qoyish kerak.

for item in map(square,mynum):
    print(item)
    
    
list(map(square,mynum))

def slicer (mystring):
    if len(mystring)%2==0:
        return ' even'
    else:
        return mystring[0]
    
names=['olimjon','ali','jhon']

list(map(slicer,names))
        


#!!! filter() SHARTGA MOS ELEMENTLARNI TANLAYDI.

#function → True qaytarsa element olinadi, False bo‘lsa olinmaydi

def checknum(num):
    return num%2==0

numbers=[1,2,3,4,5,6,7,8]


list(filter(checknum,numbers))

for n in filter(checknum,numbers):
    print(n)


#!!! lambda
#lambda — bu funksiya, lekin nomi yo‘q.
#Biror kichik hisob-kitobni tezda qilish uchun ishlatiladi.

#Lambda qanday ishlaydi?- lambda argumentlar: qaytadigan_narsa

#def square(num):
    #return num**2


mynum=[1,2,3,4,5]

lambda num:num**2


list(map(lambda num:num**2,mynum))
 

#def checknum(num):
   # return num%2==0

numbers=[1,2,3,4,5,6,7,8]


#list(filter(checknum,numbers))

list(filter(lambda num:num%2==0,numbers))

names=['olimjon','ali','jhon']
list(map(lambda x:x.upper(),names))
list(map(lambda y:y[::-1],names))













