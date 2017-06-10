try:
	hours=float(input("Enter hours: "))
	rate=float(input("Enter rate: "))
	if (hours > 40):
		extra=hours - 40
		pay = (40 * rate) + (extra * (1.5 * rate))
	else:
		pay = hours * rate
	print("Pay: "+ str(pay))
except:
	print("Error, please enter numeric input")