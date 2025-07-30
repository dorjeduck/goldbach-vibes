"""
Plot smallest and largest primes in Goldbach decompositions.
"""

from .base import GoldbachPlotBase
import matplotlib.pyplot as plt


class PlotSmallestLargestPrimes(GoldbachPlotBase):
    @staticmethod
    def plot(decomposer, start=4, end=100):
        """
        For each even number in [start, end], plot only the smallest and largest prime in the set of Goldbach decompositions.
        Smallest primes are plotted in orange, largest in green.
        """
        xs_small = []
        ys_small = []
        xs_large = []
        ys_large = []
        for even_n in range(start, end + 1, 2):
            decomps = decomposer.goldbach_decompositions(even_n)
            if decomps:
                p_values = [p for p, q in decomps]
                smallest = min(p_values)
                largest = max(p_values)
                xs_small.append(even_n)
                ys_small.append(smallest)
                xs_large.append(even_n)
                ys_large.append(largest)
        n_points = len(xs_small)
        marker_size = GoldbachPlotBase.get_marker_size(n_points)
        plt.figure(figsize=(12, 6))
        plt.scatter(
            xs_small,
            ys_small,
            s=marker_size,
            color="orange",
            alpha=0.8,
            label="Smallest Prime",
        )
        plt.scatter(
            xs_large,
            ys_large,
            s=marker_size,
            color="green",
            alpha=0.8,
            label="Largest Prime",
        )
        plt.xlabel("Even Number (2n)")
        plt.ylabel("Prime in Decomposition")
        plt.title(
            f"Smallest and Largest Primes in Goldbach Decompositions [{start},{end}]"
        )
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
