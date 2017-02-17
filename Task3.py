def main():
	primes 		= [2, 3]
	max_num 	= 100000
	designated_num = 600851475143
	max_prime_num_divide = 0;
	for i in range(2, max_num):
		print i
		if(check_list_highest_divider(i, primes)):
			primes.append(i)
	print "------------------------"
	for i in range(len(primes)):
		print primes[i]
		if(designated_num % primes[i] == 0):
			max_prime_num_divide = primes[i];
	print max_prime_num_divide

def check_list_highest_divider(num, data_tuple):
	prime = True
	for i in range(len(data_tuple)):
		if(num % data_tuple[i] == 0):
			prime = False
	return prime

if __name__ == "__main__":
	main();