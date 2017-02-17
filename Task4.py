def main():
	max_num = 0
	for i in range(999):
		for j in range(999):
			if(check_palindrome(j*i) and j*i > max_num):
				max_num = j*i
	print max_num

def check_palindrome(num):
	num_str = str(num)
	for i in range(len(num_str)):
		if((i + 1) / len(num_str) <= 0.5):
			if(not(num_str[i] == num_str[len(num_str) - i - 1])):
				return False
	return True

if __name__ == "__main__":
	main();