                     #control statements

from re import M, S


print("welcome to the ride")
h=int(input("whats your height") )
if h>120:       #120 not included
    print("Lets ride")
else:
    print("Not today kid")


    # here you have to notice that the intentation is very important in python.With an if statement
    # there will be a condition ,like always there will be condition true and condition false.
    # if the condition is true then it will execute the first part of the code or else it will execute the 
    # second part.make sure to not use intentation on else statement.


                        # comparison operators
# = (assignment)
# ==(exact same)
# >
# <
# >=
# <=
# !=
                   #exercise
            
# ---------#create a program to see if the given number is odd or even----------
number=int(input("Enter an integer number please: "))
if number%2==0:
    print("Its an even number")
else:
    print("Its an odd")

#the percentage symbol used here is called modulo and it finds the remainder 
# after the first number gets divided by the second number.

# ------------------#use two condition on the first exercise-------------------

print("welcome to the ride")
h=int(input("whats your height") )



if h>120 :       #120 not included
    age=int(input("Ok cool,whats your age") )
    if age>=18:
        print("your charge is 14$")
    else:
        print("your charge is 7$")
else:
    print("Not today kid")

# --------------#if you need more conditions you can use elif-----------------



print("welcome to the ride")
h=int(input("whats your height") )

if h>120 :       #120 not included
    age=int(input("Ok cool,whats your age") )
    if age<=12:
        print("your charge is 8$")
    elif 13<=age<18:
        print("your charge is 10$")
    else:
        print("Your charge is 14$")
else:
    print("Not today kid")

# ------------------------#BMI calculator----------------------------------------

height=float(input("Could you please enter your height in meter: "))
weight=float(input("Could you please enter your weight in kg: "))
bmi=float(weight/(height**2))
if bmi<18.5:
    print("They are underweight")
elif 18.5<bmi<25:
    print("They are normal weight")
elif 25<bmi<30:
    print("They are overweight")
elif 30<bmi<35:
    print("They are obese")
else:
    print("They are clinically obese")


# -------------------------#Find the leap year challange-----------------------

year=int(input("Enter the year"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f"{year } is leap year")
        else:
             print(f"{year } is not leap year")

    else:
        print(f"{year } is leap year")
else:
   print(f"{year } is not leap year")


# -----------------------------#pizza order-------------------------------


print("welcome to pizza hut")
size=str(input("What size do you want? S,L,M"))
pep=str(input("Do you want to add peparoni? Y / N"))
bill=0


if size=="S":
    bill=15
    print(f"Small pizza:$ {bill}")

    if pep=="Y":
        bill+=2
        print(f"Small pizza with pepperoni is: $ {bill}")
    else:
        print(f"Bill is :{bill}")

elif size=="M":
    bill=20
    print(f"Medium pizza:$ {bill}")

    if pep=="Y":
        bill+=3
        print(f"Meduim pizza with pepperoni is: $ {bill}")
    else:
        print(f"Bill is :{bill}")

else:
    bill=25
    print(f"Large pizza:$ {bill}")

    if pep=="Y":
        bill+=3
        print(f"Large pizza with pepperoni is: $ {bill}")
    else: 
         print(f"Bill is :{bill}") 


cheese=input("Do you want extra cheese?Y / N")
tt=bill+1
print(f"Total bill is :{tt}")

# -------------------------------------------------------------------------------
#Make love calculator

print("Welcome to love calculator")
name1=input("Whats your name? ")
name2=input("Whats the other one's name? ")
name1lower=name1.lower()
name2lower=name2.lower()
bothname=name1lower+name2lower
tCount=bothname.count('t')+bothname.count('r')+bothname.count('u')+bothname.count('e')
lCount=bothname.count('l')+bothname.count('o')+bothname.count('v')+bothname.count('e')
score=tCount*10+lCount
if score<10 or score>90:
    print(f"Your score is {score},you go together like coke and mentos")
elif score>40 and score<50:
    print(f"Your score is {score},you are alright together")
else:
    print(f"Your score is {score}")


#---------------------------------Treasure island--------------------------------------
print("Welcome to treasure island:")
cho1=input("where would you like to go:Left or Right?  ")
if cho1=="Right":
    print("Game over ")
elif cho1=="Left":
    cho2=input("Swim or Wait")
else:
    print("Please check your input")

if cho2=="Swim":
    print("Game over ")
elif cho2=="Wait":
    cho3=input("Which door,Red,Yellow or Blue")
else:
    print("Please check your input")

if cho3=="Red" or cho3=="Blue":
    print("Game over ")
elif cho3=="Yellow":
    print("You win!")
else:
    print("Please check your input")    

#------------------------------------DAY 3 DONE--------------------------------

