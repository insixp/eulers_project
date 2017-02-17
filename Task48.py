

def main():
    total_sum = 0
    max_num = 1000

    for i in range(max_num+1):
        total_sum += i**i
        print i

    print (total_sum - 1) % 10000000000


if __name__ == "__main__":
	main();