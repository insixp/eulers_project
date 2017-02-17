from sieve_of_eratosthenes import *

def main():
	max_num = 0
	pandigital_num = 9
	max_num_to_check = 99999
	for i in range(max_num_to_check):
		print i
		generated_num = generate_designated_num(i, 1, 0, 9)
		if(not(len(generated_num) == 9)):
			continue
		current_num = int(generated_num)
		if(is_pandigital_num(generated_num, pandigital_num) and current_num > max_num):
			max_num = current_num
	print max_num

def generate_designated_num(seed, level, current_length, max_length):
	current_level_num = seed*level
	if(current_length + len(str(current_level_num)) >= max_length):
		return str(current_level_num)
	return str(current_level_num) + generate_designated_num(seed, level+1, current_length + len(str(current_level_num)), max_length)
	

def is_pandigital_num(num, num_of_pandigital):
	test_set = set()
	for i in range(len(num)):
		if(int(num[i]) in test_set):
			return False
		test_set.add(int(num[i]))
	if(test_set == set(range(1, num_of_pandigital+1))):
		return True

if __name__ == "__main__":
	main();