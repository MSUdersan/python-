#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello world")


# In[2]:


""" if / else / elif
1. Take a number and print whether it is positive, negative, or zero."""


# In[5]:


num = int(input("enter the num:"))

if num > 0:
    print("The enter num is positive")
elif num < 0 :
     print("The enter num is negative")
else:
     print("The enter num is zero")


# In[13]:


"""Take a year and check whether it is a leap year."""


# In[8]:


year = int(input("enter the year:"))

if year % 400 ==0:
    print("it is leap year")
elif year % 100 != 0:
    print("it is not a leap year")
elif year % 4 ==0:
    print("it is leap year")
else:
    print("not a leap year")


# In[9]:


"""Take marks (0-100) and print the grade: 90+ is A, 75-89 is B, 50-74 is C, below 50 is Fail.
"""


# In[12]:


marks = int(input("enter the marks:"))

if marks > 90:
    print("A Grade")
elif marks >= 75:
    print("B Grade")
elif marks >= 50:
    print("C Grade")
else:
    print("fail")
    


# In[14]:


"""Take three numbers and print the largest one without using max()."""


# In[21]:


a = int(input("enter the num:"))
b = int(input("enter the num:"))
c = int(input("enter the num:"))

if a >= b and a >= c:
    print("A is greater")
elif b >= a and b >= c:
    print("B is greater")
else:
    print("c is greater")


# In[22]:


"""Build a simple calculator: take two numbers and an operator (+ - * /), and handle division
by zero.
"""


# In[25]:


a = float(input("enter the num:"))
b = float(input("enter the num:"))
op = input ( "enter the op (+ - * /):")

if op ==  "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b == 0:
        print("enter value is in correct")
    else:
        print(a / b)
else:
    print("enter op is invalid")
    



# In[26]:


"""2. Nested if
1. Take age and whether the person has a ticket (yes/no). If age is 18+, check for a ticket and
print "Enter" or "Buy ticket". Otherwise print "Not allowed"."""


# In[33]:


age = int(input("enter the age:"))
hav_ticket = input("enter yes or no:")

if age > 18:
    if hav_ticket.lower() == "yes":
        print("you can enter")
    else:
        print("pls buy ticket")
else:
    print("not allowed")


# In[34]:


"""2. Take a username and password. If the username is correct, check the password. Print
different messages for a wrong username and a wrong password."""


# In[38]:


username = input("enter a username:")
password = input("enter a password:")

if username == "san123":
    if password =="1234":
        print("acess granted")
    else:
        print("wrong password")
else:
    print("wrong username")


# In[39]:


"""3. Take a number. If it is positive, check whether it is even or odd, and whether it is also divisible
by 5."""


# In[43]:


num = int(input("enter a num:"))

if num > 0:
    if num % 2 == 0:
        print("it is a even num")
    else:
        print("it is odd num")
        
    if num % 5 == 0:
        print("it can div by 5")
    else:
        print("not div by 5")
else:
    print("it is a negative num")


# In[44]:


""" ATM simulation: check that the PIN is correct, then that the balance is sufficient, then print the
new balance."""


# In[66]:


pin = input("enter thr pin:")
balance = 10000

if pin == "1234":
    print("the pin correct")
    amount = int(input("enter the amount:"))
    
    if amount <= balance:
        print("The bal is sufficient")
    else:
        print("the bal is insufficient")
        
        new_bal = balance - amount
        print("the new bal is:",new_bal)
        
else:
    print("the pin is wrong")
        
     
    


# In[67]:


"""3. for loop
1. Print numbers 1 to 20"""


# In[68]:


for i in range(1,21):
    print(i)


# In[69]:


"""2. Print the multiplication table of any number"""


# In[70]:


for i in range( 1,11):
    print(i * 3)


# In[71]:


"""Find the sum of all numbers from 1 to n"""


# In[82]:


n = 10
total = 0

for num in range (1 , n + 1):
    total = total + num
print(total)


# In[1]:


"""Print only the even numbers between 1 and 50."""


# In[4]:


for n in range(1,51):
    if n % 2 == 0:
        print("even num are:",n)


# In[23]:


"""REV STRING"""


# In[5]:


name = "hello san"
rev = " "

for n in name:
    rev = n + rev
print(rev)
    


# In[6]:


"""Count the vowels in a string."""


# In[15]:


l = "one moon one sun one san"
count = 0

for n in l :
    if n in "aeiou":
        count = count + 1
        
print(count)
        


# In[ ]:


"""Print this pattern:
*
**
***
****   """


# In[17]:


for i in range(1,5):
    print(i * "*")


# In[22]:


n = 7

a = 0
b= 1 

for i in range(n):
    print(a)
    a , b = b , a + b


# In[24]:


"""4. while loop
1. Print numbers 10 down to 1.
2. Keep asking for a password until the user enters the correct one.
3. Find the sum of the digits of a number (for example 1234 gives 10).
4. Reverse a number using a while loop.
5. Check whether a number is a palindrome.
6. Number guessing game: the computer picks a number, you keep guessing, and it says "too
high" or "too low".
7. Use break and continue to print numbers 1 to 20, skip multiples of 3, and stop at 15"""


# In[26]:


""""whileloop"""""
""""Print numbers 10 down to 1."""


# In[28]:


n = 10

while n >= 1:
    print(n)
    n = n - 1
    


# In[29]:


"""Keep asking for a password until the user enters the correct one."""


# In[1]:


crt_pass = "1234"
enter_pass = " "

while enter_pass != crt_pass:
    enter_pass = input("enter your pass:")
print("access granted ")
    


# In[ ]:


"""Find the sum of the digits of a number (for example 1234 gives 10)"""


# In[1]:


num = 1234
total = 0

while num > 0:
    digit = num % 10
    total = total + digit
    num = num // 10
print(total)
    


# In[2]:


"""Reverse a number using a while loop."""


# In[6]:


num = 12345
rev = 0

while num > 0 :
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print(rev)


# In[12]:


num = int(input("enter the num:"))
original = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print(rev)

if original == rev:
    print("the num is palindrome")
else:
    print("the given num is not palindrome")


# In[13]:


"""Number guessing game: the computer picks a number, you keep guessing, and it says "too
high" or "too low".
"""


# In[1]:


num1 = 50
num = int(input("enter the num:"))

while num != num1:
    if num > num1:
        print("it too high")
    else:
        print("its too low")
    num = int(input("Try again: "))

print("Correct!")


# In[2]:


"""Part 1: for loop
Use a for loop when you know how many times the loop should run.
Easy
Q1. Print the numbers from 1 to 10.
Hint: range(1, 11)
Q2. Print the even numbers 2, 4, 6, ... 20.
Hint: range(2, 21, 2)
Q3. Print the multiplication table of 5 (5 x 1 = 5 ... 5 x 10 = 50).
Q4. Print your name 5 times.
Medium
Q5. Find the sum of the numbers from 1 to 100.
Hint: keep a total variable and add to it
Q6. Print the numbers from 10 down to 1.
Hint: range(10, 0, -1)
Q7. Find the factorial of 5 (5 x 4 x 3 x 2 x 1).
Q8. Given nums = [3, 8, 1, 9, 4], print only the numbers greater than 5.
Hint: use if inside the loop"""


# In[3]:


for i in range(1,11):
    print(i)


# In[4]:


"""Print the even numbers 2, 4, 6, ... 20."""


# In[5]:


for i in range(1,21):
    if i % 2 == 0:
        print("the num is even:",i)


# In[6]:


for i in range(1,11):
    print( i * 5)


# In[10]:


for i in range(5):
    print("sudersan")


# In[11]:


""" Find the sum of the numbers from 1 to 100.
"""


# In[16]:


num = 100
total = 0

for num in range(1, num + 1):
    total = total + num
print(total)


# In[17]:


"""Print the numbers from 10 down to 1."""


# In[5]:


for i in range(10,0,-1):
    print(i)
    


# In[6]:


"""Find the factorial of 5 (5 x 4 x 3 x 2 x 1)."""


# In[10]:


num = 5
fact = 1

for n in range(1,num+1):
    fact = fact * n        1*5=5,
print(fact)


# In[12]:


"""""""Q8. Given nums = [3, 8, 1, 9, 4], print only the numbers greater than 5.
""""Hint: use if inside the loop""""""""""""""""""


# In[17]:


nums = (3, 8, 1, 9, 4)

for n in nums:
    if n > 5:
        print("the num is:",n)


# In[18]:


"""Part 2: while loop
Use a while loop when you keep going until a condition changes.
Easy
Q9. Print the numbers from 1 to 10 using while.
Hint: do not forget i = i + 1
Q10. Print the numbers from 10 down to 1 using while.
Q11. Start at 1 and keep doubling while the number is less than 100 (1, 2, 4, 8 ...).
Medium
Q12. Count the digits of a number. For example 12345 gives 5.
Hint: divide by 10 using //
Q13. Find the sum of the digits of a number. For example 123 gives 6.
Hint: n % 10 gives the last digit
Q14. Reverse a number. For example 1234 gives 4321.
Q15. Keep asking the user for a password until they type "python".
Hint: while input(...) != "python""""


# In[1]:


num = 1
total = 0

while num <= 10:
    print(num)
    num = num + 1

    
    


# In[ ]:




