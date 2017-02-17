def main():
	check_range = 1000000000
	results = []
	upto_num = 20
	for i in range(upto_num, check_range, upto_num):
		if(deviseable_by_all_num_upto(i, upto_num)):
			results.append(i)
			break
	print results
	print len(results)
		

def deviseable_by_all_num_upto(input_num, upto_num):
	for i in range(1, upto_num):
		if(not(input_num % i == 0)):
			return False
	return True
	

if __name__ == "__main__":
	main();