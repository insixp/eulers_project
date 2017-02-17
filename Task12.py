import time, math

def main():
	primes = [2]
	i = 3
	while(len(primes) < 500):
		if(check_if_divide_by_element_in_list(i, primes)):
			primes.append(i)
		i += 1
	current_num = 0
	num_of_divisors = 0
	max_divisors = 0
	addition_number = 0
	while(not(num_of_divisors >= 500)):
		addition_number += 1
		current_num += addition_number
		num_of_divisors = num_of_divideable_by_element_in_list(current_num, primes)
		if(num_of_divisors > max_divisors):
			max_divisors = num_of_divisors
		if(current_num % 10000 == 0):
			print max_divisors
	print "result = " + str(current_num)

def num_of_divideable_by_element_in_list(num, primes):
	current_num = 1
	current_num_of_divisors = 1
	i = 0
	while(not(current_num == num) and (i < 7)):
		num_of_productions = recursive_num_of_time_diviseable(num, current_num, primes[i])
		if(not(num_of_productions == 0)):
			current_num *= primes[i]**num_of_productions
			current_num_of_divisors *= num_of_productions+1
		i += 1
	return current_num_of_divisors
		
	
def recursive_num_of_time_diviseable(result, current_num, divisor):
	if(result % (current_num*divisor) == 0):
		recu_result = recursive_num_of_time_diviseable(result, current_num*divisor, divisor)
	else:
		return 0
	return recu_result + 1
	
	
def check_if_divide_by_element_in_list(num, data_tuple):
	prime = True
	for i in range(len(data_tuple)):
		if(num % data_tuple[i] == 0):
			prime = False
	return prime
	
	
	
	
if __name__ == "__main__":
	main();