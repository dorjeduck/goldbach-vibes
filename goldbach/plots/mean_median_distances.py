"""
Plot mean and median |p-n| for Goldbach decompositions.
"""

from .base import GoldbachPlotBase
import matplotlib.pyplot as plt
import numpy as np


class PlotMeanMedianDistances(GoldbachPlotBase):
    @staticmethod
    def plot(goldbach_pairs, start=4, end=100, normalize=False):
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
            if dists:
                mean = np.mean(dists)
                median = np.median(dists)
                if normalize:
                    means.append(mean / n)
                    medians.append(median / n)
                else:
                    means.append(mean)
                    medians.append(median)
            else:
                means.append(np.nan)
                medians.append(np.nan)
        plt.figure(figsize=(12, 6))
        if normalize:
            plt.plot(evens, means, label="Mean |p - n| / n", color="orange")
            plt.plot(evens, medians, label="Median |p - n| / n", color="green")
            plt.ylabel("Normalized Distance from Center (|p - n| / n)")
        else:
            plt.plot(evens, means, label="Mean |p - n|", color="orange")
            plt.plot(evens, medians, label="Median |p - n|", color="green")
            plt.ylabel("Distance from Center (|p - n|)")
        plt.xlabel("Even Numbers")
        plt.title(
            f"Mean and Median |p - n| for Even Numbers in [{start},{end}]"
            + (" (normalized)" if normalize else "")
        )
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
