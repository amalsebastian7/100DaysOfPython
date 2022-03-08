                 # Data types: 

#1) String = "abadhjd "
# print("hello"[0])
# print first letter of the string


# from unicodedata import decimal


# 2)Integer=1234
# print(123+234)

# 3)float=5.35454
# its number with decimal

# 4)Boolean=True or False
# its capital first letter



from calendar import month
from doctest import Example


num=len(input("whats your name?"))
print("Your name has"+num+"characters")
#here there is a type error,because the num value is an integer
# and the +symbol is trying to concatinate the string and the integer.int
# so we have to change the type to concatinate.

num=len(input("whats your name?"))
stNum=str(num)#we use the str function here to change the type
print("Your name has"+stNum+"characters")

#You can use type function to find the type of input and use int,float,str for converting these

#Exercise:
# get the input from doctest import OutputChecker
# from the user:any 2 number and add those two and show the Output
# for instance input  26=8 

num1=input("enter a 2 digit number")
add = int(num1[0])+int(num1[1])
print(add)

                     #Numbers
# If there are more than one operation in a line there is a standard priority for this :

# PEMDAS
# When there is two operation from same level the calculation goes from left to right
# ()
# **
# *   /
# +   -

                    # Example

#Print BMI of the given person

height = float(input("whats your height in meter?  " ))
weight = int(input("whats your weight in kilograms? " ))
BMI = int(weight/(height**2))
print(BMI)

# print(8/3)
# this would give 2.666666666 something 
# if we have to shorten it the two common ways are 
# 1)make it an int and all the decimal places are gone boom!
# 2)Use round function and keep the precision with the shortening


# so there are two ways to use round function one is to define the precision and the other one is without defining 
# print(round(8/3,2))
# This gives a precision of two decimal points.

# (Tip:if you wanna just chop of all decimal point and just keep the integer then use a double slash eg:
# print(8//3)
# which will give 2 and remove all decimal places.
# )

# full = full +1(short hand full=+1)

                          #f-string
usual method 

score =0
height =1.8 
weight =67
print("your score is "+str(score)+" and your height is  "+str(height)+" and your weight is "+str(weight))

# ***f-string method***

score =0
height =1.8 
weight =67
print(f"your score is {score}, and your height is {height},and your weight is {weight}")

#add f infront of the string and use curley bracket for all the variables.


#Exercise 
#Given the input of age and Maxlife expectancy as 90 output the days ,weeks, year,months left

age=int(input("whats your current age? "))
left= 90-age
weeks=left * 52
months=(left//12)
days=left*365
print(f"You have {left} years,{weeks} weeks,{months} months and {days}days left ")

               
                #***Assignment Day 2***

# Make a tip calculator

print("Welcome to tip calculator.")
tb=float(input("what was the total bill?$"))
pt=int(input("what percentage tip would you like to give?10,20or15?"))
split=int(input("how many people to split the bill with?"))
total_tip = round(tb*pt/100,2)
each=round(total_tip/split,2)
print(f"Each person would pay {each} as tip totalling to {total_tip}")
per=round(tb/split+total_tip/split,2)
print(f"Each pays :{per}")


