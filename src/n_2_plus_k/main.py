"""for values of k in range START (inclusive) to STOP (exclusive) find possible value of p1 and p2 up to SEARCH"""
import sympy
import csv
import time
import datetime
import os
from multiprocessing import Pool
from dataclasses import dataclass
import cProfile


@dataclass
class Settings:
    start_k: int
    stop_k: int
    search_start: int
    search_stop: int
    processes: int
    print_mode: bool


def get_largest_prime_factor(n: int) -> int | None:
    s = sympy.primefactors(n)
    if s == []:
        return None
    return max(s)


def has_prime_factor_greater_than(n: int, p1_candidate: int) -> bool:
    factors = sorted(sympy.factorint(n).keys())
    for factor in factors:
        if factor > p1_candidate and sympy.isprime(factor):
            return True
    return False


def check_p1(k: int, p1_candidate: int) -> tuple[bool, int | None]:
    """check if p1 is part of a valid pair, and if so return p2"""
    if not sympy.isprime(p1_candidate):
        return False, None
    p2_candidate = get_largest_prime_factor(p1_candidate ** 2 + k)
    if p2_candidate is None or p2_candidate <= p1_candidate:
        return False, None
    square_and_k = p2_candidate ** 2 + k
    quotient, remainder = divmod(square_and_k, p1_candidate)
    if remainder != 0:
        return False, None
    if not has_prime_factor_greater_than(quotient, p1_candidate):
        return True, p2_candidate
    return False, None


def search_v2(k, offset, settings: Settings):
    results = []
    for iteration in range(settings.search_start + offset, settings.search_stop, settings.processes):
        if iteration % 1_000_000 == 0:
            print(f"offset: {offset} iteration: {iteration}")
        result = check_p1(k, iteration)
        if result[0]:
            p2 = result[1]
            results.append((k, iteration, p2))
    return results
    

def split_search_between_processes(k: int, settings: Settings) -> list[tuple[int, int, int]]:    
    pool = Pool()
    collective_results = [pool.apply_async(search_v2, [k, i, settings]) for i in range(settings.processes)]
    collective_answers = []
    for result in collective_results:
        collective_answers.extend(result.get())
    return collective_answers


def get_negative_even_squares_up_to(n):
    j = 1
    while n <= (j ** 2) * -1:
        j += 1
    res = [-(i ** 2) for i in range(1, j) if i % 2 == 0]
    return res


def main(settings: Settings):
    for k in range(settings.start_k, settings.stop_k):
        if k in get_negative_even_squares_up_to(settings.start_k):
            print(f"skipping negative even square number {k}")
            continue
        print(f"addition = {k}")
        collective_answers = split_search_between_processes(k, settings)
        print(collective_answers)
        if not collective_answers and settings.print_mode:
            print(f"{"*"*60}\nno results found for k: {k} in range {settings.search_start:,} to {settings.search_stop:,}")
        with open("results.csv", "a") as f:
            if len(collective_answers) > 10:
                # if many results for a given k only write first 10
                collective_answers = collective_answers[:10]
            writer = csv.writer(f)
            writer.writerows(collective_answers)
      

if __name__ == "__main__":
    settings = Settings(
        start_k=1,
        stop_k=2,
        search_start=1,
        search_stop=1_000_000,
        processes=9,
        print_mode=False
    )
    # execute main and print time taken
    start = time.time()
    main(settings)
    end = time.time()
    print(f"time taken = {end-start} seconds using {settings.processes} processes")
    try:
        os.system('say "your program has finished"')
    except Exception:
        pass
    with open("experiment_log.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow((settings.start_k, settings.stop_k, settings.search_start, settings.search_stop, end-start, datetime.datetime.now()))