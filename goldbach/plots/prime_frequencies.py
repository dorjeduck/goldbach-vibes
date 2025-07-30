"""
Plot the top N most frequent primes in Goldbach decompositions.
"""

from .base import GoldbachPlotBase
import matplotlib.pyplot as plt
from collections import Counter


class PlotPrimeFrequencies(GoldbachPlotBase):
    @staticmethod
    def plot(goldbach_pairs, start=4, end=100, top_n=30):
        """
        For all even numbers in [start, end], count how often each prime appears in any Goldbach decomposition.
        Plot the top_n most frequent primes as a bar chart.
        """
        prime_counter = Counter()
        for even_n in range(start, end + 1, 2):
            decomps = goldbach_pairs.goldbach_pairs(even_n)
            for p, q in decomps:
                prime_counter[p] += 1
                prime_counter[q] += 1
        most_common = prime_counter.most_common(top_n)
        primes, freqs = zip(*most_common) if most_common else ([], [])
        plt.figure(figsize=(12, 6))
        plt.bar(primes, freqs, color="purple")
        plt.xlabel("Prime")
        plt.ylabel("Frequency in Goldbach Pairs")
        plt.title(
            f"Top {top_n} Most Frequent Primes in Goldbach Pairs for [{start},{end}]"
        )
        plt.tight_layout()
        plt.show()
