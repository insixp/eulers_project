def main():
	with open("Task8_text.txt", "r") as file:
		str = file.read()
	num_of_nums = 13
	max_product = 0
	for i in range(len(str) - num_of_nums):
		temp_product = product_all_numbers_in_a_string(str, i, num_of_nums)
		if(temp_product > max_product):
			max_product = temp_product
	print max_product
	

def product_all_numbers_in_a_string(hole_str, pos, num_of_nums):
	total_sum = 1
	for i in range(num_of_nums):
		print pos + i - 1
		total_sum *= int(hole_str[pos + i - 1])
	return total_sum
	

if __name__ == "__main__":
	main();