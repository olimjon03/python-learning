#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 22:34:48 2025

@author: tojiboevolimjon
"""
#!!!Strings

name='olimjon'
surname='tojiboev'
print(name+' '+surname)
sticker='❤'
print(name+' '+surname,sticker)

# !!!" f "string

full_name=f"my surname is  {surname}"
print(full_name)
print (f"my name is {name},my surname is  {surname}" )

#!!! Symbols (belgilar)


print('hello world')

print('hello\tworld')

print('hello\tworld,\nmy name is\n"olimjon"')

full_name=(f'{name},{surname}')

print(full_name.upper())

print(full_name.lower())

print(full_name.title())

print(full_name.capitalize())
\
full_name=full_name.upper()

fruit='    apple,banana       '

print("i like an "+fruit+"!")

print("i like an "+fruit.lstrip()+"!")

print("i like an "+fruit.rstrip()+"!")

print("i like an "+fruit.strip()+"!")

name=input("what is your name?\n>>>")

surname=input("what is your surname?\n>>>")

fullname=(name +' '+ surname)

print('hello , welcome\t'+fullname.title())


#!!! Practice

#1 Create the following variables:
    
# street = "Bog'bon"
# neighborhood = "Sog'bon"
# district = "Bodomzor"
# region = "Samarqand"

kocha="Bog'bon"

mahalla="Sog'bon"

tuman="Bodomzor" 

viloyat="Samarqand"

#2.Combine the variables above and print them to the console in the following format:
    
#Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati


print(f"{kocha} ko'chasi,\n{mahalla} mahallasi,\n{tuman} tumani,\n{viloyat} viloyati")


#3.Ask the user to input the values of the variables (street, neighborhood, district, region) and repeat the previous exercise.


kocha=input('where is your street?\n>>>')

mahalla=input ('where is your addres?\n>>>')

tuman=input('where is your tuman?\n>>>')

viloyat=input('where is your region?\n>>>')

#4.Store the text above in a new variable called address using an f-string.

address=(f"{kocha}kochasi+{mahalla}mahallasi+{tuman}tumani")

#5.Try applying the methods title(), upper(), lower(), and capitalize() to the address variable we created above.


print("sizning adresingiz\t" +address.title())
print(address.upper())
print(address.lower())
print(address.capitalize())
















