#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 10:55:14 2019

@author: knight
"""

#month=int(input("enter month"))
#months=['jan','feb','march','april','may','june','july','aug','sept','oct','nov','dec']
#a=month-1
#number=months[a]
#if month <= 0 :
#    print(" enter positive intiger")
#elif month <=12:
 #   print(a)
#else:
 #   print("try again")
    
#for i in range(months[0],months[13])
#months[0]
 
month=int(input("enter month "))
months=['jan','feb','march','april','may','june','july','aug','sept','oct','nov','dec']
a=month-1
number=months[a]
if month <= 0 :
    print(" enter positive intiger")
elif month <=12:
    print(number)
else:
    print("try again")
    
month=int(input("enter month "))
months=['jan','feb','march','april','may','june','july','aug','sept','oct','nov','dec']
a=month-1
number=months[a]
for i in range(0,len(months[a])):
    print(i)
    
month=int(input("enter month "))
months=['jan','feb','march','april','may','june','july','aug','sept','oct','nov','dec']
a=month-1
month_name=months[a]
if a <=12 and a>0:
    for i in months:
        if (i == month_name):
            print(month_name)
            break 
if a > 12:
    
    
month=int(input("enter month "))
if month <=12 and month > 0:
    months=['jan','feb','march','april','may','june','july','aug','sept','oct','nov','dec']
    a=month-1
    month_name=months[a]
    for i in months:
        if (i == month_name):
            print(month_name)
            #break
else:
    print('err')


def maximum(a):
    mm=a[0]
    for i in a:
        if (mm<i):
            mm=i
    print(mm)
lll=[1,2,3,4,7,3,9,12,56]
maximum(lll)


# creating an empty list 
lst = [] 
  
# number of elemetns as input 
n = int(input("Enter number of elements : ")) 
  
# iterating till the range 
for i in range(0, n): 
    ele = int(input()) 
  
    lst.append(ele) # adding the element 
      
print(lst) 



lst= []
  
# iterating till the range 
for i in range(0, len(n)): 
    ele = [1,2,3,4,56] 
  
    lst.append(ele) # adding the element 
      
print(lst) 


a=list(input("enter list"))
def maximum(a):
    mm=a[0]
    for i in a:
        if (mm<i):
            mm=i
    print(mm)
    
a=int(input("enter list"))
list=a.split()
def maximum(list):
    mm=list[0]
    for i in list:
        if (mm<i):
            mm=i
    print(mm)