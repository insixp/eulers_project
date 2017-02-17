import time

def main():
	max_a = 100
	max_b = 100
	total_nums = set()
	for i in range(2, max_a + 1):
		for j in range(2, max_b + 1):
			print str(i) + "^" + str(j)
			total_nums.add(i**j)
	print len(total_nums)
	

	
if __name__ == "__main__":
	main();