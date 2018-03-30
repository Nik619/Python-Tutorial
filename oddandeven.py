#Calculating if the number is odd or even

number1 =  int(input("Please enter a number"))

number2 = int(input("Please enter a number"))

result  =  number1 % number2

print(result)

if result != 0:
	print("The number is odd")
else:
	print("The number is even")
