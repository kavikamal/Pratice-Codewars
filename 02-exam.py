
# coding: utf-8

# # Python Exam 2
#
# Welcome to your second Python Exam!  This test will cover the following topics:
#  - loops
#  - python operators
#  - functions (range, input)
#  - list comprehensions
#
# ## Complete the tasks below:
# ### Use SHIFT+ENTER to move advance and run the code cells.

# ### Task 1
# Use a for-loop and indexing to print out only the words that start with letter `s` (uppercase and lowercase) in this sentence:
#
# *"Superman derives his power from the yellow sun of Earth. Forced under a red sun akin to the red sun of his homeworld, Krypton, or exposed to red sun radiation, Superman rapidly loses his powers, reverting to the stature of a normal human."*
#
# Your output should look like this:
# ```
# Superman
# sun
# sun
# sun
# sun
# Superman
# stature```
#

# In[ ]:


mystring = """
    Superman derives his power from the yellow sun of Earth. 
    Forced under a red sun akin to the red sun of his homeworld, 
    Krypton, or exposed to red sun radiation, Superman rapidly 
    loses his powers, reverting to the stature of a normal human.
    """


# In[1]:


mystring = """
    Superman derives his power from the yellow sun of Earth. 
    Forced under a red sun akin to the red sun of his homeworld, 
    Krypton, or exposed to red sun radiation, Superman rapidly 
    loses his powers, reverting to the stature of a normal human.
    """
string = mystring.split()
for word in string:
    if (word[0] == 's' or word[0] == 'S'):
        print word


# ### Task 2
# Using the same string as previously used, use a for-loop to only print out the words with an even number of characters/letters (including punctuation).
# ```
# Superman
# from
# yellow
# of
# Earth.
# Forced
# akin
# to
# of
# homeworld,
# Krypton,
# or
# to
# radiation,
# Superman
# to
# of
# normal
# human.
# ```

# In[2]:


mystring = """
    Superman derives his power from the yellow sun of Earth. 
    Forced under a red sun akin to the red sun of his homeworld, 
    Krypton, or exposed to red sun radiation, Superman rapidly 
    loses his powers, reverting to the stature of a normal human.
    """
string = mystring.split()
for word in string:
    if len(word) % 2 == 0:
        print word


# ### Task 3
# Use a list comprehension to create a list of every first letter in `mystring`.
# ```
# ['S', 'd', 'h', 'p', 'f', 't', 'y', 's', 'o', 'E', 'F', 'u',
# 'a', 'r', 's', 'a', 't', 't', 'r', 's', 'o', 'h', 'h', 'K',
# 'o', 'e', 't', 'r', 's', 'r', 'S', 'r', 'l', 'h', 'p', 'r',
# 't', 't', 's', 'o', 'a', 'n', 'h']
# ```

# In[3]:


mystring = """
    Superman derives his power from the yellow sun of Earth. 
    Forced under a red sun akin to the red sun of his homeworld, 
    Krypton, or exposed to red sun radiation, Superman rapidly 
    loses his powers, reverting to the stature of a normal human.
    """
string = mystring.split()
char_list = [word[0] for word in string]
print char_list


# ### Task 4
# Use list comprehension to create a list of all the even numbers from 0 to 10.
# ```
# [0, 2, 4, 6, 8, 10]
# ```

# In[4]:


even_list = [i for i in range(0, 11) if i % 2 == 0]
print even_list


# ### Task 5
# Use the range function to create a list of all the even numbers from 0 to 10.
# ```
# [0, 2, 4, 6, 8, 10]
# ```

# In[5]:


even_list = list(range(0, 11, 2))
print even_list


# ### Task 6
# Create a for loop that uses the random library to create a list of 10 random numbers.
# ```
# Example: [95, 69, 33, 40, 92, 65, 9, 69, 91, 94, 85]
# ```

# In[ ]:


import random


# In[6]:


from random import *
randomlist = []
for i in range(10):
    randomlist.append(randint(1, 100))
print randomlist


# ### Task 7
# Use list comprehension and the random library to create a list of 10 random numbers
# ```
# Example: [60, 72, 40, 76, 18, 28, 82, 40, 61, 88, 24]
# ```

# In[7]:


from random import *
random_list = [randint(1, 100) for i in range(10)]
print random_list


# ### Task 8
# Create a while-loop that will ask the user to input an even number. It should keep repeating the request until an even integer is entered. You should only need to expect integers to be passed in,
# if the user provides a string or something else that can't be transformed to an integer with int(), then the loop should break with an error.
#
# NOTE: When working with while-loops with the input() function:
#  - It's very easy to get stuck in an infinite loop, click on Kernel in the top toolbar and select Restart Kernel to fix this.
#  - If you re-run a cell still waiting for an input() it will get stuck with
#  `In [*]` , again select Restart Kernel to fix this.
#
# ```
# Please provide an even number: 3
# Please provide an even number: 5
# Please provide an even number: 7
# Please provide an even number: 2
# Thank you for giving me an even number!
# ```

# In[8]:


print 'Please provide an even number:'
n = input()
while (int(n) % 2 != 0):
    print 'Please provide an even number:'
    n = input()

print 'Thank you for giving me an even number! '


# ## You have completed Exam 2!
