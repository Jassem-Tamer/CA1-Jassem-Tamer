#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: Jassem Alhaj Tamer
@Student ID: 10168910
"""
def show_menu():
    print"************************"
    print "THANK YOU FOR USING OUR CALCULATOR APP."
    print "This is a simple calculator with 10 functions "
    print "Press Q to quit a function"
    print"************************"

def sum ():
    while True:
        num1 = raw_input("Enter 1st number for addition \n")
        try:
            num1 = float(num1)
            
        except:
            print ("Please Enter Numeric Value")
            continue
        num2 = raw_input("Enter 2nd number for addition \n")
        try:
            num2 = float(num2)
           
        except:
            print ("Please Enter Numeric Value")
            continue
        plus = num1 + num2
        print "No 1 + No 2 = {}".format(plus)
        if "Q" == raw_input("Q to quit / Enter to continue:\n"):
            break
def sub ():
    while True:
        num1 = raw_input("Enter 1st numbrer for substraction\n")
        try:
            num1 = float(num1)
            
        except:
            print ("Please Enter Numeric Value")
            continue
        num2 = raw_input("Enter 2nd number for substraction\n")
        try:
            num2 = float(num2)
           
        except:
            print ("Please Enter Numeric Value")
            continue
        min = num1 - num2
        print "No 1 - No 2 = {}".format(min)
        if "Q" == raw_input("Q to quit / Enter to continue:\n"):
            break
def mult ():
    while True:
        num1 = raw_input("Enter 1st number for mutliplication\n")
        try:
            num1 = float(num1)
            
        except:
            print ("Please Enter Numeric Value")
            continue
        num2 = raw_input("Enter 2nd number for mutliplication\n")
        try:
            num2 = float(num2)
           
        except:
            print ("Please Enter Numeric Value")
            continue
        by = num1 * num2
        print "No 1 *  No 2 = {}".format(by)
        if "Q" == raw_input("Q to quit / Enter to continue:\n"):
            break
def div ():
    while True:
        num1 = raw_input("Enter 1st number for division\n")
        try:
            num1 = float(num1)
            
        except:
            print ("Please Enter Numeric Value")
            continue
        num2 = raw_input("Enter 2nd number for division\n")
        try:
            num2 = float(num2)
           
        except:
            print ("Please Enter Numeric Value")
            continue
        if num2 ==0:
            print "ZeroDivisionError"
        else:
            over = num1 / num2
            print "No 1 / No 2 = {}".format(over)
        
        if "Q" == raw_input("Q to quit / Enter to continue:\n"):
            break
def modu ():
    while True:
        num1 = raw_input("Enter 1st number for remainder\n")
        try:
            num1 = float(num1)
            
        except:
            print ("Please Enter Numeric Value")
            continue
        num2 = raw_input("Enter 2nd number for remainder\n")
        try:
            num2 = float(num2)
           
        except:
            print ("Please Enter Numeric Value")
            continue
        modulus= num1 % num2
        print "No 1 % No 2 = {}".format(modulus)
        if "Q" == raw_input("Q to quit / Enter to continue:\n"):
            break
def expo ():
    while True:
        num1 = raw_input("Enter 1st number for exponential\n")
        try:
            num1 = float(num1)
            
        except:
            print ("Please Enter Numeric Value")
            continue
        num2 = raw_input("Enter 2nd number for exponential\n")
        try:
            num2 = float(num2)
           
        except:
            print ("Please Enter Numeric Value")
            continue
        ex = num1 ** num2
        print "No 1 ** No 2 = {}".format(ex)
        if "Q" == raw_input("Q to quit / Enter to continue:\n"):
            break
def fact():
    number = raw_input("Enter a number to get factorial value\n")
    try:
        number = float(number)
    except:
        print ("Please Enter Numeric Value")
    i =1
    mult = 1
    while i <= number:
        
        mult = 1
        while i <= number:
            mult = mult * i
            i = i + 1
        print "Factorial value: {}".format(mult)
        if "Q" == raw_input("Q to quit / Enter to continue:\n"):
            break
def sqr():
    while True:
        number = raw_input("Enter a number to get Square Root\n")
        try:
            number = float(number)
        except:
            print ("Please Enter Numeric Value")
        if number >= 0:
            print "Square Root of your input is : {}".format(round(number ** (1/2.0),3))
        else:
            print "Square Root of your input is : {}".format(round(-(-number) ** (1/2.0),3))
        if "Q" == raw_input("Q to quit / Enter to continue:\n"):
            break
def cube ():
    while True:
        number = raw_input("Enter a number to get Cube Root\n")
        try:
            number = float(number)
        except:
            print ("Please Enter Numeric Value")
        if number >= 0:
            print "Cube Root of your input is : {}".format(round(number ** (1.0/3.0),3))
        else:
            print "Cube Root of your input is : {}".format(round(-(-number) ** (1/3.0),3))
        if "Q" == raw_input("Q to quit / Enter to continue:\n"):
            break
def sin ():
    while True:
        import math
        number = raw_input("Enter a number to get Sine Value\n")
        try:
            number = float(number)
        except:
            print ("Please Enter Numeric Value")
            
        print "Sine value of your input is : {}".format(round(math.sin(number),4))
        if "Q" == raw_input("Q to quit / Enter to continue:\n"):
            break

