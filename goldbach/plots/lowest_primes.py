"""
Plot lowest primes in Goldbach decompositions.
"""

from .utils import get_marker_size
import matplotlib.pyplot as plt


def plot_lowest_primes(goldbach_pairs, start=4, end=100, output=None):
    """
    For each even number in [start, end], plot only the lowest prime in the set of Goldbach pairs.

    """

    xs_small = []
    ys_small = []
    for even_n in range(start, end + 1, 2):
        pairs = goldbach_pairs.get(even_n)
        if pairs:
            xs_small.append(even_n)
            ys_small.append(pairs[0][0])

    n_points = len(xs_small)
    marker_size = get_marker_size(n_points) ** 2
    plt.figure(figsize=(12, 6))
    plt.scatter(
        xs_small,
        ys_small,
        s=marker_size,
        color="blue",
        alpha=0.8,
        label="Smallest Prime",
    )

    plt.xlabel("Even Number")
    plt.ylabel("Prime Number")
    plt.title(f"Smallest Primes in Goldbach Pairs [{start},{end}]")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    if output:
        plt.savefig(output)
    else:
        plt.show()
