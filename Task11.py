def main():
	check_table = []
	with open("Task11_text.txt", "r") as file:
		for line in file.read().split("\n"):
			temp_list = []
			for num in line.split(" "):
				temp_list.append(int(num))
			check_table.append(temp_list)
	max_product = 0
	first_check = find_max_num_of_product_right_and_left(check_table, 4)
	second_check = find_max_num_of_product_up_and_down(check_table, 4)
	third_check = find_max_num_of_product_diagonical_up(check_table, 4)
	fourth_check = find_max_num_of_product_diagonical_down(check_table, 4)
	if(first_check > max_product):	
		max_product = first_check
	if(second_check > max_product):	
		max_product = second_check
	if(third_check > max_product):	
		max_product = third_check
	if(fourth_check > max_product):	
		max_product = fourth_check
	print max_product
	
	

def find_max_num_of_product_right_and_left(table, size):
	max_product = 0
	for rows in table:
		for i in range(len(rows) - size + 1):
			temp_product = 1
			for j in range(size):
				temp_product *= rows[j + i]
			if(temp_product > max_product):
				max_product = temp_product
	return max_product
	
def find_max_num_of_product_up_and_down(table, size):
	result_list = []
	for j in range(len(table[0])):
		temp_list = []
		for i in range(len(table)):
			temp_list.append(table[i][j])
		result_list.append(temp_list)
	return find_max_num_of_product_right_and_left(result_list, size)
	
def find_max_num_of_product_diagonical_up(table, size):
	result_list = []
	result_list_second = []
	cube_size = len(table)
	for i in range(1, len(table) + 1):
		temp_list = []
		for j in range(i):
			temp_list.append(table[j][i - 1 - j])
		for j in range(len(table) - i):
			temp_list.append(0)
		result_list.append(temp_list)
	for i in range(1, len(table)):
		temp_list = []
		for j in range(i):
			temp_list.append(table[len(table) - j - 1][len(table[0]) - 1 - (i - 1 - j)])
		for j in range(len(table) - i):
			temp_list.append(0)
		result_list_second.append(temp_list)
	for i in range(len(result_list_second)):
		result_list.append(result_list_second[len(result_list_second) - 1 - i])
	return find_max_num_of_product_right_and_left(result_list, size)

def find_max_num_of_product_diagonical_down(table, size):
	new_table = []
	for rows in table:
		temp_list = []
		for i in range(len(rows)):
			temp_list.append(rows[len(rows) - 1 - i])
		new_table.append(temp_list)
	find_max_num_of_product_diagonical_up(new_table, size)
	
	
	
if __name__ == "__main__":
	main();