"""
Plot prime gaps for Goldbach pairs.
"""

from .utils import get_marker_size
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

def plot_goldbach_pair_prime_gaps(goldbach_pairs, start=4, end=100, output=None):
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
    marker_size = get_marker_size(len(evens))

    plt.figure(figsize=(12, 6))
    plt.scatter(xs, ys, s=marker_size**2, alpha=0.6, color="blue")
    plt.xlabel("Even Number")
    plt.ylabel("Prime Gaps (q - p)")
    plt.title(f"Prime Gaps in Goldbach Pairs for Even Numbers in [{start},{end}]")
    plt.grid(True, alpha=0.3)
    # Add a larger margin to the x-axis, but only label a subset of even numbers for readability
    margin = (max(evens) - min(evens)) * 0.02
    plt.xlim(min(evens) - margin, max(evens) + margin)
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
    plt.tight_layout()
    if output:
        plt.savefig(output)
    else:
        plt.show()
