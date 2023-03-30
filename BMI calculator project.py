#!/usr/bin/env python
# coding: utf-8

# In[13]:


name = input('Enter your Name : ')
weight = int(input("Enter your Weight in pounds: "))
height = int(input('Enter your height in inches :'))
BMI = (weight *703) / (height * height)
print(BMI)
if BMI > 0:
    if (BMI < 18.5):
        print(name ,"you are Underweight Minimal")   
    elif (BMI <=24.9):
          print(name ,"you are Normal Weight Minimalal")
    elif (BMI <=29.9):
          print(name ,"you are Overweight Increased")       
    elif (BMI <=34.9) :
          print(name ,"you are Obese high")       
    elif (BMI <=39.9 ):
          print(name ,"you are Severely Obese	Very High")
    else:
          print(name ,"you are over	Morbidly Obese	Extremely High")        
else:
    print("Enter Valid Input")


# In[ ]:





# In[ ]:


Under 18.5	Underweight	Minimal
18.5 - 24.9	Normal Weight	Minimal
25 - 29.9	Overweight	Increased
30 - 34.9	Obese	High
35 - 39.9	Severely Obese	Very High
40 and over	Morbidly Obese	Extremely High

