###
from googletrans import Translator

tarjimon=Translator() ### Translater bu maxsus class (tarjimon esa object)

text_uz="Assalomu aleykum ,mening ismim olimjon ,yoshim 22 da "

### istalgan matnni ingliz tiliga tarjima qilish uchun translate metodini chaqiramiz

tarjima = tarjimon.translate(text_uz)

### original matn chiqarish

print(tarjima.origin)

### tarjima matn

print(tarjima.text)

### orginal matni tilini aniqlash

print(tarjima.src)

### boshqa tillarga tarjima qilish

tarjima_kor= tarjimon.translate(text_uz,dest='ko')

print(tarjima_kor.text)

### boshqa tillardan uzbek tiliga tarjima qilish
text_eng="hello, my name is Olimjon "
tarjima_uz= tarjimon.translate(text_eng,dest='uz')

print(tarjima_uz.text)
##=============================
### uzbek, korean translater ###
##=============================


matn='write your text to translate :\n for quite enter "q"'

while True:
    text1=input(matn)
    if text1=='q':
        break
    else:
        tarjima =tarjimon.translate(text1,src='uz',dest='ko')

        print(tarjima.text)

##==============================================
### Requests - Internetdan ma’lumot olish ####
##==============================================


###1.web api dan data olish

import requests

url='https://api.github.com'
response=requests.get(url)
print(response.json())

###2.Saytga so‘rov yuborish

res=requests.get('https://www.google.com')

###res → Google serveri yuborgan javobni o‘z ichiga oladi.
###requests.get() - Google serveriga GET so‘rov yuboradi.
###Bu javobning ichida quyidagilar bo‘ladi:
###	•	HTML kod
###	•	Status kodi (200, 404, 503 …)
###	•	Headers
###	•	Cookie
###	•	Server maʼlumotlari

print(res.status_code)









    



