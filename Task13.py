def main():
	ten_digits_sum = 0
	with open("Task13_text.txt", "r") as file:
		for data in file.read().split("\n"):
			ten_digits_sum += int(data)
	print ten_digits_sum
			
			
def expo_of_ten(num):
	total_result = 1
	for i in range(num):
		total_result *= 10
	return total_result
		
	
if __name__ == "__main__":
	main();