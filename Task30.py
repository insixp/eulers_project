import time

def main():
	current_power = 5
	max_num = 1
	while((9**current_power)*len(str(max_num)) > max_num):
			max_num += 9**current_power
	total_sum = 0
	i = 2
	while(i <= max_num):
		print i
		if(check_if_sum_of_fifth_power_equal(i, current_power)):
			total_sum += i
		i += 1
	print total_sum
	

def check_if_sum_of_fifth_power_equal(num, power):
	str_num = str(num)
	for single_num in str_num:
		num -= int(single_num)**power
	return num == 0
	
if __name__ == "__main__":
	main();