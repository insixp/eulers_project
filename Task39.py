from math import *

def main():
	max_num_of_p = 1000
	p = [0] * (max_num_of_p+1)
	for a in range(max_num_of_p):
		for b in range(max_num_of_p):
			c  = calc_hypotenuse(a, b)
			if(a+b+c > max_num_of_p):
				break
			if(check_if_integer(c)):
				p[a+b+int(c)] += 1
	current_max_p = 0
	current_p = 0
	for i in range(len(p)):
		if(p[i] > current_max_p):
			current_p = i
			current_max_p = p[i]
	print current_p
			

def calc_hypotenuse(a, b):
	a_sqare = a*a
	b_sqare = b*b
	c_sqare = a_sqare + b_sqare
	return sqrt(c_sqare)
	
def check_if_integer(num):
	return num == int(num)

if __name__ == "__main__":
	main();