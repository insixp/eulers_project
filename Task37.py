from sieve_of_eratosthenes import *

def main():
	max_num_of_trancatable 		= 11
	current_max_num_of_primes 	= 20000
	current_stage 				= 10
	truncatable_primes_list 	= []
	primes 						= []	
	while(len(truncatable_primes_list) < max_num_of_trancatable):
		primes = sieve_of_eratosthenes(current_max_num_of_primes)
		for i in range(current_stage, current_max_num_of_primes):
			print i
			if(check_if_truncatably_prime(i, primes)):
				truncatable_primes_list.append(i)
		if(len(truncatable_primes_list) == max_num_of_trancatable):
			break
		if(current_max_num_of_primes % 100000 == 0 and not(current_max_num_of_primes == 100000)):
			current_stage = current_max_num_of_primes + 100000
			current_max_num_of_primes += 120000
			continue
		if(current_max_num_of_primes % 10000 == 0):
			current_stage = current_max_num_of_primes + 10000
			current_max_num_of_primes += 20000
	total_sum = 0
	for i in range(len(truncatable_primes_list))
		total_sum += truncatable_primes_list[i]
	print total_sum

def check_if_truncatably_prime(num, primes):
	total_nums = []
	for i in left_to_right_truncate(num):
		total_nums.append(i)
	for i in right_to_left_truncate(num):
		total_nums.append(i)
	for i in range(len(total_nums)):
		if(not(total_nums[i] in primes)):
			return False
	return True

def left_to_right_truncate(num):
	current_str = str(num)
	truncate_list = []
	for i in range(len(current_str)):
		truncate_list.append(int(current_str[i:]))
	return truncate_list

def right_to_left_truncate(num):
	current_str = str(num)
	truncate_list = []
	for i in range(1, len(current_str)):
		truncate_list.append(int(current_str[0:i]))
	return truncate_list

if __name__ == "__main__":
	main();