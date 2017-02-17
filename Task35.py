from sieve_of_eratosthenes import *

def main():
	max_num = 1000000
	primes = sieve_of_eratosthenes(max_num)
	print check_if_circular_prime(1, primes)
	return 0
	total_circular_primes = 0
	print len(primes)
	for i in range(len(primes)):
		if(i % 1000 == 0):
			print total_circular_primes
			print i 
		if(check_if_circular_prime(primes[i], primes)):	
			total_circular_primes += 1
	print total_circular_primes

def check_if_circular_prime(num, primes):
	str_num = str(num)
	for i in range(len(str_num)):
		current_str = ""
		for j in range(len(str_num)):
			current_str += str_num[(j + i) % len(str_num)]
		if(not(int(current_str) in primes)):
			return False
	return True
	
	
if __name__ == "__main__":
	main();