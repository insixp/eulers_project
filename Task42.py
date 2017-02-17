def main():
	num_of_triangular_words = 0
	list = []
	with open("Task42_text.txt", "r") as file:
		for i in file.read().split(","):
			list.append(i)
	longest_word = ''
	for word in list:
		if(len(word) > len(longest_word)):
			longest_word = word
	max_num_of_triagulare = len(longest_word) * (ord("Z") - (ord("A") - 1))
	triangular_numbers = triangular_number_list(max_num_of_triagulare)
	for word in list:
		current_sum = 0
		for letter in word:
			current_sum += ord(letter) - (ord("A") - 1)
		if(current_sum in triangular_numbers):
			num_of_triangular_words += 1
	print num_of_triangular_words
	
	
	
	
def triangular_number_list(max_num):
	list = []
	current_value = 1
	current_addition = 2
	while(current_value <= max_num):
		list.append(current_value)
		current_value += current_addition
		current_addition += 1
	return list

	
	
	
if __name__ == "__main__":
	main();