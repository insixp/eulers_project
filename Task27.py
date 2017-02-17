import time

def main():
	max_number_b 		= 1000
	max_number_a		= 1000
	num_of_primes_check = 1000
	b_options			= []
	current_a 			= 0
	continues_strike	= 80

	t = time.time()
	print "phase 1"
	
	for i in range(40):
		if(euler_form(i, 1, 41) < 1000):
			b_options.append(euler_form(i, 1, 41))
	
	print "phase 2"
	primes = [2]
	i = 3
	while(len(primes) < num_of_primes_check):
		if(check_if_divide_by_element_in_list(i, primes)):
			primes.append(i)
		i += 1
	
	print "phase 3"
	max_continues_primes = 0
	for j in reversed(range(len(b_options))):
		print b_options[j]
		for i in range(-1 * max_number_a, max_number_a):	
			curr_num_of_continues_primes = num_of_continues_primes(primes, i, b_options[j])
			if(curr_num_of_continues_primes > max_continues_primes):
				product = i*b_options[j]
				max_continues_primes = curr_num_of_continues_primes
				a = i
				b = b_options[j]
	print "product: " + str(product)
	print "max_continues_primes: " + str(max_continues_primes)
	print "a: " + str(a)
	print "b: " + str(b)
	print "time: " + str(time.time() - t)
	
	
def check_if_divide_by_element_in_list(num, data_tuple):
	prime = True
	for i in range(len(data_tuple)):
		if(num % data_tuple[i] == 0):
			prime = False
	return prime
	
def num_of_continues_primes(primes, a, b):
	i = 0
	while(euler_form(i, a, b) in primes):
		i += 1
	return i
		

def euler_form(n, a, b):
	return (n*n + a*n + b)
	
if __name__ == "__main__":
	main();