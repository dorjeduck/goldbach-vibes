"""
Goldbach Decomposer: Efficiently computes all Goldbach decompositions for even numbers in a range.
"""


class GoldbachDecomposer:
    """
    Main class for computing Goldbach decompositions and related statistics.
    Sieve is built and expanded automatically as needed.
    """

    def __init__(self):
        self.max_n = 0
        self.primes = []
        self.primes_set = set()

    @staticmethod
    def sieve_primes(limit):
        """Return a list of all primes <= limit using Sieve of Eratosthenes."""
        sieve = [True] * (limit + 1)
        sieve[0:2] = [False, False]
        for i in range(2, int(limit**0.5) + 1):
            if sieve[i]:
                sieve[i * i : limit + 1 : i] = [False] * len(range(i * i, limit + 1, i))
        return [i for i, is_prime in enumerate(sieve) if is_prime]

    def ensure_sieve(self, upto):
        """Ensure the sieve is computed up to the given limit."""
        if upto > self.max_n:
            self.primes = self.sieve_primes(upto)
            self.primes_set = set(self.primes)
            self.max_n = upto

    def goldbach_decompositions(self, even_n):
        """Return all pairs of primes (p, q) with p <= q, p + q = even_n."""
        self.ensure_sieve(even_n)
        decomps = []
        for p in self.primes:  # already sorted
            q = even_n - p
            if q < p:
                break
            if q in self.primes_set:
                decomps.append((p, q))
        return decomps

    def decomposition_distances(self, even_n):
        """
        For a given even number 2n, return a sorted list of |p - n| for each Goldbach decomposition (p, q).
        """
        if even_n % 2 != 0 or even_n < 4:
            raise ValueError("Input must be an even number >= 4")
        n = even_n // 2
        decomps = self.goldbach_decompositions(even_n)
        distances = sorted(abs(p - n) for p, q in decomps)
        return distances

    def analyze_range(self, start=4, end=100, show_decompositions=True):
        """
        For all even numbers in [start, end], print all Goldbach decompositions.
        If show_decompositions is False, only print the count for each n.
        """
        if start % 2 != 0:
            start += 1
        if end % 2 != 0:
            end -= 1
        self.ensure_sieve(end)
        if not show_decompositions:
            counts = []
            evens = list(range(start, end + 1, 2))
            for n in evens:
                decomps = self.goldbach_decompositions(n)
                counts.append(len(decomps))
            print(f"[{start},{end}]")
            print(counts)
        else:
            for n in range(start, end + 1, 2):
                decomps = self.goldbach_decompositions(n)
                print(f"{n}: {len(decomps)} decompositions")
                for p, q in decomps:
                    print(f"  {n} = {p} + {q}")
                print()
