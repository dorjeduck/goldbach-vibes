"""
Plot module for visualizing Goldbach distances as circles.
"""

import matplotlib.pyplot as plt
import numpy as np
import os
from .base import BasePlot


class GoldbachDistanceCirclesPlot(BasePlot):
    """Plot Goldbach distances as circles centered at numbers."""

    def plot(self, start=2, end=30, clean_mode=True, output_file=None):
        """
        Create a geometric visualization of Goldbach distances as circles.
        Each number n is shown with a circle of radius d (Goldbach distance)
        that intersects the x-axis at n-d and n+d (both primes).

        Args:
            start: Starting number for analysis
            end: Ending number for analysis
            clean_mode: If True, use thinner circles and no info boxes for large ranges
            output_file: Optional filename to save the plot
        """
        fig, ax = plt.subplots(figsize=(20, 12))

        # Set up the plot
        max_distance = 0
        valid_numbers = []

        # First pass: find valid numbers and max distance
        for n in range(start, end + 1):
            distance = self.goldbach_pairs.goldbach_distance(n)
            if distance > 0:  # Only show numbers with valid distances
                valid_numbers.append((n, distance))
                max_distance = max(max_distance, distance)

        if not valid_numbers:
            print("No valid Goldbach distances found in range.")
            return

        # Set up coordinate system - calculate needed space for full circles
        x_range = end - start + 1
        y_max = max_distance + 3

        # Calculate the actual space needed on left and right sides by checking ALL circles
        min_x_extent = start  # leftmost point any circle reaches
        max_x_extent = end  # rightmost point any circle reaches

        for n, distance in valid_numbers:
            # Each circle at position n with radius distance extends from (n-distance) to (n+distance)
            circle_left = n - distance
            circle_right = n + distance

            min_x_extent = min(min_x_extent, circle_left)
            max_x_extent = max(max_x_extent, circle_right)

        # Add small buffer for visual clarity
        left_space = start - min_x_extent + 1
        right_space = max_x_extent - end + 1

        # Add small buffer for clean visualization
        buffer = 2
        left_space += buffer
        right_space += buffer

        # Plot the number line (x-axis)
        ax.axhline(y=0, color="black", linewidth=3, alpha=0.8)

        # Mark all integers on the number line
        range_size = end - start + 1

        # Determine labeling strategy based on range size and clean_mode
        if clean_mode or range_size > 50:
            # For large ranges, label every 10th or 20th number
            label_interval = 20 if range_size > 100 else 10
            marker_size = 3 if clean_mode else 4
        else:
            # For small ranges, label every 5th number or numbers in range
            label_interval = 5
            marker_size = 5

        for i in range(start - left_space, end + right_space + 1):
            if i >= start - max_distance and i <= end + max_distance:
                ax.plot(i, 0, "ko", markersize=marker_size, alpha=0.6)

                # Smart labeling based on range size
                should_label = False
                if clean_mode or range_size > 50:
                    should_label = i % label_interval == 0
                else:
                    should_label = i % 5 == 0 or (start <= i <= end)

                if should_label:
                    ax.text(
                        i,
                        -y_max * 0.15,
                        str(i),
                        ha="center",
                        va="top",
                        fontsize=8 if clean_mode else 10,
                        alpha=0.8,
                    )

        # Mark primes with special symbols
        primes_in_range = [
            p
            for p in self.goldbach_pairs.primes
            if start - max_distance <= p <= end + max_distance
        ]
        for p in primes_in_range:
            if start <= p <= end:
                prime_marker_size = 6 if clean_mode else 8
                ax.plot(p, 0, "ro", markersize=prime_marker_size, alpha=0.9)
                if not clean_mode:  # Only show "P" labels in detailed mode
                    ax.text(
                        p,
                        y_max * 0.05,
                        "P",
                        ha="center",
                        va="bottom",
                        fontsize=10,
                        color="red",
                        fontweight="bold",
                    )
            else:
                ax.plot(
                    p, 0, "ro", markersize=4 if clean_mode else 6, alpha=0.7
                )  # Smaller for primes outside main range

        # Plot circles for each number
        colors = plt.cm.viridis(np.linspace(0, 1, len(valid_numbers)))

        for i, (n, distance) in enumerate(valid_numbers):
            # Draw the circle - thinner for clean mode
            line_width = 1.5 if clean_mode else 3
            circle = plt.Circle(
                (n, 0),
                distance,
                fill=False,
                color=colors[i],
                linewidth=line_width,
                alpha=0.8,
            )
            ax.add_patch(circle)

            # Mark the intersection points (n-d and n+d)
            left_point = n - distance
            right_point = n + distance

            # Verify these are primes and mark them
            intersection_marker_size = 6 if clean_mode else 10
            if left_point in self.goldbach_pairs.primes_set:
                ax.plot(
                    left_point, 0, "go", markersize=intersection_marker_size, alpha=0.9
                )
            if right_point in self.goldbach_pairs.primes_set:
                ax.plot(
                    right_point, 0, "go", markersize=intersection_marker_size, alpha=0.9
                )

            # Add distance label only in detailed mode
            if not clean_mode:
                ax.text(
                    n,
                    distance + y_max * 0.05,
                    f"n={n}\nd={distance}",
                    ha="center",
                    va="bottom",
                    fontsize=11,
                    bbox=dict(boxstyle="round,pad=0.4", facecolor=colors[i], alpha=0.4),
                )

            # Draw vertical line from center to top of circle (optional in clean mode)
            if not clean_mode:
                ax.plot(
                    [n, n],
                    [0, distance],
                    color=colors[i],
                    linestyle="--",
                    alpha=0.6,
                    linewidth=2,
                )

        # Customize the plot
        ax.set_xlim(start - left_space, end + right_space)
        ax.set_ylim(-y_max, y_max)
        ax.set_xlabel("Number Line", fontsize=14)
        ax.set_ylabel("Goldbach Distance (Radius)", fontsize=14)
        ax.set_title(
            f"Goldbach Distances as Circles\nRange [{start}, {end}] - Circles intersect x-axis at symmetric primes",
            fontsize=16,
            fontweight="bold",
        )

        # Add legend
        legend_elements = [
            plt.Line2D(
                [0],
                [0],
                marker="o",
                color="w",
                markerfacecolor="black",
                markersize=8,
                label="Numbers",
                alpha=0.6,
            ),
            plt.Line2D(
                [0],
                [0],
                marker="o",
                color="w",
                markerfacecolor="red",
                markersize=8,
                label="Primes in range",
                alpha=0.8,
            ),
            plt.Line2D(
                [0],
                [0],
                marker="o",
                color="w",
                markerfacecolor="green",
                markersize=10,
                label="Prime intersections",
                alpha=0.9,
            ),
            plt.Line2D(
                [0],
                [0],
                color="blue",
                linewidth=3,
                label="Goldbach distance circles",
                alpha=0.8,
            ),
        ]
        ax.legend(handles=legend_elements, loc="upper left", fontsize=12)

        # Add grid
        ax.grid(True, alpha=0.3)
        ax.set_aspect("equal")

        # Save or show the plot
        if output_file:
            self.save_plot(output_file)
        else:
            filename = f"goldbach_distance_circles_{start}_{end}.png"
            self.save_plot(filename)


def plot_goldbach_distance_circles(start=2, end=30, clean_mode=True, output_file=None):
    """
    Convenience function to create a Goldbach distance circles plot.

    Args:
        start: Starting number for analysis
        end: Ending number for analysis
        clean_mode: If True, use thinner circles and no info boxes for large ranges
        output_file: Optional filename to save the plot
    """
    plotter = GoldbachDistanceCirclesPlot()
    plotter.plot(start, end, clean_mode, output_file)
