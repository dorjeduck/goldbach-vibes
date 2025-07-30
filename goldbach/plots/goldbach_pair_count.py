"""
Plot the number of Goldbach pairs for each even number.
"""

from .base import GoldbachPlotBase
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker


class PlotGoldbachPairCounts(GoldbachPlotBase):
    @staticmethod
    def plot(goldbach_pairs, start=4, end=100, output=None):
        """
        Plot the number of Goldbach pairs for each even number in [start, end].
        """
        evens = list(range(start, end + 1, 2))
        counts = [len(goldbach_pairs.goldbach_pairs(n)) for n in evens]
        marker_size = GoldbachPlotBase.get_marker_size(len(evens))
        plt.figure(figsize=(12, 6))
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
        # Add a larger margin to the x-axis, but only label ticks for actual evens in the range
        margin = (max(evens) - min(evens)) * 0.02
        left = min(evens) - margin
        right = max(evens) + margin
        plt.xlim(left, right)
        ax = plt.gca()
        ax.xaxis.set_major_locator(mticker.MultipleLocator(2))
        ax.xaxis.set_minor_locator(mticker.NullLocator())
        # Only label ticks for evens in the range, not for the margin
        ticks = [e for e in evens if left < e < right]
        ax.set_xticks(ticks)
        ax.set_xticklabels([str(e) for e in ticks], rotation=0)
        ax.yaxis.set_major_locator(mticker.MaxNLocator(integer=True))
        plt.tight_layout()
        if output:
            plt.savefig(output)
        else:
            plt.show()
