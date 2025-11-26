#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 26 01:00:01 2025

@author: tojiboevolimjon
"""

#!!! "" FIND NUMBERS GAME ""


from random import randint


def findnum():
    randomm=randint(1,10)
    new=[]
    print('1 dan 10 gacha son oyladim topa olasizmi?')
    
    num=int(input(">>>:"))
    
    
    while randomm!=num:
        if num >randomm:
            print(f"{num} dan kichik ")
        elif num <randomm:
            print(f"{num} dan katta")
        new.append(num)
        num=int(input(">>>:"))
            
        return f"Tabriklayman , !!! Siz {len(new)+1} ta urunishda topdingiz"

findnum()           
        
        
            

  
    
    
          
        
        
       
    
    
    
    



