from binascii import *

def main():
	current_sum = 0
	top_num = 1000000
	for i in range(1, top_num):
		if(check_palindrome(i) and check_palindrome(int_to_binary(i, 20))):
			print i
			current_sum += i
	print current_sum

def check_palindrome(num):
	num_str = str(num)
	for i in range(len(num_str)):
		if((i + 1) / len(num_str) <= 0.5):
			if(not(num_str[i] == num_str[len(num_str) - i - 1])):
				return False
	return True
	
def int_to_binary(num, level):
	if(level == 0):
		return num
	binary_result = 0
	current_num = num
	current_level_num = 2**level
	if(num >= current_level_num):
		current_num -= current_level_num
		binary_result += 10**level
	return binary_result + int_to_binary(current_num, level - 1)

if __name__ == "__main__":
	main();