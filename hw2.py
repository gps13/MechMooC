# Name:gps13
# Section:
# hw2.py

##### Template for Homework 2, exercises 2.0 - 2.5  ######

# **********  Exercise 2.0 ********** 

def f1(x):
    print x + 1

def f2(x):
    return x + 1

# **********  Exercise 2.1 ********** 

# Define your function here
##### YOUR CODE HERE #####
def rpsinput(player1,player2):
	correct=["rock", "paper", "scissors"]
	win_cond={"rr":"00", "rp":"01", "rs":"10", "pr":"10", "pp":"00",
	 "ps":"01","sr":"01", "sp":"10","ss":"00"}
	if player1 not in correct and player2 not in correct:
		return "Selections not valid"
	else:
		print player1 , player2
		if win_cond[player1[0]+player2[0]]=="00":
			return "Its a tie"
		elif win_cond[player1[0]+player2[0]]=="10":
			return "Player1 wins"
		else:
			return "Player2 wins"
# Test Cases for Exercise 2.1
print rpsinput("paper", "rock")
print
print rpsinput("rock", "rock")
print
print rpsinput("paper", "scissors")
# ********** Exercise 2.2 ********** 

# Define is_divisible function here
##### YOUR CODE HERE #####
def is_divisible(m,n):
	return m%n==0 if n!=0 else "do not divide with 0"
# Test cases for is_divisible
## Provided for you... uncomment when you're done defining your function

print is_divisible(10, 5)  # This should return True
print is_divisible(18, 7)  # This should return False
print is_divisible(42, 0)  # What should this return?

# Define not_equal function here
##### YOUR CODE HERE #####
def not_equal(a,b):
	return not a==b
# Test cases for not_equal
print "g" != "d"
print not_equal("g","d")
print not_equal(1,2)
print not_equal(1,1)

# ********** Exercise 2.3 ********** 

## 1 - multadd function
##### YOUR CODE HERE #####
def multadd(a,b,c):
	return a*b+c

## 2 - Equations
##### YOUR CODE HERE #####
import math

# Test Cases
angle_test = multadd(0.5, math.cos(math.pi/4),math.sin(math.pi/4))
print "sin(pi/4) + cos(pi/4)/2 is:"
print angle_test

ceiling_test =multadd(2, math.log(12,7), math.ceil(276/19))
print "ceiling(276/19) + 2 log_7(12) is:"
print ceiling_test

## 3 - yikes function
##### YOUR CODE HERE #####
def yikes(x):
	return multadd(x,math.e**(-x),math.sqrt(1-math.e**(-x)))
# Test Cases
x = 5
print "yikes(5) =", yikes(x)

# ********** Exercise 2.4 **********

## 1 - rand_divis_3 function
##### YOUR CODE HERE #####
import random
import math
def rand_divis_3():
	return random.randint(0,100)%3==0
# Test Cases
##### YOUR CODE HERE #####
print rand_divis_3()
print rand_divis_3()
print rand_divis_3()

## 2 - roll_dice function - remember that a die's lowest number is 1;
                            #its highest is the number of sides it has
##### YOUR CODE HERE #####
def roll_dice(sides_of_dice,dice_to_roll):
	for i in range(1,dice_to_roll+1):
		print random.randint(1,sides_of_dice)
	return "That's all!"
# Test Cases
print roll_dice(6,3)  
print roll_dice(8,2)
print roll_dice(12,1)                        

# ********** Exercise 2.5 **********

# code for roots function
##### YOUR CODE HERE #####   

# Test Cases
##### YOUR CODE HERE #####   
