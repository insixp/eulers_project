def main():
	max = 0
	num = 0
	for i in range(1, 1000):
		temp = long_division(1, i)
		if(temp > max):
			max = temp
			num = i
		print "max length: " + str(max)
		print "num: " + str(num)
		
	
	
def long_division(num1, num2):
	current_num = ""
	fraction_contr = num1
	fractions_till_now = []
	while(not(fraction_contr in fractions_till_now)):
		fractions_till_now.append(fraction_contr)
		current_num += str(fraction_contr*10 / num2)
		fraction_contr = fraction_contr*10 % num2
	return len(current_num)
	

	
if __name__ == "__main__":
	main();