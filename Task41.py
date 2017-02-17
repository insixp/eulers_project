from sieve_of_eratosthenes import *

def main():
	pandigital_num = 9
	range_num = pandigital_num + 1
	current_set = set()
	for a in reversed(range(range_num)):
		current_set.add(a)
		for b in reversed(range(range_num)):
			if(not(b in current_set) or (current_set == set([0]) and b == 0)):
				current_set.add(b)
				for c in reversed(range(range_num)):
					if(not(c in current_set) or (current_set == set([0]) and c == 0)):
						current_set.add(c)
						for d in reversed(range(range_num)):
							if(not(d in current_set)or (current_set == set([0]) and d == 0)):
								current_set.add(d)
								for e in reversed(range(range_num)):
									if(not(e in current_set) or (current_set == set([0]) and e == 0)):
										current_set.add(e)								
										for f in reversed(range(range_num)):
											if(not(f in current_set) or (current_set == set([0]) and f == 0)):
												current_set.add(f)
												for g in reversed(range(range_num)):
													if(not(g in current_set) or (current_set == set([0]) and g == 0)):
														current_set.add(g)
														for h in reversed(range(range_num)):
															if(not(h in current_set) or (current_set == set([0]) and h == 0)):
																current_set.add(h)
																for i in reversed(range(range_num)):
																	if(not(i in current_set) or (current_set == set([0]) and i == 0)):
																		current_set.add(i)
																		current_num = int(str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h)+str(i))
																		print current_num
																		if(is_pandigital_num(str(current_num))):
																			if(is_prime(current_num)):
																				print current_num
																				return 0
																		current_set.remove(i)
																current_set.remove(h)
														current_set.remove(g)
												current_set.remove(f)
										current_set.remove(e)
								current_set.remove(d)
						current_set.remove(c)
				current_set.remove(b)
		current_set.remove(a)
	
def is_pandigital_num(num_in):
	for i in range(len(num_in)):
		if(not(num_in[i] == "0")):
			num = num_in[i:]
			if("0" in num):
				return False
			break
	test_set = set()
	len_of_num = len(num)
	for i in range(len_of_num):
		if(int(num[i]) in test_set):
			return False
		test_set.add(int(num[i]))
	if(test_set == set(range(1, len_of_num + 1))):
		return True
	return False
	

if __name__ == "__main__":
	main();