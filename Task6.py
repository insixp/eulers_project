def main():
	test_num = 100
	print squar_of_sums(test_num) - sum_of_squars(test_num)
	

def sum_of_squars(num):
	sum_of_squars = 0
	for i in range(num + 1):
		sum_of_squars += i*i
	return sum_of_squars

def squar_of_sums(num):
	sum_to_end = 0
	for i in range(num + 1):
		sum_to_end += i
	return sum_to_end*sum_to_end
	

if __name__ == "__main__":
	main();