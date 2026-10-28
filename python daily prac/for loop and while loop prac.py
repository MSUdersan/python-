#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""Level 1: Basics
1. Print numbers from 1 to 10.
2. Print even numbers from 1 to 20 (use step in range).
3. Take a number n from the user and print its multiplication table up to 10.
Example: 5 x 1 = 5, 5 x 2 = 10, ..."""


# In[2]:


for i in range(1,11):
    print(i)


# In[3]:


for i in range(1,21):
    if i % 2 == 0:
        print("the num is :" , i)


# In[4]:


for i in range(1,11):
    print(i * 5)


# In[5]:


"""Level 2: Calculations
4. Find the sum of all numbers from 1 to 100.
5. Find the factorial of a number given by the user.
Example: 5! = 120
6. Print numbers from 10 to 1 in reverse (countdown)."""


# In[9]:


total = 0

for i in range(1,101):
    total = total + i
    
print(total)
    


# In[10]:


"""5. Find the factorial of a number given by the user.
Example: 5! = 120
"""


# In[15]:


num = 5
fact = 1

for i in range(1, num + 1):
    fact = fact * i
    print(fact)


# In[16]:


"""Print numbers from 10 to 1 in reverse (countdown)."""


# In[17]:


for i in range(10,0,-1):
    print(i)


# In[18]:


"""7. Print the numbers from 1 to 30 that are divisible by 3 (3, 6, 9, ...).
8. Print the square of each number from 1 to 10.
Example: 1 -> 1, 2 -> 4, 3 -> 9
"""


# In[19]:


for i in range(1,31):
    if i % 3 == 0:
        print("the num is div by 3 : ", i)


# In[20]:


""""8. Print the square of each number from 1 to 10.
Example: 1 -> 1, 2 -> 4, 3 -> 9
"""


# In[22]:


for i in range(1,11):
    print(i, "- > ",i * i)


# In[23]:


"""9. Print this pattern:
*
**
***
****
*****
10. Print all prime numbers from 1 to 50 (nested for loop needed)."""


# In[24]:


for i in range(1,6):
    print(i * "*")


# In[31]:


for num in range(2,51):
    is_prime = True
    
    for i in range(2,num):
        if num % i == 0:
            is_prime = False
            break
            
    if is_prime:
        print(num)


# In[32]:


"""Level 1: Basics
1. Print numbers from 1 to 10 using a while loop.
2. Print numbers from 10 to 1 in reverse (countdown).
3. Print even numbers from 1 to 20"""


# In[1]:


num = 1 

while num <= 10:
    print(num)
    num = num + 1


# In[2]:


"""Print numbers from 10 to 1 in reverse (countdown)."""


# In[5]:


num = 10

while num >= 1:
    print(num)
    num = num - 1


# In[6]:


""""3. Print even numbers from 1 to 20"""


# In[2]:


num = 1

while num <= 20:
    if num % 2 == 0:
        print(num)
    num = num + 1


# In[3]:


"""Level 2: Calculations
4. Find the sum of all numbers from 1 to 100 using a while loop.
5. Take a number from the user and find its factorial.
6. Take a number from the user and print its multiplication table up to 10"""


# In[1]:


num = 1
total = 0

while num <= 100:
    total = total + num
    num = num + 1
print(total)


# In[2]:


"""Take a number from the user and find its factorial."""


# In[2]:


num = int(input("enter the num"))
fact = 1

while num >= 1:
    fact = fact * num
    num = num - 1 
print(fact)


# In[6]:


"""6. Take a number from the user and print its multiplication table up to 10""""""


# In[3]:


num = int(input("enter the num :"))
mul = 1

while mul <= 10:
    muls = num * mul
    print(muls)
    mul = mul + 1


# In[4]:


"""Level 3: Digit Logic
7. Take a number from the user and count how many digits it has.
Example: 4567 has 4 digits.
8. Take a number from the user and find the sum of its digits.
Example: 4567 gives 4 + 5 + 6 + 7 = 22.
9. Take a number from the user and reverse it.
Example: 1234 becomes 4321.
"""


# In[5]:


num = int(input("enter the num :"))
count = 0

while num > 0:
    num = num // 10
    count = count + 1
print(count)


# In[6]:


"""Take a number from the user and find the sum of its digits.
Example: 4567 gives 4 + 5 + 6 + 7 = 22."""


# In[7]:


num = int(input("enter the num"))
total = 0

while num > 0:
    nums = num % 10 
    total = total + nums
    num = num // 10
print(total)


# In[8]:


"""Take a number from the user and reverse it.
Example: 1234 becomes 4321."""


# In[12]:


num = int(input("enter the num"))

while num > 0:
    nums = num % 10
    print(nums)
    num = num // 10

    


# In[13]:


"""Level 4: Thinking Question
10. Keep asking the user to guess a secret number (7) until they guess it correctly."""


# In[2]:


sec_num = 7
num = int(input("enter the num:"))

while num != sec_num :
    if num > 7:
        print("the num is high")
    else:
        print("the num is low")
    num = int(input("enter the num:"))
   
    

print("the num is correct")


# In[ ]:





# In[ ]:




