#include <vector>
#include <iostream>
#include <math.h>
#include <assert.h>

#include <sys/time.h>
#include <ctime>

#define CATCH_CONFIG_RUNNER
#include "catch.hpp"

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

long compute_smpf_series(unsigned long n, unsigned int mod)
{
    std::vector<unsigned long> primes;
    primes.push_back(5);
    unsigned long prime_lim = sqrt(n);
    double sq;
    unsigned long number_of_twos, number_of_threes, sum_;

    number_of_twos = n / 2;
    number_of_threes = (n - number_of_twos - 1) / 3 + 1;
    sum_ = number_of_twos * 2 + number_of_threes * 3;

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

                sum_ += m;
                break;
            }
        }

    }

    return sum_;
}

std::vector<unsigned int> get_primes(unsigned int N)
{
    std::vector<unsigned int> primes;
    unsigned long sieve_size = (N - 1) / 2;
    std::vector<bool> sieve (sieve_size, false);
    double cross_limit = sqrt(N) / 2;

    // Note: We know that two is a prime
    //
    // cross out all odd composite numbers
    for (unsigned int i = 0; i < cross_limit; ++i) {
        if (not sieve[i]) {
            // p = 2i + 1 + 2!
            unsigned int smpf = 2 * i + 3;
            for (unsigned int j = i + smpf; j < sieve_size; j = j + smpf) {
                sieve[j] = true;
            }
        }
    }

    for (unsigned int i = 0; i < sieve_size; ++i) {
        if (not sieve[i]) {
            primes.push_back(2 * i + 3);
        }
    }

    return primes;
}

/*
long compute_smpf_sum_in_a_segment(unsigned long N, unsigned long offset, unsigend int mod)
{
    // Populate the index for crossing the next number now.
    std::vector<unsigned int> cross_next(primes.size(), 1);
    for (unsigned int i = 0; i < number_of_primes; ++i)
        cross_next[i] = (primes[i] - 1) / 2;

    for (unsigned int segment_id = 0; segment_id < number_of_segments;
            ++segment_id) {
        // std::cout << "Sieve size " << sieve_size << std::endl;
        // std::cout << "Number of segments " << number_of_segments << std::endl;
        int sieve_size = segment_size / 2;
        if (segment_id == number_of_segments - 1)
            sieve_size = N % segment_size / 2 + N % 2;
        std::vector<bool> sieve(sieve_size, false);

        // std::cout << "Sieve size " << sieve.size() << std::endl;

        unsigned long prime_limit = segment_size * sqrt(segment_id + 1);

        unsigned int smpf;
        for (unsigned int p = 0; p < number_of_primes; ++p) {
            smpf = primes[p];
            if (smpf > prime_limit or sieve_size == 0)
                break;

            int starting_index = cross_next[p] - segment_id * n / 2;

            // std::cout << std::endl << "Prime number, starting index: "
            //           << smpf << ", " << starting_index << std::endl;

            for (unsigned int j = starting_index; j < sieve_size; j += smpf) {
                if (not sieve[j]) {
                    sieve[j] = true;
                    sum += smpf;
                }
                cross_next[p] += smpf;
            }
        }

        // std::cout << "Segment number " << segment_id << std::endl;

        // Sum the leftover primes
        int offset = segment_id * segment_size;
        for (unsigned int i = 0; i < sieve_size; ++i) {
            if (not sieve[i]) {
                smpf = 2 * i + 1 + offset;
                // std::cout << smpf << " ";
                sum += smpf;
            }
        }

        if (mod != 1) {
            sum = sum % mod;
        }
    }
}
*/

long compute_smpf_series_quicker(unsigned long N, unsigned int mod)
{
    // prime list will not contain 2!
    std::vector<unsigned int> primes = get_primes(sqrt(N));
    unsigned int number_of_primes = primes.size();

    // initiate the sum and remove 1 from the next set of calculations, because
    // in the sieve we include 1 and it will appear as a prime.
    unsigned number_of_twos = N/2;
    unsigned number_of_threes = (N - N/2)/3 + 1;
    unsigned long sum = 2 * number_of_twos - 1;
    if (mod != 1) {
        sum = sum % mod;
    }

    // Populate the index for crossing the next number now.
    std::vector<unsigned int> cross_next(primes.size(), 1);

    unsigned long n = sqrt(N);
    // Note, that the segment size needs to be even for the algo to work
    // properly!
    const unsigned long segment_size = std::max((unsigned long)1000000, n) / 2 * 2;
    unsigned int number_of_segments = N / segment_size;
    // Add another segment if we do not divide the number cleanly
    number_of_segments += (N % segment_size) == 0 ? 0 : 1;

    std::cout << "Number of segments in the sieving: "
              << number_of_segments << std::endl;

    // std::cout << "List of odd primes: ";
#pragma omp parallel for reduction(+:sum)
    for (unsigned long sieved_through = 0; sieved_through <= N; sieved_through += segment_size)
    {
        unsigned long to_sieve_through = N - sieved_through;
        // std::cout << "Sieve size " << sieve_size << std::endl;
        // std::cout << "Number of segments " << number_of_segments << std::endl;
        int sieve_size = segment_size / 2;
        if (to_sieve_through < segment_size)
        {
            // std::cout << "Last sieve size is " << to_sieve_through << std::endl;
            sieve_size = (to_sieve_through + 1) / 2;
        }

        std::vector<bool> sieve(sieve_size, false);

        // std::cout << "Sieve size " << sieve.size() << std::endl;

        unsigned long prime_limit = sqrt(sieved_through + sieve_size * 2);
        // std::cout << "\nThe primes should be checked up to " << prime_limit << std::endl;

        for (unsigned int p = 0; p < number_of_primes; ++p)
        {
            unsigned int smpf = primes[p];
            if (smpf > prime_limit or sieve_size == 0)
            {
                // std::cout << "\nWill not sieve " << primes[p]
                //           << " because the limit is " << prime_limit << "\n";
                break;
            }
            int starting_index = (smpf - 1) / 2 + 
                sieved_through / 2 / smpf * smpf - sieved_through / 2;
            if (starting_index < 0)
                starting_index += smpf;

            // std::cout << std::endl << "Prime number, starting index: "
            //           << smpf << ", " << starting_index << std::endl;

            for (unsigned int j = starting_index; j < sieve_size; j += smpf)
            {
                if (not sieve[j])
                {
                    sieve[j] = true;
                    sum += smpf;
                    // std::cout << "\nCrossing out: " << 2 * j + 1 + sieved_through << " (" << primes[p] << ")\n";
                }
            }
        }

        // std::cout << "Segment number " << segment_id << std::endl;

        // Sum the leftover primes
        for (unsigned int i = 0; i < sieve_size; ++i) {
            if (not sieve[i]) {
                sum += 2 * i + 1 + sieved_through;
            }
        }

        if (mod != 1) {
            sum = sum % mod;
        }
    }
    // std::cout << std::endl;

    if (mod != 1) {
        sum = sum % mod;
    }

    std::cout << "The sum: " << sum << std::endl;

    return sum;
}

long compute_smpf_series_quickest(unsigned long N, unsigned int mod)
{
    // prime list will not contain 2!
    std::vector<unsigned int> primes = get_primes(sqrt(N));
    unsigned int number_of_primes = primes.size();

    unsigned int number_of_twos = N / 2;
    unsigned int number_of_odds = N - number_of_twos - 1;
    unsigned long sum = number_of_twos * 2;
    unsigned long highest_odd_number = (N + 1) / 2 * 2 - 1;

    unsigned long all_sum = sum + number_of_odds * (highest_odd_number + 3);

    // generate all factors of prime numbers and then subtract the difference
    // between the smpf and the number.
    //
    // if n = k * smpf, smpf = n - (k - 1) * smpf;
    //
    // First subtract all 3s, then 5s, then 7s, then ...
    /*
     *  subtract threes:
     *
     *
     *  // subtract the rest by using recursive generators.
     *  for p in primes > 3:
     *      all_sum -=
     */
    

    // initiate the sum and remove 1 from the next set of calculations, because
    // in the sieve we include 1 and it will appear as a prime.
    if (mod != 1) {
        sum = sum % mod;
    }

    std::cout << "The sum: " << sum << std::endl;

    return sum;
}

TEST_CASE( "Smallest prime factor sums are computed", "[Sum]" ) {
    REQUIRE(compute_smpf_series_quicker(100, 1) == 1257);
    REQUIRE(compute_smpf_series_quicker(101, 1) == 1358);
    REQUIRE(compute_smpf_series_quicker(pow(10, 8), 1) == 279218813374515);
    REQUIRE(compute_smpf_series_quicker(pow(10, 8), pow(10, 5)) == 74515);
}

TEST_CASE( "Checking the computational time", "[Time]" ) {
    unsigned long sum;
    long start, end;

    start = getTimeMiliseconds();
    sum = compute_smpf_series_quicker(pow(10, 9), 1);
    end = getTimeMiliseconds();
    REQUIRE((end - start) * 0.001 < 0.1);
}

int main(int argc, char* const argv[])
{
    // Run tests
    Catch::Session session; // There must be exactly once instance
    if (session.run(argc, argv))
    {
        // do_sieving_and_print(pow(10,3));
        unsigned long sum;
        long start, end;

        start = getTimeMiliseconds();
        sum = compute_smpf_series_quicker(pow(10, 12), pow(10, 9));
        // sum = compute_smpf_series_quicker(pow(10, 9), pow(10, 5));
        end = getTimeMiliseconds();
        std::cout << "Answer is: " << sum << std::endl
                  << "Took " << (end - start) * 0.001 << "s" << std::endl;
    }

    return 0;
}
