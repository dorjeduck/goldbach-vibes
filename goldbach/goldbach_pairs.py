"""
Goldbach Pairs: Efficiently computes all Goldbach pairs for even numbers in a range.
"""


class GoldbachPairs:
    """
    Main class for computing Goldbach pairs and related statistics.
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

    def goldbach_pairs(self, even_n):
        """Return all Goldbach pairs (p, q) with p <= q, p + q = even_n."""
        self.ensure_sieve(even_n)
        pairs = []
        for p in self.primes:  # already sorted
            q = even_n - p
            if q < p:
                break
            if q in self.primes_set:
                pairs.append((p, q))
        return pairs

    def decomposition_distances(self, even_n):
        """
        For a given even number 2n, return a sorted list of |p - n| for each Goldbach decomposition (p, q).
        """
        if even_n % 2 != 0 or even_n < 4:
            raise ValueError("Input must be an even number >= 4")
        n = even_n // 2
        pairs = self.goldbach_pairs(even_n)
        distances = sorted(abs(p - n) for p, q in pairs)
        return distances

    def prime_gaps(self, even_n):
        """
        For a given even number, return a sorted list of q - p for each Goldbach pair (p, q).
        """
        if even_n % 2 != 0 or even_n < 4:
            raise ValueError("Input must be an even number >= 4")
        pairs = self.goldbach_pairs(even_n)
        gaps = sorted(q - p for p, q in pairs)
        return gaps

    def analyze_range(self, start=4, end=100, show_decompositions=True):
        if start % 2 != 0:
            start += 1
        if end % 2 != 0:
            end -= 1
        self.ensure_sieve(end)
        if not show_decompositions:
            counts = []
            evens = list(range(start, end + 1, 2))
            for n in evens:
                pairs = self.goldbach_pairs(n)
                counts.append(len(pairs))
            print(f"[{start},{end}]")
            print(counts)
        else:
            for n in range(start, end + 1, 2):
                pairs = self.goldbach_pairs(n)
                label = "Goldbach pair" if len(pairs) == 1 else "Goldbach pairs"
                print(f"{n}: {len(pairs)} {label}")
                for p, q in pairs:
                    print(f"  {n} = {p} + {q}")
                print()
