def main():
	list = []
	with open("Task22_text.txt", "r") as file:
		for i in file.read().split(","):
			list.append(i)
	list = sort_names(list)
	list_str = ""
	for word in list:
		list_str += word + "\n"
	with open("result.txt", "w+") as file:
		file.write(list_str)
	result = 0
	for i in range(len(list)):
		temp_result = 0
		for letter in list[i]:
			temp_result += ord(letter) - 64
		result += temp_result * (i + 1)
		if(list[i] == "COLIN"):
			show_last = temp_result * (i + 1)
	print show_last
	print result
	
	
	
def sort_names(name_list):
	for i in range(len(name_list)):
		print i
		current_word = name_list[i]
		location = i
		for j in range(len(name_list) - i):
			curre_check_num = smallest_size(current_word, name_list[i + j])
			for k in range(curre_check_num):
				if(ord(name_list[i+j][k]) < ord(current_word[k])):
					current_word = name_list[i+j]
					location = i + j
					break
				elif(ord(name_list[i+j][k]) > ord(current_word[k])):
					break
				if(k == curre_check_num - 1 and len(name_list[i+j]) == curre_check_num):
					current_word = name_list[i+j]
					location = i + j
		temp_name = name_list[i]
		name_list[i] = current_word
		name_list[location] = temp_name
	return name_list
			
def smallest_size (word1, word2):
	if(len(word1) < len(word2)):
		return len(word1)
	else:	
		return len(word2)
	
	
	
if __name__ == "__main__":
	main();