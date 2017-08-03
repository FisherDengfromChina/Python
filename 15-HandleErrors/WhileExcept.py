while True:
	try:
		x=int(input("Please enter a number:"))
		print(x)
		break
	except ValueError:
		print("Oops! That was not a valid number, try again")
#print(x)