"""
Plot the number of Goldbach pairs for each even number.
"""

from .base import GoldbachPlotBase
import matplotlib.pyplot as plt


class PlotGoldbachPairCounts(GoldbachPlotBase):
    @staticmethod
    def plot(goldbach_pairs, start=4, end=100, output=None):
        """
        Plot the number of Goldbach pairs for each even number in [start, end].
        """
        evens = list(range(start, end + 1, 2))
        counts = [len(goldbach_pairs.goldbach_pairs(n)) for n in evens]
        marker_size = GoldbachPlotBase.get_marker_size(len(evens))
        plt.figure(figsize=(10, 5))
        plt.plot(
            evens,
            counts,
            marker="o",
            linestyle="",
            color="blue",
            markersize=marker_size,
        )
        plt.xlabel("Even Number")
        plt.ylabel("Number of Goldbach Pairs")
        plt.title(f"Goldbach Pair Counts for Even Numbers in [{start},{end}]")
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        if output:
            plt.savefig(output)
        else:
            plt.show()
