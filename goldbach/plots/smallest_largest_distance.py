"""
Plot distance between smallest and largest p in Goldbach decompositions.
"""

from .base import GoldbachPlotBase
import matplotlib.pyplot as plt


class PlotSmallestLargestDistance(GoldbachPlotBase):
    @staticmethod
    def plot(decomposer, start=4, end=100):
        """
        For each even number in [start, end], plot the distance between the smallest and largest p in the decompositions.
        """
        xs = []
        ys = []
        for even_n in range(start, end + 1, 2):
            decomps = decomposer.goldbach_decompositions(even_n)
            if decomps:
                p_values = [p for p, q in decomps]
                dist = max(p_values) - min(p_values)
                xs.append(even_n)
                ys.append(dist)
        plt.figure(figsize=(12, 6))
        marker_size = GoldbachPlotBase.get_marker_size(len(xs))
        plt.scatter(xs, ys, s=marker_size, color="purple", alpha=0.7)
        plt.xlabel("Even Number (2n)")
        plt.ylabel("Distance between Smallest and Largest p")
        plt.title(
            f"Distance between Smallest and Largest p in Goldbach Decompositions [{start},{end}]"
        )
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
