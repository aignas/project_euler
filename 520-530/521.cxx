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

// forward declaration
class PrimeIterator;

class PrimeFactorIterator;

class PrimeIterator
{
public:
    PrimeIterator() {
        mMin = 5;
        mSkip = false;

        value = mMin;
        index = 0;
    }

    PrimeIterator(const unsigned int min) {
        mMin = min;
        mSkip = false;

        // Check that the lower bound is higher or equal than 5
        if (min > 5) {

            // Find the closest odd number which is higher than min
            mMin = (mMin % 2 == 0 ? mMin + 1 : mMin);

            // Find the closest odd number which is higher than min and not a
            // multiple of 3
            if (mMin % 3 == 0) {
                // The number should be skipped,
                // the mMin value should be e.g. 11
                mMin += 2;
            } else if ((mMin + 2) % 3 == 0) {
                // The next number should be skipped
                mSkip = true;
            }

        } else {
            mMin = 5;
        }

        value = mMin;
        index = 0;
    }

    unsigned long next(void) {
        value += (mSkip ? 4: 2);
        mSkip = not mSkip;
        ++index;
        
        return value;
    }

private:
    const unsigned int mMin;
    bool mSkip;

public:
    unsigned long value;
    unsigned int index;
};

// FIME: implement the start of the iteration.
class PrimeFactorIndexIterator
{
public:
    PrimeFactorIndexIterator(const unsigned int min,
                             const unsigned int prime) {
        mMin = prime;
        mPrime = prime;
        mSkip = false;
        // FIXME: calculate the offset below
        index_offset = 0;

        // Check that the lower bound is higher or equal than 5
        if (min > prime) {
            // Find the closest prime number multiple which is higher
            // than the prime itself;
            mMin = (min / prime + 1) * prime;

            // Find the closest odd number which is higher than min and not a
            // multiple of 3
            if (mMin % 3 == 0) {
                // The number should be skipped,
                // the mMin value should be e.g. 11
                mMin += 2 * prime;
            } else if ((mMin + 2 * prime) % 3 == 0) {
                // The next number should be skipped
                mSkip = true;
            }

            index_offset
        }

        value = mMin;
        // Calculate the first index which is equal to
        // number of odds - number of odd factors of three
        // where odd factors of three = factors of three - even factors
        //  of three
        index = mMin / 2 - mMin / 3 + mMin / 6;

        // remove the offset, were we need to find the first 
        // FIXME: implement
    }

    unsigned long next(void) {
        // Add the value
        // value += (mSkip ? 4 : 2 ) * mPrime;

        // Add the index.
        index += mPrime + (mSkip ? 2 : -2);
        mSkip = not mSkip;
        
        return index;
    }

private:
    const unsigned int mMin;
    const unsigned int mPrime;
    bool mSkip;

public:
    unsigned long value;
    unsigned int index;
};

typedef std::vector<unsigned int> PrimeList;
typedef std::vector<bool> Sieve;

Primes get_primes(unsigned int N)
{
    Primes primes;
    primes.push_back(2);
    primes.push_back(3);

    unsigned long sieve_size = (N - 1) / 2 - 1;
    Sieve sieve (sieve_size, false);
    double cross_limit = sqrt(N) / 2;

    // Note: We know that two is a prime
    //
    // cross out all odd composite numbers
    bool skip = false;
    for (PrimeIterator it(); it.value =< cross_limit; it.next()) {
        if (not sieve[i]) {
            // We are using the slightly more complex formula:
            //  p = 6k +/- 1
            //
            // Hence, then smpf is equal
            //  smpf = 5 + 3 * i +/- 1
            bool skip_ = false;
            for (PrimeFactorIterator pfit();
                    pfit.index < sieve_size; 
                    pfit.next())
            {
                sieve[j] = true;
            }
        }
    }

    for (PrimeIterator it(); it.index =< sieve_size; it.next()) {
    {
        if (not sieve[it.index]) {
            primes.push_back(it.value);
        }
    }

    return primes;
}

long compute_smpf_series(unsigned long N, unsigned int mod)
{
    // Get the primes we need to sieve everything
    Primes primes = get_primes(sqrt(N));
    // Remove 2 and 3 from the prime list
    primes.erase(primes.begin(), primes.begin() + 1);

    if (N == 100) {
        for (unsigned i = 0; i < primes.size(); ++i)
        {
            std::cout << primes[i] << " ";
        }
        std::cout << std::endl;
    }

    // initiate the sum and remove 1 from the next set of calculations, because
    // in the sieve we include 1 and it will appear as a prime.
    unsigned number_of_twos = N/2;
    unsigned number_of_threes = (N - N/2)/3 + 1;
    unsigned long sum = 2 * number_of_twos - 1 + number_of_threes * 3;
    if (mod != 1) {
        sum = sum % mod;
    }

    // Setup some sieving stuff
    std::vector<unsigned int> sieve_indices(primes.size(), 1);
    std::vector<bool> skip(primes.size(), true);
    unsigned int number_of_primes = primes.size();

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

    int sign = -1;
    for (unsigned int i = 0; i < primes.size(); ++i, sign = -sign)
    {
        sieve_indices[i] = (primes[i] - sign) / 6 - 1;
    }

    std::cout << "List of odd primes: ";
#pragma omp parallel for reduction(+:sum)
    for (unsigned long sieved_through = 0; sieved_through <= N; sieved_through += segment_size)
    {
        unsigned long to_sieve_through = N - sieved_through;
        // std::cout << "Sieve size " << sieve_size << std::endl;
        // std::cout << "Number of segments " << number_of_segments << std::endl;
        unsigned int sieve_size = segment_size / 3;
        unsigned long prime_limit = sqrt(sieved_through + segment_size);
        if (to_sieve_through < segment_size)
        {
            // std::cout << "Last sieve size is " << to_sieve_through << std::endl;
            sieve_size = (to_sieve_through + 2) / 3;
            prime_limit = sqrt(N);
        }

        std::vector<bool> sieve(sieve_size, false);

        // std::cout << "Sieve size " << sieve.size() << std::endl;
        // std::cout << "\nThe primes should be checked up to " << prime_limit << std::endl;
        unsigned int sieved_through_by_two = sieved_through / 2;

        for (unsigned int p = 1; p < number_of_primes; ++p)
        {
            unsigned int smpf = primes[p];
            if (smpf > prime_limit or sieve_size == 0)
            {
                // std::cout << "\nWill not sieve " << primes[p]
                //           << " because the limit is " << prime_limit << "\n";
                break;
            }

            // std::cout << std::endl << "Prime number, starting index: "
            //           << smpf << ", " << starting_index << std::endl;

            // FIXME: indexing in this loop is wrong!!!
            for (; sieve_indices[p] < sieve_size;
                    sieve_indices[p] += smpf * (skip[p] ? 2 : 1),
                    skip[p] = not skip[p])
            {
                if (not sieve[sieve_indices[p]])
                {
                    sieve[sieve_indices[p]] = true;
                    sum += smpf;
                    // std::cout << "\nCrossing out: " << 2 * j + 1 + sieved_through << " (" << primes[p] << ")\n";
                }
            }
        }

        unsigned int offset_by_three = (sieved_through + 1)/ 6;
        unsigned long offset = offset_by_six * 6 + 1;
        bool skip_ = (sieved_through + 1) % 6 == 0;

        if (mod != 1) {
            offset %= mod;
            sum %= mod;
        }

        // std::cout << "Segment number " << segment_id << std::endl;

        // Sum the leftover primes
        for (unsigned int i = 0, smpf = offset; 
                i < sieve_size;
                ++i, smpf += 2 * (skip_ ? 2 : 1), skip_ = not skip_)
        {
            if (not sieve[i]) {
                sum += smpf;
                std::cout << " " << smpf;
            }
        }

        if (mod != 1) {
            sum %= mod;
        }
    }
    std::cout << std::endl;

    if (mod != 1) {
        sum %= mod;
    }

    std::cout << "The sum: " << sum << std::endl;

    return sum;
}

unsigned long factor_sum_diff(
        std::vector<unsigned int>& primes,
        std::vector<unsigned int>::iterator primes_begin,
        unsigned long factor, const unsigned long max)
{
    unsigned long result, sum = 0;

    if (factor > max) {
        return sum;
    }

    for (std::vector<unsigned int>::iterator p = primes_begin;
            p != primes.end(); ++p)
    {
        result = factor * *p;

        if (result <= max) {
            std::cout << " " << result << "(" << result - *primes_begin << ")";
            sum += result - *primes_begin;
        } else {
            break;
        }

    }

    for (std::vector<unsigned int>::iterator p = primes_begin;
            p != primes.end(); ++p)
    {
        result = factor_sum_diff(
            primes, p, *p * factor, max);

        if (result == 0)
            break;
        else
            sum += result;
    }

    return sum;
}

long compute_smpf_series_quickest(unsigned long N, unsigned int mod)
{
    // prime list will not contain 2!
    std::vector<unsigned int> primes = get_primes(sqrt(N));
    unsigned int number_of_primes = primes.size();

    unsigned int number_of_twos = N / 2;
    unsigned int number_of_odds = N - number_of_twos - 1;
    unsigned long highest_odd_number = (N + 1) / 2 * 2 - 1;

    unsigned long sum = number_of_twos * 2 + number_of_odds * (highest_odd_number + 3) / 2;

    // generate all factors of prime numbers and then subtract the difference
    // between the smpf and the number.
    //
    // if n = k * smpf, smpf = n - (k - 1) * smpf;
    //
    // First subtract all 3s, then 5s, then 7s, then ...
    /*
     */
    for (std::vector<unsigned int>::iterator p = primes.begin();
            p != primes.end(); ++p)
    {
        if (*p > sqrt(N))
            break;

        std::cout << *p;
        sum -= factor_sum_diff(primes, p, *p, N);
        std::cout << std::endl;
    }
    

    // initiate the sum and remove 1 from the next set of calculations, because
    // in the sieve we include 1 and it will appear as a prime.
    if (mod != 1) {
        sum = sum % mod;
    }

    std::cout << "The sum: " << sum << std::endl;

    return sum;
}

TEST_CASE( "Smallest prime factor sums are computed", "[Sum]" ) {
    // REQUIRE(compute_smpf_series_quickest(100, 1) == 1257);

    REQUIRE(compute_smpf_series_quicker(100, 1) == 1257);
    // REQUIRE(compute_smpf_series_quicker(101, 1) == 1358);
    // REQUIRE(compute_smpf_series_quicker(pow(10, 8), 1) == 279218813374515);
    // REQUIRE(compute_smpf_series_quicker(pow(10, 8), pow(10, 5)) == 74515);
}

TEST_CASE( "Checking the computational time", "[Time]" ) {
    long start = getTimeMiliseconds();
    // compute_smpf_series_quicker(pow(10, 9), 1);
    long end = getTimeMiliseconds();

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
        // sum = compute_smpf_series_quicker(pow(10, 12), pow(10, 9));
        // compute_smpf_series_quickest(100, 1);
        // sum = compute_smpf_series_quicker(pow(10, 9), pow(10, 5));
        end = getTimeMiliseconds();
        std::cout << "Answer is: " << sum << std::endl
                  << "Took " << (end - start) * 0.001 << "s" << std::endl;
    }

    return 0;
}
