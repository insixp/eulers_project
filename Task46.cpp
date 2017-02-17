#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <math.h>
#include <primes.h>


int main(){
    
    int max_primes = 1000000;
    int curr_num = 1;
    int curr_prime_index;
    int curr_int;
    int total_sum;
    int num_of_primes;
    int *primes;
    
    num_of_primes = sieve_of_eratosthenes(1000000, &primes, NULL);
    
    while(true){
        curr_num            += 2;
        curr_prime_index    = 0;
        
        if(is_prime(curr_num))
            continue;
        
        printf("%d\n", curr_num);
        
        do{
            curr_int        = 1;
            curr_prime_index++;
            while(2 * (curr_int * curr_int) + primes[curr_prime_index] < curr_num)
                curr_int++;
            total_sum = 2 * (curr_int * curr_int) + primes[curr_prime_index];
        }while(total_sum != curr_num && curr_num > primes[curr_prime_index]);
        if(total_sum == curr_num)
            continue;
        
        printf("The answer is: %d\n", curr_num);
        return 0;
    }
	
	return 0;
}