num = None
total = 0
count = 0
anerage = 0
while(True):
	num = input("Enter a number: ")
	if num == 'done':
		if(count > 0):
			average = total / count
			print(str(total), " ", str(count), " ", str(average))
		break;
	try:
		num = float(num)
		count = count + 1
		total = total + num
	except:
		print("Invalid input")
