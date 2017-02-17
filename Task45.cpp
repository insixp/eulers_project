#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <math.h>
#include <nodes.h>

double triangular(int index);
double pentagonal(int index);
double hexagonal(int index);

int main(){
    
    double  bigger_than             = 40755;
    double  curr_triangular_num     = 0;
    double  curr_pentagonal_num     = 0;
    double  curr_hexagonal_num      = 0;
    
    
    
    double  curr_triangular_delta   = 1;
    double  curr_pentagonal_delta   = 1;
    double  curr_hexagonal_delta    = 1;
    
    while(true){
        //  Set the Triangular number
        curr_triangular_num     += curr_triangular_delta;
        curr_triangular_delta   += 1;
        
        while(curr_pentagonal_num < curr_triangular_num){
            //  Set the Pentagonal number
            curr_pentagonal_num     += curr_pentagonal_delta;
            curr_pentagonal_delta   += 3;
        }
        
        
        if(curr_triangular_num != curr_pentagonal_num)
            continue;
        
        
        while(curr_hexagonal_num < curr_triangular_num){
            //  Set the Hexagonal number
            curr_hexagonal_num      += curr_hexagonal_delta;
            curr_hexagonal_delta    += 4;
        }
        
        if(curr_triangular_num != curr_hexagonal_num)
            continue;
        
        if(curr_triangular_num <= bigger_than)
            continue;
        
        
        printf("The answer is:%f\n", curr_triangular_num);
        return 0;
    }
	
	return 0;
}