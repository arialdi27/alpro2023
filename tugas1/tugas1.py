batas = int(input("masukan batas angkanya: "))

for i in range(batas):
	print(i + 1, end="")
	fizz = (i + 1 ) % 2 == 0
	buzz = (i + 1 ) % 3 == 0
	
	
	if fizz and buzz:
		print("-->fizz dan buzz") 
		
	elif fizz:
		print("-->fizz")
	elif buzz:
		print("-->Buzz")
	else:
		print("")
				
