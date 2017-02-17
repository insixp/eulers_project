#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <math.h>
#include <pentagonal.h>
#include <nodes.h>

int main(){
	
	element 	*last_item;
	element 	*curr_item;
	int                 pentagonal_sum;
	int                 pentagonal_diff;
    int                 curr_index;
	
	
	
	last_item 		= head_element(1);
	pentagonal_sum  = 2;
    pentagonal_diff = 2;
	while(true){
        curr_index = 1;
        curr_item   = get_element(curr_index, last_item);
        while(curr_item != NULL){
            if(is_pentagonal(last_item->value - curr_item->value) && is_pentagonal(last_item->value + curr_item->value)){
                printf("The Answer is: %f\n", last_item->value - curr_item->value);
                return 0;
            }
            curr_index++;
            curr_item   = get_element(curr_index, last_item);
        }
        curr_index  = pentagonal_index(last_item->value);       
        last_item   = add_element(pentagonal_num(curr_index + 1), last_item);
        printf("Recently added: %d\n", (int)last_item->value);
    }
	
	return 0;
}

