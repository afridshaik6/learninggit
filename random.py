#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 12:31:43 2022

@author: zorro
"""

class Employee:
    emp_count = 0
    def __init__(self,fname,lname,dob,salary):
        self.firstname = fname
        self.secondname = lname
        self.dateofbirth = dob
        self.grosssalary = salary
        Employee.emp_count+=1
        print("hi")
    def age(self):
        return(2022 - self.dateofbirth)
    
    
emp1 = Employee("Afrid","shaik",1998,25000)
c=emp1.age()



    
        
