#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""Take a number and print "positive even", "positive odd", "negative" or "zero"""


# In[9]:


num = int (input("enter a num:"))

if num == 0 :
    print("number is zero:")
elif num > 0 and num % 2 == 0:
    print("positive even num")
elif num > 0 and num % 2 != 0:
    print("positive odd num")
else:
    print("negative num")


# In[10]:


"""Movie ticket. Under 5 is free, 5 to 17 pay Rs 100, 18 to 59 pay Rs 200, 60+ pay Rs 120. On
Tuesday, everyone except the free group gets Rs 50 off.
"""


# In[26]:


age = int(input("enter your age :"))
day = input("enter the day name:")


if age <= 5:
    print("ticket is free for you")
elif age <= 17:
    price = 100
elif age <=59:
    price = 200
else:
    price = 120
    

if day.lower() == "tuesday":
    price -= 50
print(price)
    


# In[27]:


"""[Easy] Print the numbers 1 to 10."""


# In[30]:


for i in range(1,11):
    print(i)


# In[38]:


for i in range(1,11):
    print(i * 2)


# In[ ]:


"""Print this pattern for n = 5:"""


# In[39]:


n = 5
for i in range(1,6):
    print("*" * i)
    


# In[40]:


"""Print 10 down to 1, then "Liftoff"."""


# In[41]:


num = 10

while num > 0:
    print("num is:",num)
    num -= 1
print("liftoff")


# In[42]:


"""Take a number and print the sum of its digits (1234 gives 10)"""


# In[56]:


num = int(input("Enter a number: "))
total = 0

while num > 0:
    digit = num % 10
    total = total + digit
    print("number is",total)
    num = num // 10

print("Sum of digits:", total)


# In[67]:


attempts = 0
sec_num = 7

while True :
    guess_num = int(input("enter the number:"))
    attempts += 1
    
    if sec_num > guess_num:
        print("the secret num is too low")
    elif sec_num < guess_num:
        print("the secret num is too high")
    else:
        print("the num is correct")
        break
        
print("total num of attempts:",attempts)       
        


# In[68]:


""" [Easy] Take 2 numbers and print sum, difference, product and division.
[Medium] Check even or odd using %, and print the square using **.
[Hard] Swap a and b without a third variable. Then print a // b and a % b.
"""


# In[69]:


a = 2
b = 3

print(a + b)
print(a - b)
print( a * b)
print(a / b)


# In[72]:


n = 7
print("even", n % 2 == 0)
print("odd", n % 2 != 0)
print(n ** 2)


# In[73]:


a = 2
b = 10

a,b = b,a
print(a  //b)
print(a % b)


# In[74]:


"""Write greet(name) that prints "Hello, name". Then write add(a, b) that returns the sum, and print
the result outside"""


# In[76]:


def greet(name):
    print("hello",name)
greet("San")


# In[77]:


def add(a,b):
    return a + b
result = add(1,3)
print(result)


# In[78]:


"""Write is_prime(n) that returns True or False. Write min_max(numbers) that returns both the
smallest and largest values from a list."""


# In[92]:


n = 7

def is_prime(n):
    if n < 2:
        return False

    for i in range(2,n):
        if n % i == 0:
            return False
    
    return True 

print("is_prime",is_prime(n))


# In[ ]:





# In[ ]:




