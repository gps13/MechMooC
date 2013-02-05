import time
import calendar
f_name=raw_input("Enter your first name: ")
#l_name=raw_input("Enter your last name: ")
print ("Enter your date of birth:")
mo=raw_input("month: ")
A = time.strptime(mo[:3], "%b").tm_mon
if A >=3:
	A-=2
	C=0
else:
	A+=10
	C = -1

#print month
B=input("Day: ")
wholeyear=raw_input("year: ")
D=int(wholeyear[:2])
C+=int(wholeyear[2:])

W=(13*A-1)/5
X=C/4
Y=D/4
Z=W+X+Y+B+C-2*D
R=Z%7
print R

if R>0:
	print calendar.day_name[R-1]
else:
	print calendar.day_name[6]