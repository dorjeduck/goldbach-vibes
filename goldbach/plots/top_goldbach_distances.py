"""
Plot module for visualizing top Goldbach distances.
"""

import matplotlib.pyplot as plt
import os
from .base import BasePlot


class TopGoldbachDistancesPlot(BasePlot):
    """Plot the top N numbers with largest Goldbach distances."""

    def plot(self, start=3, end=100, top_n=10, output_file=None):
        """
        Create a bar plot showing the top N numbers with largest Goldbach distances.

        Args:
            start: Starting number for analysis
            end: Ending number for analysis
            top_n: Number of top results to show
            output_file: Optional filename to save the plot
        """
        top_distances = self.goldbach_pairs.top_goldbach_distances(start, end, top_n)

        if not top_distances:
            print("No valid Goldbach distances found in the given range.")
            return

        # Extract data for plotting
        numbers = [n for n, _ in top_distances]
        distances = [distance for _, distance in top_distances]

        # Create the plot
        plt.figure(figsize=(12, 8))

        # Create bar plot with different colors for different distance values
        unique_distances = sorted(set(distances), reverse=True)
        colors = plt.cm.viridis(range(len(unique_distances)))
        color_map = {dist: colors[i] for i, dist in enumerate(unique_distances)}
        bar_colors = [color_map[dist] for dist in distances]

        bars = plt.bar(
            range(len(numbers)),
            distances,
            color=bar_colors,
            alpha=0.8,
            edgecolor="black",
            linewidth=0.5,
        )

        # Customize the plot
        plt.xlabel("Numbers (n)", fontsize=12)
        plt.ylabel("Goldbach Distance", fontsize=12)
        plt.title(
            f"Top {top_n} Largest Goldbach Distances in Range [{start}, {end}]",
            fontsize=14,
            fontweight="bold",
        )

        # Set x-axis labels to show the actual numbers
        plt.xticks(
            range(len(numbers)), numbers, rotation=45 if len(numbers) > 15 else 0
        )

        # Add value labels on top of bars
        for i, (bar, distance) in enumerate(zip(bars, distances)):
            plt.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 0.1,
                str(distance),
                ha="center",
                va="bottom",
                fontsize=10,
                fontweight="bold",
            )

        # Add a legend showing distance ranges
        legend_elements = []
        for dist in unique_distances:
            count = distances.count(dist)
            legend_elements.append(
                plt.Rectangle(
                    (0, 0),
                    1,
                    1,
                    fc=color_map[dist],
                    alpha=0.8,
                    label=f"Distance {dist} ({count} numbers)",
                )
            )
        plt.legend(handles=legend_elements, loc="upper right", fontsize=10)

        # Improve layout
        plt.grid(axis="y", alpha=0.3)
        plt.tight_layout()

        # Save or show the plot
        if output_file:
            self.save_plot(output_file)
        else:
            filename = f"top_goldbach_distances_{start}_{end}_top{top_n}.png"
            self.save_plot(filename)


def plot_top_goldbach_distances(start=3, end=100, top_n=10, output_file=None):
    """
    Convenience function to create a top Goldbach distances plot.

    Args:
        start: Starting number for analysis
        end: Ending number for analysis
        top_n: Number of top results to show
        output_file: Optional filename to save the plot
    """
    plotter = TopGoldbachDistancesPlot()
    plotter.plot(start, end, top_n, output_file)
