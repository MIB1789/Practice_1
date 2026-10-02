def sieve_of_eratosthenes(n):
    if n < 2:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p <= n:
        # Если число p осталось истинным, значит оно простое
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1

    primes = [i for i in range(2, n + 1) if is_prime[i]]
    return primes

N = 100000
print(f"Простые числа в диапазоне [2, {N}]: {sieve_of_eratosthenes(N)}")
