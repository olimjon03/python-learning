###datatime module

import datetime as dt

now= dt.datetime.now()
print(f'hozirgi vaqt : {now}')

### sanani ajratish

print(now.date())

###vaqtni ajratish

print(now.time())

###sekundani ajratish

print(now.second)

###date()

today= dt.date.today()
print(f'hozirgi sana: {today}')
tomorrow=dt.date(2025,12,7 )
print(f'ertangi sana: {tomorrow}')
timenext=dt.time(14,30,45)
print(timenext)


###sanalarni solishtirish
today= dt.date.today()
bday= dt.date(2026,3,26) 
farq= bday - today
print(farq)

print(farq.days)
print(f"tugu'ilgan kunimgacha {farq.days} kun qoldi")

###soatlar orasida farq

now= dt.datetime.now()
 
football_game= dt.datetime(2025,12,9,18,0,0)
time_diff= football_game - now
seconds= time_diff.seconds
minutes= int(seconds/60)
hours= int(minutes/60)
print(f"football o'yiniga {time_diff.days} kun, {hours} soat, {minutes} daqiqa qoldi")

import math
PI= math.pi
print(f"pi ning qiymati: {PI}")
E= math.e 
print(f"e ning qiymati: {E}")
###radianlar va burchaklar orasida konvertatsiya
print(math.degrees(PI/2))
print(math.radians(90))

###sonlarni yaxlitlash
x=4.6
print(math.ceil(x))
print(math.floor(x))

###kvadrat ildiz
x=81
print(math.sqrt(x))

###darajaga ko'tarish
print(math.pow(x,3)) # x ning kubini hisoblaydi
math.pow(x,5) # x ning beshinchi darajasini hisoblaydi
math.pow(x,1/3) # x ning kub ildizini hisoblaydi

### RegEx module (regular expressions)

###Regex (Regular Expressions) — matn ichidan ma’lum bir pattern (shablon) bo‘yicha qidirish, 
### topish, almashtirish imkonini beradigan kuchli modul.
import re
word1= "olimjon"
word2= "temur"
word3= "tomir"

andoza="^t...r$"
print(re.match(andoza,word1)) ### None qaytaradi, chunki mos kelmaydi
print(re.match(andoza,word2)) ### mos keladi, 
print(re.match(andoza,word3)) ### mos keladi

text="""Assalom alaykum hurmatli do'stlar. Navbatdagi darsimiz 
YouTubega yuklandi: https://youtu.be/vsxJPRLXpgI Ushbu darsimizda unittest 
moduli yordamida klasslarning xususiyatlar va metodlarini tekshiruvchi dastur yozishni o'rganamiz.
 Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test"""

url_andoza= r'https?://[^\s]+'
urls= re.findall(url_andoza,text)
print(urls)

###telefon raqamlarini topish
# phone_num=input("Telefon raqamingizni kiriting: ")
# def find_phones(phone_num):
#     kor_phone_andoza= r'\+82[0-9]{9}'
#     match= re.match(kor_phone_andoza,phone_num)
#     if match:
#         print("Raqam to'g'ri formatda kiritildi.")
#     else:
#         print("Raqam noto'g'ri formatda kiritildi. Iltimos, +82XXXXXXXXX formatida kiriting.")
    


# find_phones(phone_num)


###PRACTICE (AMALIYOT)

###1.Bugungi sanadan boshlab 2 hafta farq bilan 10 ta sanani konsolga chiqaring.
now= dt.date.today()
for i in range(1,11):
    future_date= now + dt.timedelta(weeks=2*i)
    print(future_date)




###2.Ramazon va qurbon hayitigacha qolgan kunlarni konsolga chiqaring
ramazon= dt.date(2026,3,11)
qurbon_hayit= dt.date(2026,6,16)
today= dt.date.today()
days_to_ramazon= (ramazon - today)
days_to_qurbon= (qurbon_hayit - today)
print(f"Ramazon hayitiga {days_to_ramazon.days} kun qoldi")
print(f"Qurbon hayitiga {days_to_qurbon.days} kun qoldi")





###3.Tug'ilgan kuningizdan bugungi sanagacha qancha yil, oy, kun o'tganini qaytaruvchi funksiya yozing

def age_calculator(birth_date):
    today= dt.date.today()
    age_days= (today - birth_date)
    age_years= age_days/365
    age_months= age_days/30
    print(f"Siz {age_years.days} yil, {age_months.days} oy, {age_days.days} kun yashagansiz.")


birth_date= dt.date(2003,3,26)
age_calculator(birth_date)

    
