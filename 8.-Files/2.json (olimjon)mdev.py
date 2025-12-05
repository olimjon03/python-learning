#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 10:39:57 2025

@author: tojiboevolimjon
"""

#!!! json 



import json

x=10
x_json=json.dumps(x)


type(x)
print(x)
type(x_json)

y=5.5
y_json=json.dumps(y)
y_json

m=True
m_json=json.dumps(m)

m_json

json.loads(m_json)

 #loads - json dan pyhtonga otqazadi


numbers=(12,13,24,12,44)
num_json=json.dumps(numbers)
num_json


user={
      'name':'olimjon',
      'surname':'tojiboev',
      'age':23,
      "country":'uzbekistan',
      'university':'chonnam'
      }
      
user_json=json.dumps(user)

print(user_json)    

type(user_json)

user_json=json.dumps(user,indent=4) #indent=4 chiroyli formatda chiqarib beradi
print(user_json)    


#!!! json ni filega yozish

with open ('user.json','w') as file :
    json.dump(user,file)

#!!! PRACTICE (amaliyot)


#1.

# Berilgan JSON matn (dict ko‘rinishida)
user2 = {
    "name": "Olimjon",
    "age": 22,
    "languages": ["Python", "JavaScript", "SQL"]
}

# dict → JSON matn
user2_json = json.dumps(user2)

# JSON matn → Python dict
data = json.loads(user2_json)

# Kerakli qiymatlarni chiqarish
print(data['name'])
print(data['languages'])

#2.

student1 = {
  "id": 101,
  "name": "Ali",
  "major": "Computer Science",
  "courses": [
    {"title": "Python Basics", "score": 90},
    {"title": "Data Structures", "score": 85}
  ]
}

# JSON faylga yozish
with open('student.json', 'w') as file:
    json.dump(student1, file, indent=4)

# JSON fayldan o‘qish
with open('student.json', 'r') as file:
    studentr = json.load(file)

# Python Basics kursining balli
score = studentr['courses'][0]['score']

print(studentr)
print("Python Basics score:", score)
















