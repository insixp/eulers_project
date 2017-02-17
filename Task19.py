def main():
	starting_year = 1901
	ending_year = 2001
	num_of_days = (ending_year - starting_year) * 365
	current_day_of_week = 2
	current_day = 0
	current_month = 1
	num_of_sundays = 0
	current_year = starting_year
	while(current_year < ending_year):
		if(current_day_of_week == 7):
			current_day_of_week = 0
		if(current_month in [4, 6, 9, 11] and current_day == 30):
			current_day = 0
			current_month += 1
		if(current_month in [2]):
			if(((current_year % 4 == 0) or (current_year % 100 == 0 and current_year % 400 == 0)) and current_day == 29):
				current_day = 0
				current_month += 1
			if(not ((current_year % 4 == 0) or ( current_year % 100 == 0 and current_year % 400 == 0)) and current_day == 28):
				current_day = 0
				current_month += 1
		if(current_month in [1, 3, 5, 7, 8, 10] and current_day == 31):
			current_day = 0
			current_month += 1
		if(current_month in [12] and current_day == 31):
			current_day = 0
			current_month = 1
			current_year += 1
		if(current_day==0 and current_day_of_week==0):
			num_of_sundays += 1
		current_day += 1
		current_day_of_week += 1
	print num_of_sundays
	
		
	
if __name__ == "__main__":
	main();