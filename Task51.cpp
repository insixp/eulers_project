#include <iostream>
#include <stdint.h>
#include <sstream>
#include "miller_rabin.cpp"
#include <string>
#include <time.h>

using namespace std;


//  Parameters
char    MAX_N       = '9';

//  Functions
string      ui64os(uint64_t in);
uint64_t    stoui64(istringstream in);
int         get_primes_num(string n, uint16_t k);
void        print_all_primes(string n, uint16_t k);
int      check_n_rec(string n, int num_of_primes, uint16_t k);

int main()
{
    int         num_of_primes   = 8;
    uint16_t    k               = 4;

    uint64_t    curr_int;
    int         result_n    = -1;
    string      curr_n      = "100100";

    while(result_n == -1){
        result_n    = check_n_rec(curr_n, num_of_primes, k);
        //cout << result_n << endl;
        curr_int    = stoui64(static_cast<istringstream>(curr_n));
        curr_int++;
        cout << curr_int << endl;
        curr_n      = ui64os(curr_int);
    }
}

int      check_n_rec(string n, int num_of_primes, uint16_t k){
    int res;
    string tmp_n;
    for(int loc = 0; loc < n.length(); loc++){
        tmp_n       = n;
        if(tmp_n[loc]  != '*'){
            tmp_n[loc]  = '*';
            res = check_n_rec(tmp_n, num_of_primes, k);
            if(res != -1)
                return res;
        } else {
            //  Check if num of primes
            cout << get_primes_num(tmp_n, k) << endl;
            if(get_primes_num(tmp_n, k) == num_of_primes){
                print_all_primes(tmp_n, k);
                return 0;
            }
        }
    }
    return -1;
}

int     get_primes_num(string n, uint16_t k){
    int num_of_primes   = 0;
    string tmp_n;
    uint64_t tmp_int;

    for(char i = '0'; i <= MAX_N; i++){
        tmp_n   = n;
        for(int loc = 0; loc < n.length(); loc++){
            if(tmp_n[loc] == '*')
                tmp_n[loc]  = i;
        }
        tmp_int = stoui64(static_cast<istringstream>(tmp_n));
        if(isPrime(tmp_int, k)){
            num_of_primes++;
        }
    }
    return num_of_primes;
}


uint64_t stoui64(istringstream in){
    uint64_t        res;
    if(!(in >> res))
        cout    << "Error: failed to convert string to int" << endl;
    return res;
}

string ui64os(uint64_t in){
    string res;
    ostringstream   o;
    o << in;
    res = o.str();
    return res;
}

void print_all_primes(string n, uint16_t k){
    string tmp_n;
    uint64_t tmp_int;

    for(char i = '0'; i <= MAX_N; i++){
        tmp_n   = n;
        for(int loc = 0; loc < n.length(); loc++){
            if(tmp_n[loc] == '*')
                tmp_n[loc]  = i;
        }
        tmp_int = stoui64(static_cast<istringstream>(tmp_n));
        if(isPrime(tmp_int, k)){
            cout << tmp_int << endl;
        }
    }
}