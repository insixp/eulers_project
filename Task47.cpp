#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <math.h>
#include <primes.h>
#include <general.h>

bool is_distinct(int *list_a, int size_a, int *list_b, int size_b, int *list_c, int size_c, int *list_d, int size_d);
int max_num(int a, int b, int c, int d);

int main(){
    
    int *primes;
    int num_of_primes         = sieve_of_eratosthenes(2000000, &primes, NULL);
    
    
    int size_a, size_b, size_c, size_d;
    int *divisors_a;
    int *divisors_b;
    int *divisors_c;
    int *divisors_d;
    int index = 1;
    
    size_a      = primes_factorization(++index, primes, num_of_primes, &divisors_a);
    size_a      = list_unify(divisors_a, size_a, &divisors_a);
    size_b      = primes_factorization(++index, primes, num_of_primes, &divisors_b);
    size_b      = list_unify(divisors_b, size_b, &divisors_b);
    size_c      = primes_factorization(++index, primes, num_of_primes, &divisors_c);
    size_c      = list_unify(divisors_c, size_c, &divisors_c);
    size_d      = primes_factorization(++index, primes, num_of_primes, &divisors_d);
    size_d      = list_unify(divisors_d, size_d, &divisors_d);
    
    
    while(!is_distinct(divisors_a, size_a, divisors_b, size_b, divisors_c, size_c, divisors_d, size_d) || size_a != 4 || size_b != 4 || size_c != 4 || size_d != 4){
        free(divisors_a);
        divisors_a  = divisors_b;
        size_a      = size_b;
        divisors_b  = divisors_c;
        size_b      = size_c;
        divisors_c  = divisors_d;
        size_c      = size_d;
        size_d      = primes_factorization(++index, primes, num_of_primes, &divisors_d);
        size_d      = list_unify(divisors_d, size_d, &divisors_d);
        printf("%d\n", index);
    }
    printf("%d\n", index - 3);
    
    for(int i = 0; i < max_num(size_a, size_b, size_c, size_d); i++){
        printf("a=%d, b=%d, c=%d, d=%d\n", divisors_a[i], divisors_b[i], divisors_c[i], divisors_d[i]);
    }
}


bool is_distinct(int *list_a, int size_a, int *list_b, int size_b, int *list_c, int size_c, int *list_d, int size_d){
    for(int a = 0; a < size_a; a++){
        for(int b = 0; b < size_b; b++){
            for(int c = 0; c < size_c; c++){
                for(int d = 0; d < size_d; d++){
                    if(list_d[d] == list_a[a])
                        return false;
                    if(list_d[d] == list_b[b])
                        return false;
                    if(list_d[d] == list_c[c])
                        return false;
                }
                if(list_c[c] == list_b[b])
                    return false;
                if(list_c[c] == list_a[a])
                    return false;
            }
            if(list_b[b] == list_a[a])
                return false;
        }
    }
    return true;
}

int max_num(int a, int b, int c, int d){
    int tmp = a;
    if(tmp < b)
        tmp = b;
    if(tmp < c)
        tmp = c;
    if(tmp < d)
        tmp = d;
    return tmp;
}
