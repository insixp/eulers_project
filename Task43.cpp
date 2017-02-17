#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <math.h>
#include <pandigital.h>

bool	is_substring_divisable(int *curr_num, int length);

int main(){
	
	int length;
	int *curr_num;
	int num_of_digits		= 10;
	double total_sum		= 0;
	int num_of_pandigitals  = fact(num_of_digits - 1) * (num_of_digits - 1);
	double *generated_pandigital_nums 	= (double*) malloc(num_of_pandigitals * sizeof(double));
	length								= generate_all_pandigital(generated_pandigital_nums);
	printf("The pandigital numbers that were printed were from:\n\n	%f - %f\n\n\nTake %d space\n", generated_pandigital_nums[0], generated_pandigital_nums[length - 1], length);
	for(int i = 0; i < length; i++){
		printf("%f\%\n", (double)(i*100)/length);
		curr_num = get_elementes(generated_pandigital_nums[i]);
		int curr_num_length		= 0;
		while(curr_num[curr_num_length] != -1){
			curr_num_length++;
		}
		if(is_substring_divisable(curr_num, curr_num_length)){
			total_sum		+= generated_pandigital_nums[i];
		}
	}
	printf("\n\n\n\n\n\n Answer: %f", total_sum);
	
	return 0;
}


bool is_substring_divisable(int *curr_num, int length){
	if(length < 10)
		return false;
	int divisable[7] = {2, 3, 5, 7, 11, 13, 17};
	int num_to_check;
	for(int i = 1;i < length - 2; i++){
		num_to_check = (int)(curr_num[i]*100 + curr_num[i+1] * 10 + curr_num[i+2]);
		if((double)num_to_check / divisable[i - 1] != num_to_check / divisable[i - 1])
			return false;
	}
	return true;
}

