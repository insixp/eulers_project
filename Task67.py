def main():
	piramid = []
	with open("Task67_text.txt", "r") as file:
		for line in file.read().split("\n"):
			temp_line = []
			for word in line.split(" "):
				temp_line.append(int(word))
			piramid.append(temp_line)
	print sum_shortest_piramid_path(piramid)
	
def sum_shortest_piramid_path(piramid):
	result = [0]*len(piramid)
	piramid_len = len(piramid) - 1
	for i in range(len(piramid) - 1):
		current_row_addition = []
		for j in range(len(result)):
			result[j] += piramid[piramid_len - i][j]
		for j in range(len(piramid[piramid_len - i]) - 1):
			if(result[j] >= result[j + 1]):
				current_row_addition.append(result[j])
			else:
				current_row_addition.append(result[j + 1])
		result = current_row_addition
	return result[0] + piramid[0][0]
	
if __name__ == "__main__":
	main();