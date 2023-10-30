#find all numbers for the range 2000 to 3200 that are divisible by 7
# but are not a multiple of 5.
n = []
for i in range(2000, 3201):	#count is increased by 1 because the loop should run until 3200.
#Condition 1
#first condition is whether the number is divisible by 7 or not.
#technically all numbers are divisible by 7 with a remainder. However, here when they say divisible
#what they mean is that whether the remainder is zero or not.
#if (i%7==0): then that number should be added to the list
#The symbol % in python will give the remainder. It won't give the final value.
#Condition 2
#not a multiple of 5 means that the remainder shouln't be equal to zero. For example, cases like 2000, 2005, etc.,
#shouldn't be part of the list. Therefore, 
#if (i%5!=0)  sing != means "NOT EQUAL TO" in python.
# Combine both conditions
	if (i%7==0) and (i%5!=0):
#add the number that meets both the conditions to the list n.
		n.append(str(i))

print(n)

