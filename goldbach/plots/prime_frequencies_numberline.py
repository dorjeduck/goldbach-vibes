"""
Plot the frequency of each prime in Goldbach decompositions, ordered by the number line.
"""

from .base import GoldbachPlotBase
import matplotlib.pyplot as plt
from collections import Counter


class PlotPrimeFrequenciesNumberline(GoldbachPlotBase):
    @staticmethod
    def plot(goldbach_pairs, start=4, end=100, show_all_odds=False):
        """
        Plot the frequency of each prime in Goldbach decompositions, ordered by the number line.
        If show_all_odds is True, show every odd number on the x-axis (frequency 0 for non-primes).
        Otherwise, show only primes on the x-axis.
        """
        prime_counter = Counter()
        for even_n in range(start, end + 1, 2):
            decomps = goldbach_pairs.goldbach_pairs(even_n)
            for p, q in decomps:
                prime_counter[p] += 1
                prime_counter[q] += 1
        primes, freqs = (
            zip(*sorted(prime_counter.items())) if prime_counter else ([], [])
        )
        plt.figure(figsize=(12, 6))
        plt.stem(primes, freqs, basefmt=" ", use_line_collection=True)
        plt.xlabel("Prime")
        plt.ylabel("Frequency in Goldbach Pairs")
        plt.title(f"Prime Frequencies in Goldbach Pairs for [{start},{end}]")
        plt.tight_layout()
        plt.show()
