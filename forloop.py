# for [iteration variable] in [sequence]:
#
# range in python is used by loops. range controlls how many loops to control
# a range can have from 1 to 3 arguments
# the arguments that are used is as follows range(start,stop,step)



# 
#
#
#
# in the below example
# we have just provided a single argument assigned to range by default the range would consider the start to 0 
# and the argument assigned would be consider as stop 
#
# the value in range would be passed into the Iteration which is "a" 
# Uppon Printing the Iterated value It would print all the values from an index of 0 to 6.
#

for a in range(6):
	print(a)

print("   ")

# In the Next Example we have defined the starting arguments and Stop arguments
#
# the value in range would be passed into the Iteration which is "i" 
# 
# If the start argument is 1 then it would start prining from 1 and would stop at 4 not 5 since we have said that the 
# range should stop at 5
#

for i in range(1,5):
	print(i)

print("  ")

# In the Next Example we have defined the starting arguments, Stop arguments and Step Argument
#
# The step is used as an incerment or decrement( these are speified by using a - indicator) 
# 
# we have decared the start arugment 0 and the Stop arugment to 10. As for the Step argument is set to 2. 
# The loop would start by printing 0. The Next values that would be printed would be 2 
# This is happened since we have set the STEP arugment to 2. 
# This tells the FOR loop to increment the 0 by 2 the process would carry on till the STOP arugment matches 
#
#


for b in range(0,10,2):
	print(b)


print("   ")


# The same Follows for decrementation but the Step value should have minus symbol
for c in range(40,0,-10):
	print(c)

