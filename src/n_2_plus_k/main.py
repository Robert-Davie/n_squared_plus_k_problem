"""for values of k in range START (inclusive) to STOP (exclusive) find possible value of p1 and p2 up to SEARCH"""
import sympy
import csv
from time import time
from typing import Optional


START = -822
STOP = -100
SEARCH = 100_000



def get_largest_prime_factor(n: int) -> Optional[int]:
    s = sympy.primefactors(n)
    if s == []:
        return None
    return max(s)


def check_p1(k: int, iteration: int) -> tuple[bool, Optional[int]]:
    """check if p1 is part of a valid pair, and if so return p2"""
    if not sympy.isprime(iteration):
        return False, None
    p2_candidate = get_largest_prime_factor(iteration ** 2 + k)
    if p2_candidate is None or p2_candidate <= iteration:
        return False, None
    t = get_largest_prime_factor(p2_candidate ** 2 + k)
    if t == iteration:
        return True, p2_candidate
    else:
        return False, None


def check_k(k: int, iterations: int):
    results = []
    for iteration in range(iterations):
        if iteration % 10_000 == 0:
            print(iteration)
        result = check_p1(k, iteration)
        if result[0]:
            p2 = result[1]
            results.append((k, iteration, p2))
            print(f"found solution {iteration}, {p2}")
    
    # write results to results.csv
    with open("results.csv", "a") as f:
        if len(results) > 10:
            # if many results for a given k only write first 10
            results = results[:10]
        writer = csv.writer(f)
        writer.writerows(results)


def main():
    for k in range(START, STOP):
        print(f"addition = {k}")
        check_k(k, SEARCH)
            

if __name__ == "__main__":
    # execute main and print time taken
    start = time()
    main()
    end = time()
    print(f"time taken = {end-start}")
