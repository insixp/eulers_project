import math

def sieve_of_eratosthenes(max_num):
	sieve_prime_list = set()
	primes = []
	for i in range(2, int(math.ceil(math.sqrt(max_num)))):
		for j in range(2, int(math.ceil(float(max_num) / i))):
			sieve_prime_list.add(j*i)
	for i in range(2, max_num):
		if(not(i in sieve_prime_list)):
			primes.append(i)
	return primes
	
def sieve_of_eratosthenes_slower(max_num, silent):
	sieve_prime_list = set()
	primes = []
	current_num = 2
	while(current_num < int(math.ceil(math.sqrt(max_num)))):
		if(current_num % 1000 == 0 and not silent):
			print current_num
		current_mul = 2
		while(current_mul < int(math.ceil(float(max_num) / current_num))):
			print current_mul
			sieve_prime_list.add(current_mul*current_num)
			current_mul += 1
		current_num += 1
	for i in range(2, max_num):
		if(not(i in sieve_prime_list)):
			primes.append(i)
	return primes
	
def is_prime(num):
	if(num == 1 or num == 0):
		return False
	upper_limit = int(math.ceil(math.sqrt(num)))
	for i in range(2, upper_limit + 1):
		if(num % i == 0):
			return False
	return True