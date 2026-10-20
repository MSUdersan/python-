#print statement
print("hello world ")

#variable
a = 10
b = 20
print(a + b)

#data tyoe
a = 100
print(type(a))

name ="sudersan"
print(type(name))

c= 100.02
print(type(c))

status = True
print(type(status))

#overwrite
x  = 12
x = "sara"
x = 10.2##overwrite
print(x,type(x))

#var scope l-e-g-b
#local-enclosing-global-builtin,

#local
def order():   ##function
    food = "biriyani"
    print("your food order is:",food) ##print statement and  calling tha var

order()
#enclosing
def mart ():
    discount = 10

    def order_disc ():
        print("applying discount staus:",discount)
    order_disc()

mart()
#global

user_id = "san_19"

def homepage ():
   print("wlc to homepage:",user_id)
homepage()

def profilepage():
    print("wlc to profilepage:",user_id)
profilepage()

#typecasting and typechecking
#type checking
x = "12"
y = "25"
print(type(x))
print(type(y))

#casting
print(int(x)+int(y))

#without casting
print(x + y) # without casting it work like concatination 2 string just combine

#casting
"""
a = "10.2"
print(type(a))
print(int(a)) #it give float in string cant change to int(numeric value in string so it lable as string)
"""
b = 10.2 ## this works bcoz it in a numeric value
print(type(b))
print(int(b))

## change string to float and chnage float to int
a = "10.2"
print(type(a))
print(int(float(a)))

""" 
## a string value cant change to any type of casting  
a = "sara"
print(type(a))
print(int(a)) 
"""

##operator
x = 5 + 10
print(x)

x = 10
y = 5
print(x + y) #add
print(x - y) #sub
print(x * y) #mul
print(x / y) #div
print(x // y) #floor it will use to round off decimal value
print(x % y) #rem
print(x ** y) #mult 5 times based on value

#comparison operator
a = 5
b = 10

print(a == 5) #equal
print(a!= 5) #not equal
print(a < 5) #lesser
print(a > 5) #greater

#logical operator
a = True
b = False
print( a and b)
print(a or b)
print(not a )

#using operator

amt = 600
tax = amt * 0.18              #finding tax amt
totalamt = amt + tax          #after adding taxamt with amt

if totalamt > 1000:          ##after adding tax amt the final amt is greater than 1000 we need give discount 10%
    disc = totalamt * 0.10   ## finding the disc amt
    c = totalamt - disc      ##after that minus the disc amt with final amt
else:
    print("totalamt:",totalamt)
print(c)

age = 65
student =  "yes"

if age >= 65 and student == "yes":
    print("yes discount")
else:
    print("no discount")