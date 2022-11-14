""" Number 1 Ticket 2 """

numbers = input('Enter numbers: ').split(' ')
for i in range(len(numbers)):
	numbers[i] = int(numbers[i])

muliply = 1
negative_here = False

for i in numbers:
	if i < 0:
		muliply *= i
		negative_here = True

if negative_here:
	print(muliply)
else:
	print("You haven't enter the negative number")
