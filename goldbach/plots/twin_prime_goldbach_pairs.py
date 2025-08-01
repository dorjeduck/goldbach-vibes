"""
Plot the number of Goldbach pairs made from twin primes for each even number in a given range.
"""

import matplotlib.pyplot as plt
from goldbach.plots.utils import get_marker_size


def plot_twin_prime_goldbach_pairs(goldbach_pairs, start=4, end=100, output=None):
    """
    For each even number in [start, end], plot the number of Goldbach pairs where both primes
    are from the set of twin primes.
    """
    evens = list(range(start, end + 1, 2))
    counts = [goldbach_pairs.count_twin_prime_goldbach_pairs(n) for n in evens]

    plt.figure(figsize=(12, 6))
    plt.bar(evens, counts, color="purple", alpha=0.7)

    # Set x-axis ticks
    if end - start <= 50:
        plt.xticks(evens, [str(e) for e in evens], rotation=0)
    else:
        n = len(evens)
        step = max(2, 2 * ((n - 1) // 10 + 1))
        idxs = set(range(0, n, step // 2))
        idxs.add(0)
        idxs.add(n - 1)
        ticks = [evens[i] for i in sorted(idxs)]
        labels = [str(evens[i]) for i in sorted(idxs)]
        plt.xticks(ticks, labels, rotation=0)

    plt.xlabel("Even Number")
    plt.ylabel("Number of Twin Prime Goldbach Pairs")
    plt.title(f"Goldbach Pairs from Twin Primes for Even Numbers in [{start},{end}]")

    # Force integer ticks on y-axis
    max_count = max(counts) if counts else 0
    if max_count > 0:
        plt.yticks(range(0, max_count + 1))

    plt.grid(True, axis="y", alpha=0.3)
    plt.tight_layout()

    if output:
        plt.savefig(output, dpi=150, bbox_inches="tight")
        print(f"Plot saved to {output}")
    else:
        plt.show()

    plt.close()
