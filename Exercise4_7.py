def computeGrade(score):
	if (score < 0.0) or (score > 1.0):
		print("Bad score")
	elif (score >= 0.9):
		print("A")
	elif (score >= 0.8):
		print("B")
	elif (score >= 0.7):
		print("C")
	elif score >= 0.6:
		print("D")
	else:
		print("F")
		
try:
	score = float(input("Enter score between 0.0 and 1.0: "))
	computeGrade(score)
except:
	print("Enter a numeric value")
