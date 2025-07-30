"""
Boxplot of |p-n| for Goldbach decompositions.
"""

from .base import GoldbachPlotBase
import matplotlib.pyplot as plt
import numpy as np


class PlotDistanceBoxplots(GoldbachPlotBase):
    @staticmethod
    def plot(goldbach_pairs, start=4, end=100, normalize=False, showfliers=False):
        """
        For each even number in [start, end], plot a boxplot of |p-n| for all Goldbach decompositions.
        If normalize is True, distances are divided by n.
        """
        evens = list(range(start, end + 1, 2))
        data = []
        for even_n in evens:
            dists = goldbach_pairs.decomposition_distances(even_n)
            n = even_n // 2
            if normalize and dists:
                data.append([d / n for d in dists])
            else:
                data.append(dists)
        plt.figure(figsize=(14, 6))
        plt.boxplot(
            data,
            positions=evens,
            widths=1.5,
            showfliers=showfliers,
            patch_artist=True,
            boxprops=dict(facecolor="lightblue", alpha=0.7),
        )
        plt.xlabel("Even Numbers")
        if normalize:
            plt.ylabel("Normalized |p - n| / n")
            plt.title(
                f"Boxplot of Normalized |p - n| for Even Numbers in [{start},{end}]"
            )
        else:
            plt.ylabel("|p - n| (Distance from Center)")
            plt.title(f"Boxplot of |p - n| for Even Numbers in [{start},{end}]")
        plt.grid(True, axis="y", alpha=0.3)
        # Show fewer x-ticks for clarity
        step = max(1, len(evens) // 20)
        plt.xticks(evens[::step])
        plt.tight_layout()
        plt.show()
