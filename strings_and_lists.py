# Name:
# Section:
# strings_and_lists.py

# **********  Exercise 2.7 **********

def sum_all(number_list):
    # number_list is a list of numbers
    total = 0
    for num in number_list:
        total += num

    return total

# Test cases
print "sum_all of [4, 3, 6] is:", sum_all([4, 3, 6])
print "sum_all of [1, 2, 3, 4] is:", sum_all([1, 2, 3, 4])


def cumulative_sum(number_list):
    # number_list is a list of numbers
    # Solution 1
    # cumul=[]
    # for num in number_list:
    #     cumul.append(sum(number_list[:number_list.index(num)+1]))
    # return cumul
    # Solution 2
    # return [sum(number_list[:number_list.index(num)+1]) for num in number_list]
    # Solution 3
    return [sum(number_list[:i+1]) for i in range(len(number_list))]


# Test Cases
print cumulative_sum([4, 3, 6])
# [4, 7, 13].
print cumulative_sum([1, 2, 3, 4])
# [1, 3, 6, 10]
print cumulative_sum([4, 3, 2, 1])
# [4, 7, 9, 10]

# **********  Exercise 2.8 **********

def report_card():
    ##### YOUR CODE HERE #####
    course=[]
    grade=[]
    count=input("How many classes did you take?")
    for i in range(int(count)):
        course.append(raw_input("What was the name of this class?"))
        grade.append(input("What was your grade?"))
    print "................"
    print "Report Card:"
    for i in range(int(count)):
        print course[i] + " - " + str(grade[i])
    print "Overall GPA %s" %(sum(grade)/int(count))

# Test Cases
## In comments, show the output of one run of your function.
# How many classes did you take?2
# What was the name of this class?c
# What was your grade?10
# What was the name of this class?p
# What was your grade?6
# ................
# Report Card:
# c - 10
# p - 6
# Overall GPA 8
# **********  Exercise 2.9 **********

# Write any helper functions you need here.

VOWELS = ['a', 'e', 'i', 'o', 'u']

def pig_latin(word):
    # word is a string to convert to pig-latin
    ##### YOUR CODE HERE ##### 
    if word[0] in VOWELS :
        return word+'hay'
    else:
        return word[1:]+word[0]+'ay'

# Test Cases
print pig_latin("boot")
print pig_latin("image")  


# **********  Exercise 2.10 **********
##### YOUR CODE HERE #####
print [x**3 for x in range(1,11)]
print [x+y for x in ["h","t"] for y in ["h","t"]] 

def fonien(word):
    return [x for x in word if x in ['a', 'e', 'i', 'o', 'u']]
# Test Cases
print fonien("tester")
# **********  Exercise OPT.1 **********
# If you do any work for this problem, submit it here 
VOWELS = ['a', 'e', 'i', 'o', 'u']
def pig_latin(word):
    # word is a string to convert to pig-latin
    ##### YOUR CODE HERE ##### 
    if word[0] in VOWELS :
        return word+'hay'
    else:
        return word[1:]+word[0]+'ay'
def translate():
    phrase=raw_input("please enter a phrase. only words and spaces!!!!")
    phrase=phrase.lower()
    words=phrase.split()
    return [pig_latin(x) for x in words]
