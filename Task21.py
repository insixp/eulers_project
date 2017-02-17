def main():
	primes = [2]
	max_num = 10000
	i = 3
	while(len(primes) < 500):
		if(check_if_divide_by_element_in_list(i, primes)):
			primes.append(i)
		i += 1
	
	result = 0
	for i in range(1, max_num):
		temp_num = sum_of_list(list_of_divisors(i, primes))
		if(sum_of_list(list_of_divisors(temp_num, primes)) == i and not (i == temp_num)):
			result += i
			print i
	print result

def list_of_divisors(num, primes):
	result = 0
	list = [1]
	for i in range(len(primes)):	
		recursive_sum_of_divisable(num, 1, primes[i], list)
	list = multiply_elements(num, list)
	return list
		
	
def recursive_sum_of_divisable(result, current_num, divisor, list):
	if(result % (current_num*divisor) == 0):
		list.append(current_num*divisor)
		recursive_sum_of_divisable(result, current_num*divisor, divisor, list)
	else:
		return 0
	return list

def multiply_elements(num, list):
	num_of_elements = len(list)
	for i in range(len(list)):	
		for j in range(len(list) - i):			
			if(num % (list[i]*list[len(list) - 1 - j]) == 0 and not(num == (list[i]*list[len(list) - 1 - j])) and not((list[i]*list[len(list) - 1 - j]) in list) ):	
				list.append(list[i]*list[len(list) - 1 - j])
	if(num_of_elements == len(list)):
		return list
	else:
		list = multiply_elements(num, list)
	return list
	
def sum_of_list(list):
	result = 0
	for i in range(len(list)):
		result += list[i]
	return result
	
def check_if_divide_by_element_in_list(num, data_tuple):
	prime = True
	for i in range(len(data_tuple)):
		if(num % data_tuple[i] == 0):
			prime = False
	return prime
	
	
	
	
if __name__ == "__main__":
	main();