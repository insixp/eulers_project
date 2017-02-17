def main():
	max_collatz = 0
	collatz_num = 0
	for i in range(1, 1000000):
		if(i % 10000 == 0):
			print i
		current_collatz = collatz_sequence(i, 0)
		if(current_collatz > max_collatz):
			max_collatz = current_collatz
			collatz_num = i
	print collatz_num
			
def collatz_sequence(num, level):
	if(num == 1):
		return 1
	if(num % 2 == 0):
		return collatz_sequence(num/2, level + 1) + 1
	else:
		return collatz_sequence(3*num + 1, level + 1) + 1
	
if __name__ == "__main__":
	main();