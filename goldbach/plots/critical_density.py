"""
Critical Even Numbers Density Plot

Plots the density of critical even numbers (those with no upper twin primes in their Goldbach pairs)
across different subranges to study their distribution.
"""

import matplotlib.pyplot as plt
import numpy as np

from goldbach.plots.utils import get_marker_size


def set_x_ticks(ax, x_values):
    """Set a reasonable number of x-axis ticks to avoid overlapping."""
    n = len(x_values)

    # Aim for at most 8-10 ticks regardless of data size
    if n <= 8:
        step = 1
    elif n <= 20:
        step = max(1, n // 8)
    elif n <= 50:
        step = max(1, n // 6)
    else:
        step = max(1, n // 8)

    idxs = set(range(0, n, step))
    idxs.add(0)
    idxs.add(n - 1)

    ticks = [x_values[i] for i in sorted(idxs)]
    ax.set_xticks(ticks)
    # Rotate labels for better readability when there are many ticks
    if len(ticks) > 6:
        ax.tick_params(axis="x", rotation=45)


def plot_critical_density(
    goldbach_pairs, start=6, end=1000, subrange_size=100, output=None
):
    """
    Plot the density of critical even numbers across subranges.

    Args:
        goldbach_pairs: GoldbachPairs instance
        start: Starting even number for analysis
        end: Ending even number for analysis
        subrange_size: Size of each subrange (default: 100)
        output: Path to save the plot (optional)
    """
    # Get density data
    density_data = goldbach_pairs.critical_density_by_subrange(
        start, end, subrange_size
    )

    # Extract data for plotting
    subrange_midpoints = []
    critical_counts = []

    for subrange_start, subrange_end, critical_count, total_evens in density_data:
        midpoint = (subrange_start + subrange_end) / 2

        subrange_midpoints.append(midpoint)
        critical_counts.append(critical_count)

    # Create the plot
    plt.figure(figsize=(12, 6))

    # Plot critical count as bars
    plt.bar(
        subrange_midpoints,
        critical_counts,
        alpha=0.7,
        color="red",
        width=subrange_size * 0.8,
    )
    plt.xlabel("Subrange Midpoint")
    plt.ylabel("Critical Even Numbers Count")
    plt.title(f"Critical Even Numbers Count by Subrange (size={subrange_size})")
    plt.grid(True, alpha=0.3)

    # Set reasonable number of x-axis ticks
    set_x_ticks(plt.gca(), subrange_midpoints)

    plt.tight_layout()

    if output:
        plt.savefig(output, dpi=150, bbox_inches="tight")
        print(f"Plot saved to {output}")
    else:
        plt.show()

    plt.close()

    return density_data
