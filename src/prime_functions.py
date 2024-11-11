from typing import Any
import numpy as np

type Primes = np.ndarray[Any, np.dtype[np.intp]]

def generate_primes(n: int) -> Primes:
    def sieve(limit):
        is_prime = np.ones(limit + 1, dtype=bool)
        is_prime[:2] = False
        for p in range(2, int(limit**0.5) + 1):
            if is_prime[p]:
                is_prime[p * p : limit + 1 : p] = False
        return np.nonzero(is_prime)[0]

    limit = int(n * np.log(n) * 1.2)
    primes = sieve(limit)
    return primes[:n]

def generate_prime_indices(n: int) -> np.ndarray:
    primes = generate_primes(n)
    return primes[primes <= n]

def generate_prime_of_primes(n: int) -> Primes:
    primes = generate_primes(n)
    prime_indices = generate_prime_indices(len(primes))
    return primes[prime_indices - 1]

def subtract_primes_by_index(n: int) -> Primes:
    primes = generate_primes(n)
    indices = np.arange(1, n + 1)  # Generate indices starting from 1 to n
    return primes - indices

def generate_prime_fractions(n: int) -> np.ndarray:
    primes = generate_primes(n)

    numerators = np.arange(1, n + 1)

    return numerators / primes