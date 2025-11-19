class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        
        # Sieve of Erathosthenes
        i = 2
        while i * i < n:
            if is_prime[i]:
                # Mark all multiples of i as not prime
                # Start from i * i b/c smaller multiples are already marked
                for j in range(i * i, n, i):
                    is_prime[j] = False
                
            i += 1
        return sum(is_prime)