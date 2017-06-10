def computePay(hours,rate):
	try:
		hours=float(hours)
		rate=float(rate)
		if (hours > 40):
			extra=hours - 40
			pay = (40 * rate) + (extra * (1.5 * rate))
		else:
			pay = hours * rate
		print("Pay: "+ str(pay))
	except:
		print("Error, please enter numeric input")

computePay(40,10)
computePay(45,10)
computePay("cd",10)
computePay(50,"xx")