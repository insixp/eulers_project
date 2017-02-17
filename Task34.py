def main():
	factorialize_result = []
	for i in range(10):
		factorialize_result.append(factorialize(i))
	total_sum = 0
	designated_num = 2540160
	for i in range(3, designated_num):
		if(is_factorialy_curious(i, factorialize_result)):
			print i
			total_sum += i
	print total_sum
			

def is_factorialy_curious(num, factorialize_result):
	str_num = str(num)
	current_num_sum = 0
	for i in range(len(str_num)):
		current_num_sum += factorialize_result[int(str_num[i])]
	if(current_num_sum == num):
		return True
	return False
	
def factorialize(num):
	if(num == 0 or num == 1):
		return 1
	return factorialize(num - 1)*num
	
if __name__ == "__main__":
	main();