"""
Plot the frequency of each prime in Goldbach decompositions, ordered by the number line.
"""

from .base import GoldbachPlotBase
import matplotlib.pyplot as plt
from collections import Counter


class PlotPrimeFrequenciesNumberline(GoldbachPlotBase):
    @staticmethod
    def plot(goldbach_pairs, start=4, end=100, show_all_odds=False, output=None):
        """
        Plot the frequency of each prime in Goldbach decompositions, ordered by the number line.
        If show_all_odds is True, show every odd number on the x-axis (frequency 0 for non-primes).
        Otherwise, show only primes on the x-axis.

        :param goldbach_pairs: Instance of GoldbachPairs to generate decompositions.
        :param start: Starting even number (inclusive) for Goldbach decompositions.
        :param end: Ending even number (inclusive) for Goldbach decompositions.
        :param show_all_odds: If True, include all odd numbers in the plot range.
        :param output: File path to save the plot as an image. If None, the plot will be shown but not saved.
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
        if output:
            plt.savefig(output)
        else:
            plt.show()
