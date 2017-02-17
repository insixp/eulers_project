def main():
	primes = [2]
	max_num = 2000000
	for i in range(3, max_num):
		print i
		if(check_if_divide_by_element_in_list(i, primes)):
			primes.append(i)
	print primes
	result = 0
	for i in range(len(primes)):
		result += primes[i]
	print result
	

def check_if_divide_by_element_in_list(num, data_tuple):
	prime = True
	for i in range(len(data_tuple)):
		if(num % data_tuple[i] == 0):
			prime = False
	return prime
	

if __name__ == "__main__":
	main();