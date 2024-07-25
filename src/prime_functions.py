import numpy as np


def generate_primes(n: int):
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
