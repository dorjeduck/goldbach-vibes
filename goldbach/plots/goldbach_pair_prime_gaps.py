"""
Plot prime gaps for Goldbach pairs.
"""

from .base import GoldbachPlotBase
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker


class PlotGoldbachPrimeGaps(GoldbachPlotBase):
    @staticmethod
    def plot(goldbach_pairs, start=4, end=100, output=None):
        """
        For each even number in [start, end], plot all prime gaps (q - p) for Goldbach pairs as a scatter plot.
        X-axis: even number, Y-axis: q - p for each Goldbach pair.
        Marker size is chosen based on the number of points.
        """
        xs = []
        ys = []
        for even_n in range(start, end + 1, 2):
            for gap in goldbach_pairs.prime_gaps(even_n):
                xs.append(even_n)
                ys.append(gap)
        evens = list(range(start, end + 1, 2))
        marker_size = GoldbachPlotBase.get_marker_size(len(evens))

        plt.figure(figsize=(12, 6))
        plt.scatter(xs, ys, s=marker_size**2, alpha=0.6, color="blue")
        plt.xlabel("Even Number")
        plt.ylabel("Prime Gaps (q - p)")
        plt.title(f"Prime Gaps in Goldbach Pairs for Even Numbers in [{start},{end}]")
        plt.grid(True, alpha=0.3)
        # Add a larger margin to the x-axis, but only label ticks for actual evens
        margin = (max(evens) - min(evens)) * 0.02
        plt.xlim(min(evens) - margin, max(evens) + margin)
        ax = plt.gca()
        ax.xaxis.set_major_locator(mticker.FixedLocator(evens))
        ax.xaxis.set_minor_locator(mticker.NullLocator())
        ax.set_xticklabels([str(e) for e in evens], rotation=0)
        plt.tight_layout()
        if output:
            plt.savefig(output)
        else:
            plt.show()
