from sieve_of_eratosthenes import *

def main():
	print is_pandigital_num(1928374756)
	
def is_pandigital_num(num):
	test_set = set()
	len_of_num = len(num)
	for i in range(len_of_num):
		if(int(num[i]) in test_set):
			return False
		test_set.add(int(num[i]))
	if(test_set == set(range(1, len_of_num))):
		return True
	

if __name__ == "__main__":
	main();