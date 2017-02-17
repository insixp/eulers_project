def main():
	primes = [2]
	max_num = 28123
	i = 3
	while(len(primes) < 500):
		if(check_if_divide_by_element_in_list(i, primes)):
			primes.append(i)
		i += 1
	
	abdundant_nums = []
	for i in range(1, max_num):
		print i
		if(sum_of_list(list_of_divisors(i, primes)) > i):
			abdundant_nums.append(i)
	all_sum_possibilities = all_posible_sums_of_list(abdundant_nums, max_num)
	result = 0
	for i in range(max_num):
		print i
		if(all_sum_possibilities[i] == 0):
			result += i
	print result

def all_posible_sums_of_list(abdundant_nums, max_num):
	list = [0]*(max_num+1)
	for i in range(len(abdundant_nums)):
		print i
		for j in range(len(abdundant_nums)):
			if(abdundant_nums[i] + abdundant_nums[j] <= max_num):
				list[abdundant_nums[i] + abdundant_nums[j]] = 1
			else:
				break
	return list
			
def list_of_divisors(num, primes):
	result = 0
	list = [1]
	for i in range(len(primes)):	
		recursive_sum_of_divisable(num, 1, primes[i], list)
	list = multiply_elements(num, list)
	return list
		
	
def recursive_sum_of_divisable(result, current_num, divisor, list):
	if(result % (current_num*divisor) == 0 and not(current_num*divisor == result)):
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