#include <vector>
#include <iostream>
#include <math.h>
#include <assert.h>

#include <sys/time.h>
#include <ctime>

/* Some analysis of the problem:
 *
When we subtract all factors of 2 and 3, then we are left with factors of higher primes.

5, 7, 11, 13, 17, 19, 23,
5 * 5, 29, 31,
5 * 7, 37, 41, 43, 47,
7*7, 53,
5* 11, 59, 

number_of_primes(below N) = alpha
number_of_primes(below sqrt(N)) = beta

number of factors of 5 is:
5, 5 * primes', 5 * 5 * primes, 5 * 7 * primes, 5, * 11 * primes, 5 * 13 * primes,
, ..., 5 * 5 * 5 * primes, ... until product < n

formula: 5 + 5 * number_of_primes + 5 * C(number_of_primes, 1) * number_of_primes +  5 * C(number_of_primes, 2) * number_of_primes

2      3      5      7     11     13     17     19     23     29 
31     37     41     43     47     53     59     61     67     71 
73     79     83     89     97    101    103    107    109    113 
 */


long getTimeMiliseconds()
{
    /* Linux */
    struct timeval tv;

    gettimeofday(&tv, NULL);

    long ret = tv.tv_usec;
    /* Convert from micro seconds (10^-6) to milliseconds (10^-3) */
    ret /= 1000;

    /* Adds the seconds (10^0) after converting them to milliseconds (10^-3) */
    ret += (tv.tv_sec * 1000);

    return ret;
}

class PossiblePrimeGenerator {
private:
    char i;
    unsigned long k;
    unsigned long m;
public:
    PossiblePrimeGenerator() {
        i = 1;
        k = 0;
        m = 1;
    };
    PossiblePrimeGenerator(int start) {
        i = 1;
        k = 0;
        m = start;
    };
    unsigned long next() {
        if (m == 1 || m == 2) {
            ++m;
        } else {
            i = -i;
            if (i == -1)
                ++k;

            m = 6 * k + i;
        }
        return m;
    }
};

long compute_smpf_series(unsigned long n, int mod)
{
    std::vector<unsigned long> primes;
    primes.push_back(5);
    unsigned long prime_lim = sqrt(n);
    double sq;
    unsigned long number_of_twos, number_of_threes, sum_;

    number_of_twos = n / 2;
    number_of_threes = (n - number_of_twos - 1) / 3 + 1;
    sum_ = number_of_twos * 2 + number_of_threes * 3;

    if (mod != -1) {
        sum_ = sum_ % mod;
    }

    PossiblePrimeGenerator gen(3);
    for (unsigned long m = gen.next(); m <= n; m = gen.next())
    {
        sq = sqrt(m);
        for (std::vector<unsigned long>::iterator it = primes.begin();
                it != primes.end(); ++it)
        {
            if (m % *it == 0)
            {
                sum_ += *it;
                break;
            }

            if (*it > sq) {
                if (m < prime_lim)
                    primes.push_back(m);
                if (mod != -1 && m > mod)
                    sum_ += m % mod;
                else
                    sum_ += m;
                break;
            }
        }

        if (mod != -1 && sum_ > mod) {
            sum_ = sum_ % mod;
        }
    }

    return sum_;
}

long compute_smpf_series_quicker(unsigned long n, int mod)
{
    std::vector<unsigned long> primes;
    primes.push_back(3);
    primes.push_back(3);
    unsigned long prime_lim = sqrt(n);
    double sq;

    PossiblePrimeGenerator gen(3);
    for (unsigned long m = gen.next(); m <= prime_lim; m = gen.next())
    {
        sq = sqrt(m);
        for (std::vector<unsigned long>::iterator it = primes.begin();
                it != primes.end(); ++it)
        {
            if (m % *it == 0)
                break;

            if (*it > sq) {
                primes.push_back(m);
                break;
            }
        }
    }


    unsigned long number_of_twos, number_of_threes, number_of_primes, sum_;

    number_of_primes = primes.size();
    number_of_twos = n / 2;
    number_of_threes = (n - number_of_twos - 1) / 3 + 1;
    sum_ = number_of_twos * 2 + number_of_threes * 3;

    if (mod != -1) {
        sum_ = sum_ % mod;
    }

    return sum_;
}

void count_all(unsigned long n){
    PossiblePrimeGenerator gen(3);
    for (unsigned long m = gen.next(); m <= n; m = gen.next())
    {
    }
}


bool test_solutions() {
    // assert(compute_smpf_series(100, -1) == 1257);
    // assert(compute_smpf_series(101, -1) == 1358);

    return true;
}

int main()
{
    if (test_solutions()) {
        unsigned long sum_;
        long start, end;

        start = getTimeMiliseconds();
        // sum_ = compute_smpf_series(pow(10, 12), pow(10, 9));
        count_all(pow(10, 10));
        sum_ = 0;
        end = getTimeMiliseconds();
        std::cout << "Answer is: " << sum_ << std::endl
                  << "Took " << (end - start) * 0.001 << "s" << std::endl;
    }

    return 0;
}
