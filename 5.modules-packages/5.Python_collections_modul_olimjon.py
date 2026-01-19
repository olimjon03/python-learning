
###======== Counter ===========###

#listdagi itemlarni necha marta takrorlanganini bilish uchun

from collections import Counter

mylist=[1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3]

print(Counter(mylist))

mylist2=['a','a','a',10,10,10,10]

print(Counter(mylist2))

sentence="How many times does each word show up in this sentence with a word"

print(Counter(sentence.split()))

letters='aaaaabbbbbcccddddddd'
c=Counter(letters)
print(c)
print(c.most_common)

print(list(c))




###======== namedtuple ===========###

from collections import namedtuple

##namedtuple — bu Python’da collections modulida 
## bor bo‘lgan maxsus tuzilma bo‘lib, u oddiy tuple’ni o‘qilishi oson va 
## ma’noli qilib beradi.

Dog =namedtuple ('Dog',['age','breed','name'])

sammy=Dog(age=5,breed='Husky',name='Sam')

print(type(sammy))
print(sammy)



