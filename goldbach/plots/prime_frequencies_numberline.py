"""
Plot the frequency of each prime in Goldbach decompositions, ordered by the number line.
"""

from .base import GoldbachPlotBase
import matplotlib.pyplot as plt
from collections import Counter


class PlotPrimeFrequenciesNumberline(GoldbachPlotBase):
    @staticmethod
    def plot(decomposer, start=4, end=100, show_all_odds=False):
        """
        Plot the frequency of each prime in Goldbach decompositions, ordered by the number line.
        If show_all_odds is True, show every odd number on the x-axis (frequency 0 for non-primes).
        Otherwise, show only primes on the x-axis.
        """
        freq = Counter()
        for even_n in range(start, end + 1, 2):
            decomps = decomposer.goldbach_decompositions(even_n)
            for p, q in decomps:
                if p != 2:
                    freq[p] += 1
                if q != 2:
                    freq[q] += 1
        if not freq:
            print("No decompositions found in range.")
            return
        max_prime = max(freq)
        min_prime = min(freq)
        if show_all_odds:
            xs = list(range(min_prime, max_prime + 1, 2))
            ys = [freq[x] if x in freq else 0 for x in xs]
            label = "All Odd Numbers (excluding 2)"
        else:
            xs = sorted(freq.keys())
            ys = [freq[x] for x in xs]
            label = "Primes Only (excluding 2)"
        plt.figure(figsize=(16, 6))
        if show_all_odds:
            plt.bar(xs, ys, width=1.5, color="teal", alpha=0.8)
            plt.xlabel("Number (Odd Numbers)")
            step = max(1, len(xs) // 30)
            plt.xticks(xs[::step], xs[::step], rotation=45)
        else:
            bar_positions = list(range(len(xs)))
            plt.bar(
                bar_positions, ys, width=0.8, color="teal", alpha=0.8, align="center"
            )
            plt.xlabel("Prime Numbers (Consecutive)")
            plt.xticks(bar_positions, xs, rotation=45)
        plt.ylabel("Frequency in Goldbach Decompositions")
        plt.title(
            f"Prime Frequencies in Goldbach Decompositions [{start},{end}] (Ordered by Number Line)\n[{label}]"
        )
        plt.tight_layout()
        plt.show()
