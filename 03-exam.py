
# coding: utf-8

# 
# # 03-exam: Functions 
# 
# Let's see if you can solve these word problems by creating functions. The function "skeleton" has been set up for you to fill in below the problem description, as well as example outputs of what the function should return given certain inputs. Best of luck, some of these will be challenging! 
# 
# The tasks will start off easy and proceed to get harder and harder.

# ## Task 1
# 
# Create a function that takes in two integers and returns True if their sum is 10, False if their sum is something else.

# In[1]:


def check_ten(n1,n2):
    if n1+n2 == 10:
       return True
    else:
       return False 
        
    pass


# In[2]:


# Example Inputs and Outputs:


# In[3]:


check_ten(10,0)


# In[4]:


check_ten(5,5)


# In[5]:


check_ten(2,7)


# ## Task 2
# Create a function that takes in two integers and returns True if their sum is 10, otherwise, return the actual sum value.

# In[6]:


def check_ten_sum(n1,n2):
    if n1+n2 == 10:
       return True
    else:
       return n1+n2
    pass


# In[7]:


# Example Inputs and Outputs:


# In[8]:


check_ten_sum(10,0)


# In[9]:


check_ten_sum(2,7)


# ## Task 3
# 
# Create a function that takes in a string and returns back the first character of that string in upper case.

# In[10]:


def first_upper(mystring):
    return mystring[0].upper()
    pass


# In[11]:


# Example Inputs and Outputs:


# In[12]:


# Expected return: 'H'
first_upper('hello')


# In[13]:


# Expected return: 'P'
first_upper('person of interest')


# ## Task 4
# Create a function that takes in a string and returns the last two characters. If there are less than two chracters, return the string:  "Error". [Use this link if you need help/hint.](https://stackoverflow.com/questions/7983820/get-the-last-4-characters-of-a-string)

# In[20]:


def last_two(mystring):
    if len(mystring)<2:
        return "Error"
    else:
        return mystring[-2:]
    pass


# In[21]:


# Example Inputs and Outputs:


# In[22]:


# Expected return: 'lo'
last_two('hello')


# In[23]:


# Expected return: 'hi'
last_two('hi')


# In[24]:


# Expected return: 'Error'
last_two('a')


# ## Task 5
# Given a list of integers, return True if the sequence [1,2,3] is somewhere in the list. Hint: Use slicing and a for loop.

# In[25]:


def seq_check(nums):
    for i in range (len(nums)):
        if nums[i]==1 and nums[i:i+3] == [1,2,3]:
            return True
    return False
            
    pass


# In[26]:


# Example Inputs and Outputs:


# In[27]:


# Expected return: True
seq_check([1,2,3])


# In[28]:


# Expected return: True
seq_check([7,7,7,1,2,3,7,7,7])


# In[29]:


# Expected return: False
seq_check([3,2,1,3,2,1,1,1,2,2,3,3,3])


# ## Task 6
# Given two strings, create a function that returns the difference in length between them. This difference in length should always be a positive number (or just 0). Hint: Absolute Value.

# In[30]:


def compare_len(s1,s2):
    return abs(len(s1)-len(s2))
    pass


# In[31]:


# Example Inputs and Outputs:


# In[32]:


# Expected return: 0
compare_len('aa','aa')


# In[33]:


# Expected return: 1
compare_len('a','bb')


# In[34]:


# Expected return: 1
compare_len('bb','a')


# ## Task 7
# Given a list of integers, if the length of the list is an even number, return the sum of the list. If the length of the list is odd, return the max value in that list.

# In[35]:


def sum_or_max(mylist):
    if len(mylist)%2==0:
        return sum(mylist)
    else:
        return max(mylist)
    pass


# In[36]:


# Example Inputs and Outputs:


# In[37]:


# Expected return: 3
sum_or_max([1,2,3])


# In[38]:


# Expected return: 6
sum_or_max([0,1,2,3])


# ## Task 8
# Create a function that takes in a string name (e.g. "James", "Cindy", etc...) and replaces all vowels with the letter x. For our purposes, consider these letters as vowels: [a,e,i,o,u]). Then switch the position of the first and last letters.
# 
# **This task is challenging, break it down into multiple pieces. **

# In[57]:


def replace_and_switch(name):
    result = ''
    for c in name:
        if c.lower() in ['a','e','i','o','u']:
            result += 'x'
        else:
            result+=c

    return result[-1]+result[1:-1]+result[0]
            
    pass


# In[58]:


# Example Inputs and Outputs:


# In[59]:


# Expected return: 'sxmxJ'
replace_and_switch('James')


# In[60]:


# Expected return: 'yxndC'
replace_and_switch('Cindy')


# In[61]:


# Expected return: 'dlfrxx'
replace_and_switch("Alfred")


# ## Great Job! 
# Later on you will combine multiple functions to create large working pieces of code that accomplish complex tasks!
