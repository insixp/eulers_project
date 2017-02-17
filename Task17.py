def main():
	size_num = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
	tenth_unit = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
	second_tenth = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
	extra_units = ["hundred", "thousand", "and"]
	total_sum = 0
	for i in range(1, 1001):
		if((i / 10) % 10 == 1):
			total_sum += len(second_tenth[i%10])
		else:
			total_sum += len(size_num[i % 10])
			total_sum += len(tenth_unit[(i/10)%10])
		if(not((i/100)%10==0)):
			total_sum += len(extra_units[0])
			total_sum += len(size_num[(i/100)%10])
		if(not((i/100)%10==0) and (not(i%100==0))):
			total_sum += len(extra_units[2])
		if(not((i/1000)%10==0)):
			total_sum += len(extra_units[1])
			total_sum += len(size_num[(i/1000)%10])
	print total_sum
	
if __name__ == "__main__":
	main();