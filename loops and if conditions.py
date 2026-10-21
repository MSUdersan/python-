#if ,ifelse ,else
#one condition

#if condition
age  = 25

if age >= 25:
    print("you will get an mla seat")
else:
    print("not apllicable")

#elif condition
mark = 50

if mark >= 90 :
    print("grade A")
elif mark >= 70:
    print("grade B")
elif mark >= 50:
    print("grade C")
else:
    print("fail")

#nested if else
age = 17
has_lic = "yes"

if age >= 18:
    if has_lic == "yes":
        print("you can drive")
    else:
        print("you are not allowed to drive")

else:
    print("go and take the lic")

#Question 1: College Exam Eligibility
#Three conditions check pannanum:
# Student registered-ah?
# Attendance 75% or above-ah?
# Fees paid-ah?

std = "reg"
attendance = 75
fees = "no"

if std == "reg":
    if attendance >= 75:
        if fees == "paid":
            print("you are eligible for exam")
        else:
            print("pay the fees amt")
    else:
        print("your attedance is low")
else:
    print("you are not register")

#1 if 2 condition use logical operator
mark = 50
attedance = 75

if mark >= 75 and attendance >=75:
    print("allowed for exam")
else:
    print("not allowed for exam")

order_amt = 800
days = "sun"
membership = "yes"

if (order_amt >= 1000 and days in ["sat","sun"]) or (membership == "yes"):
    print("you are eligible for discount")
else:
    print("you are not eligible for discount")

#looping

#for loop
names = ["san","sara","naaz","karan"]

for test in names:
    print(test.upper())

for i in range ( 1 ,6):
    print(2 * i)

marks = [80, 65, 90, 45]

for mark in marks:
    print(mark)

h = "hello"

for s in range(6):
    print(h)

m = "sara"
for s in range(6):
    print(m)
"""
#while loop
correct_pin = "1234"
enter_pin = " "

while enter_pin != correct_pin:
    enter_pin = input("enter correct pin : ")

print("access granted")
"""
# break
num = [ 1,2,3,4,5,6,7,8,9]

for i in num:
    if i == 5:
        break
    print(i)

#continue
n = [10,-5,7,9,-3]

for i in n:
    if i < 0 :
        continue
    print(i)

fruits = ["apple", "banana", "orange", "grapes"]
for fr in fruits:
    if fr == "orange":
        continue
    print(fr)

#while loop
count = 5

while count > 0:
    print("countdown", count)
    count -= 1
print("times up")

items = []
while True:
    item = input("add items(type done for finish ):")
    if item.lower() == "done":
        break

    items.append(item)
print("item in carts:",items)
