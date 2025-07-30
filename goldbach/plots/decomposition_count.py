"""
Plot the number of Goldbach decompositions for each even number.
"""

from .base import GoldbachPlotBase
import matplotlib.pyplot as plt


class PlotDecompositionCounts(GoldbachPlotBase):
    @staticmethod
    def plot(decomposer, start=4, end=100, output=None):
        """
        Plot the number of Goldbach decompositions for each even number in [start, end].
        """
        evens = list(range(start, end + 1, 2))
        counts = [len(decomposer.goldbach_decompositions(n)) for n in evens]
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
        plt.ylabel("Number of Goldbach Decompositions")
        plt.title(f"Goldbach Decomposition Counts for Even Numbers in [{start},{end}]")
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        if output:
            plt.savefig(output)
        else:
            plt.show()
