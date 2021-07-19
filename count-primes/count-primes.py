class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        prime = [1]*n
        prime[0] = 0
        prime[1] = 0
        p = 2
        # count = n-2
        while p*p <= n:
            if prime[p]:
                prime[p*p:n:p] = [0] * (1+(n-p*p-1) // p)
            if p == 2:
                p += 1
            else:
                p += 2
        # count = 0
        # for i in range(2, n):
        #     if prime[i]:
        #         count += 1
        return sum(prime)