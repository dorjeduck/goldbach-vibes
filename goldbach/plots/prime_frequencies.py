"""
Plot the top N most frequent primes in Goldbach decompositions.
"""

from .base import GoldbachPlotBase
import matplotlib.pyplot as plt
from collections import Counter


class PlotPrimeFrequencies(GoldbachPlotBase):
    @staticmethod
    def plot(decomposer, start=4, end=100, top_n=30):
        """
        For all even numbers in [start, end], count how often each prime appears in any Goldbach decomposition.
        Plot the top_n most frequent primes as a bar chart.
        """
        freq = Counter()
        for even_n in range(start, end + 1, 2):
            decomps = decomposer.goldbach_decompositions(even_n)
            for p, q in decomps:
                freq[p] += 1
                freq[q] += 1
        if not freq:
            print("No decompositions found in range.")
            return
        most_common = freq.most_common(top_n)
        primes, counts = zip(*most_common)
        plt.figure(figsize=(14, 6))
        plt.bar(range(len(primes)), counts, color="teal", alpha=0.8)
        plt.xticks(range(len(primes)), primes, rotation=45)
        plt.xlabel("Prime Number")
        plt.ylabel("Frequency in Goldbach Decompositions")
        plt.title(
            f"Top {top_n} Most Frequent Primes in Goldbach Decompositions [{start},{end}]"
        )
        plt.tight_layout()
        plt.show()
