"""
Plot decomposition distances for Goldbach decompositions.
"""

from .base import GoldbachPlotBase
import matplotlib.pyplot as plt


class PlotDecompositionDistances(GoldbachPlotBase):
    @staticmethod
    def plot(decomposer, start=4, end=100):
        """
        For each even number in [start, end], plot all decomposition distances as a scatter plot.
        X-axis: even number, Y-axis: |p - n| for each decomposition.
        Marker size is chosen based on the number of points.
        """
        xs = []
        ys = []
        for even_n in range(start, end + 1, 2):
            n = even_n // 2
            for d in decomposer.decomposition_distances(even_n):
                xs.append(even_n)
                ys.append(d)
        n_points = len(xs)
        marker_size = GoldbachPlotBase.get_marker_size(n_points)
        plt.figure(figsize=(12, 6))
        plt.scatter(xs, ys, s=marker_size, alpha=0.6, color="blue")
        plt.xlabel("Even Number (2n)")
        plt.ylabel("|p - n| (Distance from Center)")
        plt.title(
            f"Goldbach Decomposition Distances for Even Numbers in [{start},{end}]"
        )
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
