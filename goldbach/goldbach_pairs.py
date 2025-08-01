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

    def sieve_primes(self, limit):
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

    def get(self, even_n):
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

    def prime_gaps(self, even_n):
        """
        For a given even number, return a sorted list of q - p for each Goldbach pair (p, q).
        """
        if even_n % 2 != 0 or even_n < 4:
            raise ValueError("Input must be an even number >= 4")
        pairs = self.get_goldbach_pairs(even_n)
        gaps = sorted(q - p for p, q in pairs)
        return gaps

    def pair_with_smallest_lower_prime(self, even_n):
        """
        For a given even number, return the Goldbach pair (p, q) with the largest lower prime p.
        Returns None if no such pair exists.
        """
        self.ensure_sieve(even_n)
        pairs = self.get(even_n)
        if not pairs:
            return None
        return min(pairs, key=lambda pair: pair[0])

    def pair_with_largest_lower_prime(self, even_n):
        """
        For a given even number, return the Goldbach pair (p, q) with the largest lower prime p.
        Returns None if no such pair exists.
        """
        self.ensure_sieve(even_n)
        pairs = self.get(even_n)
        if not pairs:
            return None
        return max(pairs, key=lambda pair: pair[0])

    def count_pairs_with_upper_twin_prime(self, even_n):
        """
        For a given even number, return the count of Goldbach pairs (p, q) where either p or q is an upper twin prime (i.e., p and p-2 are prime, or q and q-2 are prime).
        """
        self.ensure_sieve(even_n)
        pairs = self.get(even_n)
        count = 0
        for p, q in pairs:
            if (p - 2 in self.primes_set) or (q - 2 in self.primes_set):
                count += 1
        return count

    def count_pairs_with_lower_twin_prime(self, even_n):
        """
        For a given even number, return the count of Goldbach pairs (p, q) where either p or q is a lower twin prime (i.e., p and p+2 are prime, or q and q+2 are prime).
        """
        self.ensure_sieve(even_n)
        pairs = self.get(even_n)
        count = 0
        for p, q in pairs:
            if (p + 2 in self.primes_set) or (q + 2 in self.primes_set):
                count += 1
        return count

    def is_critical_even_number(self, even_n):
        """
        Return True if the even number has no upper twin primes in any of its Goldbach pairs.
        These are 'critical' numbers that cannot inherit their Goldbach property from even_n-2.
        """
        return self.count_pairs_with_upper_twin_prime(even_n) == 0

    def get_critical_even_numbers(self, start, end):
        """
        Return a list of critical even numbers in the range [start, end].
        Critical numbers have no upper twin primes in any of their Goldbach pairs.
        """
        critical_numbers = []
        for n in range(start + (start % 2), end + 1, 2):  # ensure even numbers only
            if self.is_critical_even_number(n):
                critical_numbers.append(n)
        return critical_numbers

    def critical_density_by_subrange(self, start, end, subrange_size=100):
        """
        Analyze the density of critical even numbers across subranges.
        Returns a list of tuples: (subrange_start, subrange_end, critical_count, total_evens_in_subrange)
        """
        results = []
        current_start = start

        while current_start <= end:
            current_end = min(current_start + subrange_size - 1, end)
            if current_end % 2 == 1:  # ensure even end
                current_end -= 1

            critical_numbers = self.get_critical_even_numbers(
                current_start, current_end
            )
            total_evens = len(
                range(current_start + (current_start % 2), current_end + 1, 2)
            )

            results.append(
                (current_start, current_end, len(critical_numbers), total_evens)
            )
            current_start += subrange_size

        return results
