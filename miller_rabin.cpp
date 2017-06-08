#include <tuple>
#include <stdint.h>
#include <time.h>
#include <unistd.h>

using namespace std;

tuple<uint64_t, uint16_t> get_factors(uint64_t n, uint16_t depth);
uint64_t    power_me(uint64_t x, uint64_t y, uint64_t p);
bool        miller_test(uint64_t n, uint64_t d);

bool isPrime(uint64_t n, uint8_t k){

    tuple<uint64_t, uint16_t>   factors;

    //  Initiate rand
    srand(time(NULL));

    //  Handle base cases for n < 3
    if(n < 3){
        if(n != 1)
            return true;
        else
            return false;
    }    

    // Handle even cases
    if(n % 2 == 0)
        return false;

    //  Get factors
    factors = get_factors(n - 1, 0);

    for(uint8_t i = 0; i < get<1>(factors); i++){
        if(!miller_test(n, get<0>(factors)))
            return false;
    }
    return true;
}

tuple<uint64_t, uint16_t> get_factors(uint64_t n, uint16_t depth){
    if(n % 2 == 0)
        return get_factors(n/2, depth + 1);
    else
        return make_tuple(n, depth);
}

uint64_t    power_me(uint64_t x, uint64_t y, uint64_t p){
    uint64_t        res = 1;

    x = x % p;
    while(y > 0){
        if(y & 1)
            res = (res*x) % p;
        y   >>= 1;
        x   = (x*x) % p;
    }
    return res;
}

bool miller_test(uint64_t n, uint64_t d){

    uint64_t    max_a   = n - 4;
    uint8_t     min_a   = 2;

    uint64_t    a = min_a + rand() % max_a;
    uint64_t    x = power_me(a, d, n);

    if(x == 1 || x == n - 1)
        return true;
    while (d < n - 1){
        x   = (x*x) % n;
        d   *= 2;
        if(x == 1)
            return false;
        if(x == n - 1)
            return true;
    }
    return false;

}