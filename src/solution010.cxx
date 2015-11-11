#include <vector>
#include <iostream>
#include <math.h>
#include <assert.h>

#include <sys/time.h>
#include <ctime>

/*
 
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

long sum_primes(unsigned long n)
{
    std::vector<unsigned long> primes;
    primes.push_back(2);
    primes.push_back(3);
    double sq;
    unsigned long sum;

    bool is_prime = true;
    PossiblePrimeGenerator gen(3);
    for (unsigned long m = gen.next(); n >= m; m = gen.next())
    {
        sq = sqrt(m);
        is_prime = true;
        for (std::vector<unsigned long>::iterator it = primes.begin();
                it != primes.end(); ++it)
        {
            if (*it > sq) {
                break;
            } else if (m % *it == 0) {
                is_prime = false;
                break;
            }
        }

        if (is_prime) {
            primes.push_back(m);
            sum += m;
        }
    }
    
    return sum + 2 + 3;
}

long sum_primes_sieve(unsigned long n)
{
    unsigned long sieve_size = (n - 1) / 2;
    std::vector<bool> sieve (sieve_size, false);
    double cross_limit = sqrt(n) / 2;
    // We know that two is a prime
    long sum = 2;

    // cross out all odd composite numbers
    for (unsigned int i = 0; i < cross_limit; ++i) {
        if (not sieve[i]) {
            /*
             * we now that the number is p = 2 i + 3 (where i starts at 0)
             *
             * i 0 1 2 3  4  5  6  7  8  9 10 11
             * p 3 5 7 9 11 13 15 17 19 21 23 25
             *
             * 2i + 3 = p
             *
             * 3 - > 9 = 3
             * 5 - > 15 -> 25 = 1 6 11
             *
             * j = p * k = (2i + 3)* k
             *
             */
            for (unsigned int j = 3*(i + 1); j < sieve_size; j = j + 2 * i + 3) {
                sieve[j] = true;
            }
        }
    }

    // sum everything:
    for (unsigned int i = 0; i < sieve_size; ++i) {
        if (not sieve[i]) {
            // std::cout << 2 * i + 3 << " ";
            sum += 2 * i + 3;
        }
    }
    // std::cout << std::endl;

    return sum;
}

bool test_solutions() {
    std::cout << sum_primes_sieve(10) << std::endl;
    assert(sum_primes_sieve(10) == 17);

    return true;
}

int main()
{
    if (test_solutions()) {
        unsigned long sum;
        long start, end;

        /*
        start = getTimeMiliseconds();
        sum = sum_primes(2 * pow(10, 6));
        end = getTimeMiliseconds();
        std::cout << "Answer is: " << sum << std::endl
                  << "Took " << (end - start) * 0.001 << "s" << std::endl;
        */

        start = getTimeMiliseconds();
        sum = sum_primes_sieve(2 * pow(10, 6));
        end = getTimeMiliseconds();
        std::cout << "Answer is: " << sum << std::endl
                  << "Took " << (end - start) * 0.001 << "s" << std::endl;
    }

    return 0;
}
