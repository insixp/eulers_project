def main():
	list = [2]
	prime_num = 10001
	check_range = 100000000
	for i in range(3, check_range):
		print str(i) + " - " + str(len(list))
		if(check_list_highest_divider(i, list)):
			list.append(i)
		if(len(list) == prime_num):
			print list
			print list[prime_num - 1]
			return True
	

def check_list_highest_divider(num, data_tuple):
	prime = True
	for i in range(len(data_tuple)):
		if(num % data_tuple[i] == 0):
			prime = False
	return prime
	

if __name__ == "__main__":
	main();