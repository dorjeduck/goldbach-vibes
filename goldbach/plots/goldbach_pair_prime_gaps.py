"""
Plot prime gaps for Goldbach pairs.
"""

from .base import GoldbachPlotBase
import matplotlib.pyplot as plt


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
        n_points = len(xs)
        marker_size = GoldbachPlotBase.get_marker_size(n_points)
        plt.figure(figsize=(12, 6))
        plt.scatter(xs, ys, s=marker_size, alpha=0.6, color="blue")
        plt.xlabel("Even Number")
        plt.ylabel("Prime Gap (q - p)")
        plt.title(f"Prime Gaps in Goldbach Pairs for Even Numbers in [{start},{end}]")
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        if output:
            plt.savefig(output)
        else:
            plt.show()
