"""
Plot the number of Goldbach pairs for each even number.
"""

from .utils import get_marker_size
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

def plot_goldbach_pair_counts(goldbach_pairs, start=4, end=100, output=None):
    """
    Plot the number of Goldbach pairs for each even number in [start, end].
    """
    evens = list(range(start, end + 1, 2))
    counts = [len(goldbach_pairs.goldbach_pairs(n)) for n in evens]
    marker_size = get_marker_size(len(evens))
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
    # Add a larger margin to the x-axis, but only label a subset of even numbers for readability
    margin = (max(evens) - min(evens)) * 0.02
    left = min(evens) - margin
    right = max(evens) + margin
    plt.xlim(left, right)
    ax = plt.gca()
    # Choose a step so that at most 20 ticks are shown
    max_ticks = 20
    step = max(2, 2 * ((len(evens) - 1) // (max_ticks - 1) + 1))
    ticks = [e for i, e in enumerate(evens) if i % (step // 2) == 0]
    if evens[-1] not in ticks:
        ticks.append(evens[-1])
    ax.xaxis.set_major_locator(mticker.FixedLocator(ticks))
    ax.xaxis.set_minor_locator(mticker.NullLocator())
    ax.set_xticklabels([str(e) for e in ticks], rotation=0)
    ax.yaxis.set_major_locator(mticker.MaxNLocator(integer=True))
    plt.tight_layout()
    if output:
        plt.savefig(output)
    else:
        plt.show()
