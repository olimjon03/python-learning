##===================================
### TRY / EXCEPT / ELSE /FINALLY   ###
##===================================

###TRY — xato bo‘lishi mumkin bo‘lgan kod

## try: Sinab ko‘r
### except: Xato bo‘lsa ushla
### else: Xato bo‘lmasa davom et
### finally: Baribir yakunla

# def  add (n1,n2):
#     print(n1+n2)

# add(10,20)

# number1=10
# number2=input("please enter a number :")
# add(number1,number2) ##bunda xato beradi agar shunda try ishlatilsa davom etishi mumkin

try:
    ###xato bolishi mumkin kod
    result=10+10

except:
    ### kod xato bolsa javob berish
    print('hey ,it looks like you are not adding correctly')

print(result)

###====================================
try:
    ###xato bolishi mumkin kod
    result=10+'10'

except:
    ### kod xato bolsa javob berish
    print('hey ,it looks like you are not adding correctly')
else:
    ##xato bolmasa javob berish
    
    print('add went well')
    print(result)



###======= example with files=======


try:
    f=open('testfile','r')
    f.write('write a test line')
except TypeError:### agar typeerror bolsa javob qaytaradi
    print("there was a type error!!")
except OSError:
    print('hey,you have an OS Error')
finally:#har doim ishlaydi xato bolsa ham bolmasa ham
    print('i always run')


#======================================

def ask_for_int():
    while True:
        try:

            result=int(input("provide number :"))
        except:
            print("whoops!, that is not a number ")
            continue
        else:
            print('yes thank you')
            break
        finally:
            print("end of try/except/finally")
            
    


ask_for_int()


##==========================
### PRACTICE (AMALIYOT)
##==========================
## 1.Handle the exception thrown by the code below by using try and except blocks.
try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print('you can calculate only numbers')

###2.Handle the exception thrown by the code below by using 
##try and except blocks. Then use a finally block to print 'All Done.'

x=5
y=0
try:
    z=x/y
except ZeroDivisionError:
    print('you cant divide by "O" ')

finally:
    print('all done')

##3.Write a function that asks for an integer and prints the square of it.
##Use a while loop with a try, except, else block to account for incorrect inputs.

def ask():
    while True:
        try:
            sq_num=int(input("enter a number :"))
            
        except:
            print('please write only number')
            continue
        else:
            print(f"answer :{sq_num **2}")

            break

     
ask()
    









