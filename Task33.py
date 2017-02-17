def main():
	starting_num1 = 10
	starting_num2 = 10
	max_num1 = 100
	max_num2 = 100
	numinator = 1
	denuminator = 1
	for i in range(starting_num1, max_num1):
		for j in range(starting_num2, max_num2):
			if(i > j):
				continue
			if(i == j):
				continue
			if(i % 10 == 0 and j % 10 == 0):
				continue
			if(i % 11 == 0 and j % 11 == 0):
				continue
			result = is_digit_cancelling_fraction(i, j)
			if(not(result == [] )):
				print result[0] + " - " + result[1]
				numinator *= int(result[0])
				denuminator *= int(result[1])
	print find_lowest_fraction_denuminator(numinator, denuminator)
			
	

def is_digit_cancelling_fraction(num1, num2):
	num1_str = str(num1)
	num2_str = str(num2)
	current_prod = float(num1) / num2
	for i in range(len(num1_str)):
		for j in range(len(num2_str)):
			if(float(num2_str[j]) == 0):
				continue
			if(float(num1_str[i]) / float(num2_str[j]) == current_prod and num1_str[len(num1_str) - i - 1] == num2_str[len(num2_str) - j - 1]):
				return [num1_str[i], num2_str[j]]
	return []
	
def find_lowest_fraction_denuminator(num1, num2):
	current_num1 = num1
	current_num2 = num2
	i = num1
	while(i > 0):
		if(current_num1 % i == 0 and current_num2 % i == 0):
			current_num1 = current_num1 / i
			current_num2 = current_num2 / i
		i -= 1
	return current_num2

def is_divisable_by_all_elements_of_set(num, set):
	for item in set:
		if(not(num % item == 0)):
			return False
	return True
	
if __name__ == "__main__":
	main();