# In Python I don`t to Define type , but if i want then i can

x = int (10);
y = str ("sakin");
print(type (x));
print(type (y));


a, b, c = "Orange", "Banana", "Cherry"
print(a)
print(b)
print(c)


name1 , name2, name3 = "Sakin", "Mahid", "Abir"
print(name1,name2,name3)


score1 = score2 = score3 = 100
print(score1,score2,score3)

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
fruit1,fruit2,fruit3 = fruits
print(fruit1,fruit2,fruit3)

#Assignment  Operator
count1 = 100
count2=200
print(count1+count2) #300
print(count1,count2)# 100 200


# Global Variables
"""
Variables that are created outside of a function (as in all of the examples above) are known as global variables.
Global variables can be used by everyone, both inside of functions and outside.
"""

item="I LOVE BANGLADESH" #Global Scope
def myFun():
    item = "I LOVE BAN"  #Function Scope
    print(item)
myFun()

print(item)
 
 # Global variable De-clearation
def myFunction():
    global z # z is now a Global Variable
    z = "I'm the Global Scope"
myFunction() 
print(z)      
