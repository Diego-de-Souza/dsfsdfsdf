# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 12:31:36 2023

@author: lucas
"""
import funcao as f
import math as m

def funcao_bolzano_newruf(x,precisao):
    
    
    k=0
    
    while True :
        k+=1
        x = x - f.funcao(x)/f.Derfuncao(x)
        
         
        if( len(str(x).split(".")[1]) > precisao) :
            break
        
        
    return {x,k}


def decimal_places(number):
    if isinstance(number, float):
        str_number = str(number)
        if '.' in str_number:
            return len(str_number.split('.')[1])
    return 0
        
    
