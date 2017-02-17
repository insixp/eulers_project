def main():
	total_sum = 0
	pandigital_numn = 9
	prod_pandigital_num = set([])
	for i in range(1, 1000):
		print i
		for j in range(0, 1001):
			if(is_pandigital_num(str(i) + str(j) + str(j*i), pandigital_numn)):
				prod_pandigital_num.add(i*j)
	for i in range(1000, 10000):
		print i
		for j in range(1, 10):
			if(is_pandigital_num(str(i) + str(j) + str(j*i), pandigital_numn)):
				prod_pandigital_num.add(i*j)
	print prod_pandigital_num
	print "phase 2"
	for num in prod_pandigital_num:
		total_sum += num
	print total_sum

def is_pandigital_num(num, num_of_pandigital):
	test_set = set()
	for i in range(len(num)):
		if(int(num[i]) in test_set):
			return False
		test_set.add(int(num[i]))
	if(test_set == set(range(1, num_of_pandigital+1))):
		return True
					
	
	
if __name__ == "__main__":
	main();