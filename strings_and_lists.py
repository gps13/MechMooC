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
    

# Test Cases
## In comments, show the output of one run of your function.

# **********  Exercise 2.9 **********

# Write any helper functions you need here.

VOWELS = ['a', 'e', 'i', 'o', 'u']

def pig_latin(word):
    # word is a string to convert to pig-latin

    ##### YOUR CODE HERE #####
    return "Not Implemented Yet"    

# Test Cases
##### YOUR CODE HERE #####


# **********  Exercise 2.10 **********
# Test Cases
##### YOUR CODE HERE #####


# **********  Exercise OPT.1 **********
# If you do any work for this problem, submit it here 
