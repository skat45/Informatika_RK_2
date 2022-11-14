""" Number 1 Ticket 2 """

file_in = open('stdin.txt', 'r')
numbers = file_in.read().split(' ')
file_in.close()
for i in range(len(numbers)):
	numbers[i] = float(numbers[i])

muliply = 1
negative_here = False

for i in numbers:
	if i < 0:
		muliply *= i
		negative_here = True

file_out = open('stdout.txt', 'w')

if negative_here:
	file_out.write(str(muliply))
else:
	file_out.write("You haven't enter the negative number")

file_out.close()
