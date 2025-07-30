"""
Plot mean and median |p-n| for Goldbach decompositions.
"""

from .base import GoldbachPlotBase
import matplotlib.pyplot as plt
import numpy as np


class PlotMeanMedianDistances(GoldbachPlotBase):
    @staticmethod
    def plot(goldbach_pairs, start=4, end=100, normalize=False, output=None):
        """
        For each even number in [start, end], plot the mean and median |p-n| as a function of the even number.
        If normalize is True, plot mean and median divided by n (the center).
        """
        evens = list(range(start, end + 1, 2))
        means = []
        medians = []
        for even_n in evens:
            dists = goldbach_pairs.decomposition_distances(even_n)
            n = even_n // 2
            if normalize and dists:
                dists = [d / n for d in dists]
            if dists:
                means.append(np.mean(dists))
                medians.append(np.median(dists))
            else:
                means.append(0)
                medians.append(0)
        plt.figure(figsize=(12, 6))
        plt.plot(evens, means, label="Mean", color="blue")
        plt.plot(evens, medians, label="Median", color="red")
        plt.xlabel("Even Number")
        if normalize:
            plt.ylabel("Normalized |p - n| / n")
            plt.title(
                f"Mean/Median of Normalized |p - n| for Even Numbers in [{start},{end}]"
            )
        else:
            plt.ylabel("|p - n| (Distance from Center)")
            plt.title(f"Mean/Median of |p - n| for Even Numbers in [{start},{end}]")
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        if output:
            plt.savefig(output)
        else:
            plt.show()
