"""
Plot Goldbach distances for a range of numbers.
"""

from .utils import get_marker_size
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker


def plot_goldbach_distance(goldbach_pairs, start=3, end=50, output=None):
    """
    For each number n in [start, end], plot the Goldbach distance as a scatter plot.
    X-axis: number n, Y-axis: Goldbach distance for n.
    Marker size is chosen based on the number of points.

    Args:
        goldbach_pairs: GoldbachPairs instance
        start: Starting number
        end: Ending number
        output: Path to save the plot (optional)
    """

    xs = []
    ys = []

    for n in range(start, end + 1):
        distance = goldbach_pairs.goldbach_distance(n)
        if distance >= 0:  # Only include valid distances (not -1)
            xs.append(n)
            ys.append(distance)

    if not xs:
        print("No valid Goldbach distances found in the given range.")
        return

    numbers = list(range(start, end + 1))
    marker_size = get_marker_size(len(numbers))

    plt.figure(figsize=(12, 6))
    plt.scatter(xs, ys, s=marker_size**2, alpha=0.7, color="purple")
    plt.xlabel("Number n")
    plt.ylabel("Goldbach Distance")
    plt.title(f"Goldbach Distances for Numbers in [{start},{end}]")
    plt.grid(True, alpha=0.3)

    # Add margin to x-axis
    if len(xs) > 1:
        margin = (max(xs) - min(xs)) * 0.02
        plt.xlim(min(xs) - margin, max(xs) + margin)

    # Set reasonable number of x-axis ticks
    ax = plt.gca()
    if len(xs) > 20:
        max_ticks = 20
        step = max(1, (len(xs) - 1) // (max_ticks - 1) + 1)
        ticks = [xs[i] for i in range(0, len(xs), step)]
        if xs[-1] not in ticks:
            ticks.append(xs[-1])
        ax.xaxis.set_major_locator(mticker.FixedLocator(ticks))

    plt.tight_layout()

    if output:
        plt.savefig(output, dpi=300, bbox_inches="tight")
        print(f"Plot saved to {output}")
    else:
        plt.show()
