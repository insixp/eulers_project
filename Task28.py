import time

def main():
	width = 1001
	height = 1001
	total_num_in_spiral = width * height
	
	current_num = 1
	current_jump = 0
	d = 0
	total_sum = 0
	while (current_num <= total_num_in_spiral):
		total_sum += current_num
		if(d % 4 == 0):
			current_jump += 2
		d += 1
		current_num += current_jump
	print total_sum

def euler_form(n, a, b):
	return (n*n + a*n + b)
	
if __name__ == "__main__":
	main();