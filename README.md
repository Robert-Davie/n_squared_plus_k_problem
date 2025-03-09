# n_squared_plus_k_problem

find a pair of prime numbers p1 and p2 such that p1 != p2, and p2 is the greatest prime factor of (p1 ^ 2) + k and p1 is the greatest prime factor of (p2 ^ 2) + k.

results_sorted.csv contains pairs of p1 and p2 for different values of k

important observation is when k is a negative even square number, there are many solutions: k = -4 contains all twin primes aside from 3 & 5. In general for k = -m^2 p1 and p2 = pairs of primes m apart.

all pairs where p1 is up to 100,000 have been found for k between -1000 and 1000, listed in results_sorted.csv
all pairs where p1 is up to 1,000,000 have been found for k between -100 and 100, listed in results_sorted.csv
all pairs where p1 is up to 100,000,000 have been found for k = 1 and k = 6, listed in results_sorted.csv