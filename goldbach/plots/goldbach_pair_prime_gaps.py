"""
Plot prime gaps for Goldbach pairs.
"""

from .utils import get_marker_size
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker


def plot_goldbach_pair_prime_gaps(
    goldbach_pairs, start=4, end=100, gap_mode="all", output=None
):
    """
    For each even number in [start, end], plot prime gaps (q - p) for Goldbach pairs as a scatter plot.
    X-axis: even number, Y-axis: q - p for each Goldbach pair.
    Marker size is chosen based on the number of points.

    Args:
        goldbach_pairs: GoldbachPairs instance
        start: Starting even number
        end: Ending even number
        gap_mode: "all" for all gaps, "smallest" for smallest gap only, "largest" for largest gap only
        output: Path to save the plot (optional)
    """

    xs = []
    ys = []
    for even_n in range(start, end + 1, 2):
        if gap_mode == "all":
            gaps = goldbach_pairs.prime_gaps(even_n)
            for gap in gaps:
                xs.append(even_n)
                ys.append(gap)
        elif gap_mode == "smallest":
            gap = goldbach_pairs.smallest_prime_gap(even_n)
            if gap is not None:
                xs.append(even_n)
                ys.append(gap)
        elif gap_mode == "largest":
            gap = goldbach_pairs.largest_prime_gap(even_n)
            if gap is not None:
                xs.append(even_n)
                ys.append(gap)
        else:
            raise ValueError("gap_mode must be 'all', 'smallest', or 'largest'")

    evens = list(range(start, end + 1, 2))
    marker_size = get_marker_size(len(evens))

    plt.figure(figsize=(12, 6))

    if gap_mode == "all":
        plt.scatter(xs, ys, s=marker_size**2, alpha=0.6, color="blue")
        title_suffix = "All Gaps"
    elif gap_mode == "smallest":
        plt.scatter(xs, ys, s=marker_size**2, alpha=0.8, color="green")
        title_suffix = "Smallest Gaps Only"
    else:  # largest
        plt.scatter(xs, ys, s=marker_size**2, alpha=0.8, color="red")
        title_suffix = "Largest Gaps Only"

    plt.xlabel("Even Number")
    plt.ylabel("Prime Gaps (q - p)")
    plt.title(
        f"Prime Gaps in Goldbach Pairs ({title_suffix}) for Even Numbers in [{start},{end}]"
    )
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
