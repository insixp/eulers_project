def main():
	get_lexo_permutation_index_num(1000000, 10)
		
def get_lexo_permutation_index_num(num, num_of_digits):
	list = []
	result = ""
	for i in range(num_of_digits):
		list.append(i)
	for i in range(num_of_digits):
		current_num = (num - 1) % factorial(num_of_digits - i)
		num_of_parts = factorial(num_of_digits - (i + 1))
		current_position = current_num / num_of_parts;
		print current_position
		result += str(list[current_position])
		print list
		del list[current_position]
	print result
	
def factorial(num):
	if(num == 1 or num == 0):
		return 1
	return factorial(num - 1)*num

	
if __name__ == "__main__":
	main();