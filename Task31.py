def main():
	ways = 0
	for a in range(0, 201, 200):
		for b in range(0, 201 - a, 100):
			for c in range(0, 201 - (a+b), 50):
				for d in range(0, 201 - (a+b+c), 20):
					for e in range(0, 201 - (a+b+c+d), 10):
						print e
						for f in range(0, 201 - (a+b+c+d+e), 5):
							for g in range(0, 201 - (a+b+c+e+d+f), 2):
								for h in range(0, 201 - (a+b+c+d+e+f+g), 1):
									if(a+b+c+d+e+f+g+h == 200):
										ways += 1
								
	print ways
			
	
if __name__ == "__main__":
	main();