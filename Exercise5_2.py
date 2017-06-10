num = None
count = 0
total = 0
max = 0
min = 0
while(True):
	num = input("Enter a number: ")
	if num == 'done':
		if(count > 0):
			print(str(total), " ", str(count), " ", str(max), " ", str(min))
		break;
	try:
		num = float(num)
		if count == 0:
			min = num
			max = num
		count = count + 1
		total = total + num
		if num > max:
			max = num
		if num < min:
			min = num
	except:
		print("Invalid input")
