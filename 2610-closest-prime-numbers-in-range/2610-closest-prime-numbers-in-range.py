class Solution(object):
    def closestPrimes(self, left, right):
        # Step 1: Use Sieve of Eratosthenes to precompute primes up to 'right'
        limit = right + 1
        is_prime = [True] * limit
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes

        for i in range(2, int(limit**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, limit, i):
                    is_prime[j] = False

        # Step 2: Extract primes within [left, right]
        possible_primes = [i for i in range(left, right + 1) if is_prime[i]]

        # Edge case: If there are fewer than 2 primes, return [-1, -1]
        if len(possible_primes) < 2:
            return [-1, -1]

        # Step 3: Find the closest prime pair in O(N) time
        min_pair = (possible_primes[0], possible_primes[1])
        min_diff = min_pair[1] - min_pair[0]

        for i in range(1, len(possible_primes) - 1):
            diff = possible_primes[i + 1] - possible_primes[i]
            if diff < min_diff:
                min_diff = diff
                min_pair = (possible_primes[i], possible_primes[i + 1])

        return list(min_pair)  # Convert tuple to list





        '''
        possible_primes = []
        for i in range(left, right + 1):
            if self.isprime(i):
                possible_primes.append(i)
        
        print(possible_primes) 
        
        if len(possible_primes) < 2: 
            return [-1, -1]

        min_diff = {}
        for i in range(1, len(possible_primes)):
            min_diff[(possible_primes[i], possible_primes[i - 1])] = possible_primes[i] - possible_primes[i - 1]

        min_pair = min(min_diff.items(), key=lambda x: (x[1], x[0]))[0]
        return sorted(list(min_pair))  

    def isprime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
        
1 Find all prime numbers in the given range [left, right].
2️ Store adjacent prime pairs and calculate their differences.
3️ Find the pair with the smallest difference using min().
4️ Handle ties by selecting the numerically smallest pair.
5️ Return [-1, -1] if fewer than two primes exist.
        
        '''