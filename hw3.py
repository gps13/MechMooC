# Name:
# Section:
# hw3.py

##### Template for Homework 3, exercises 3.1 - ######

# **********  Exercise 3.1 ********** 

# Define your function here
def list_intersection(list1,list2):
    return [num for num in list1 if num in list2]
# sets solution
# def list_intersection(list1,list2):
#     return list(set(list1)&set(list2))

# Test Cases for Exercise 3.1
##### YOUR CODE HERE #####
print list_intersection([1, 3, 5], [5, 3, 1]) == [1, 3, 5]
print list_intersection([1, 3, 6, 9], [10, 14, 3, 72, 9]) == [3, 9]
print list_intersection([2, 3], [3, 3, 3, 2, 10]) == [3, 2] or list_intersection([2, 3], [3, 3, 3, 2, 10]) ==[2, 3]
print list_intersection([2, 4, 6], [1, 3, 5]) ==[]
# **********  Exercise 3.2 **********

# Define your function here
import math
def ball_collide(ball1, ball2):
    ##### YOUR CODE HERE #####
    # x1,y1,r1 = ball1  #part of solution2
    # x2,y2,r2 = ball2  #part of solution2
    return math.sqrt( (ball1[0] - ball2[0]) ** 2 + (ball1[1] - ball2[1]) ** 2)<= ball1[2]+ball2[2]
    # return math.sqrt((x1-x2)**2+(y1-y2)**2) <= r1+r2    #part of solution2

# Test Cases for Exercise 3.2
print ball_collide((0, 0, 1), (3, 3, 1)) # Should be False
print ball_collide((5, 5, 2), (2, 8, 3)) # Should be True
print ball_collide((7, 8, 2), (4, 4, 3)) # Should be True

# **********  Exercise 3.3 **********

# Define your dictionary here - populate with classes from last term
my_classes = {'6.111': 'History', '6.222':'Math','8.444':'Literature'}

def add_class(class_num, desc):
    ##### YOUR CODE HERE #####
    my_classes[class_num]=desc
    # return "Not Yet Implemented"

# Here, use add_class to add the classes you're taking next term
add_class('6.189', 'Introduction to Python')

def print_classes(course):
    ##### YOUR CODE HERE #####
    is_lesson_in=False
    for lesson in my_classes.keys():
        if course ==  lesson[0]:
            print lesson+ ' - ' + my_classes[lesson]
            is_lesson_in =True
    if not is_lesson_in:
        print "No Course %s classes taken" %course
    # return "Not Yet Implemented

# Test Cases for Exercise 3.3
##### YOUR CODE HERE #####
print_classes('6')
print_classes('9')
# **********  Exercise 3.4 **********

NAMES = ['Alice', 'Bob', 'Cathy', 'Dan', 'Ed', 'Frank',
                 'Gary', 'Helen', 'Irene', 'Jack', 'Kelly', 'Larry']
AGES = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]

# Define your functions here
def combine_lists(l1, l2):
    comb_dict = dict(zip(l1, l2))
    return comb_dict

combined_dict = combine_lists(NAMES, AGES)

def people(age):
    return [name for name in combined_dict if combined_dict[name]==age ]

# Test Cases for Exercise 3.4 (all should be True)
print 'Dan' in people(18) and 'Cathy' in people(18)
print 'Ed' in people(19) and 'Helen' in people(19) and\
       'Irene' in people(19) and 'Jack' in people(19) and 'Larry'in people(19)
print 'Alice' in people(20) and 'Frank' in people(20) and 'Gary' in people(20)
print people(21) ==   ['Bob']
print people(22) ==   ['Kelly']
print people(23) ==   []

# **********  Exercise 3.5 **********

def zellers(month, day, year):
    ##### YOUR CODE HERE #####
    dict_of_days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
    num_of_month = [11,12]+range(1,11)
    #combine to create dict_of_months
    dict_of_months=dict(zip(months,num_of_month))
    A=dict_of_months[month[:3].lower()]
    B=day
    D=year/100
    C=year%100
    if A == 11 or A == 12:
        C -= 1
    W=(13*A-1)/5
    X=C/4
    Y=D/4
    Z=W+X+Y+B+C-2*D
    R=Z%7
    if R < 0:
        R += 7
    return dict_of_days[R]

# Test Cases for Exercise 3.5
##### YOUR CODE HERE #####
print zellers("March", 10, 1940) == "Sunday" # This should be True
print zellers("May", 19, 2012) == "Saturday" # This should be True
print zellers("May", 19, 2012) == "Monday" # This should be False