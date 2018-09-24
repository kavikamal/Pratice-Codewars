def xor(a,b):
    if a == b:
        return False
    else:
        return True    

def chromosome_check(sperm):
    if 'Y' in sperm.upper():
        return  'Congratulations! You\'re going to have a son.'
    else:
        return 'Congratulations! You\'re going to have a daughter.'

print chromosome_check('XX')          

"""
The Western Suburbs Croquet Club has two categories of membership, Senior and Open. 
They would like your help with an application form that will tell prospective members which category 
they will be placed.

To be a senior, a member must be at least 55 years old and have a handicap greater than 7. 
In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

Input
Input will consist of a list of lists containing two items each. Each list contains information 
for a single potential member. Information consists of an integer for the person's age 
and an integer for the person's handicap.

Note for F#: The input will be of (int list list) which is a List>

Example Input
[[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]]
Output
Output will consist of a list of string values (in Haskell: Open or Senior) stating whether the respective member is to be placed in the senior or open category.

Example Output
["Open", "Open", "Senior", "Open", "Open", "Senior"]
"""
def openOrSenior(data):  
    return ["Senior" if member[0]>54 and member[1]>7  else "Open" for member in data ]
   

print openOrSenior([[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]])

""" 
Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:

name + " plays banjo" 
name + " does not play banjo"
Names given are always valid strings.

test.assert_equals(areYouPlayingBanjo("martin"), "martin does not play banjo");
test.assert_equals(areYouPlayingBanjo("Rikke"), "Rikke plays banjo");
"""

def areYouPlayingBanjo(name):
    return  '{} banjo'.format(name+' does not play' if name[0].lower() != 'r' else name+' plays')

def abundant_number(num):
    return True if num < sum([i for i in range(1,num) if num%i==0])  else  False

print(abundant_number(18))

def amicable_numbers(n1,n2):
   return True if (sum([i for i in range(1,n1) if n1%i==0]) == n2 and sum([i for i in range(1,n2) if n2%i==0]) == n1)  else False