"""
Plot lowest primes in Goldbach decompositions.
"""

from .utils import get_marker_size
import matplotlib.pyplot as plt


def plot_largest_lowest_prime_so_far(goldbach_pairs, start=4, end=100, output=None):
    """
    For each even number in [start, end], plot only the lowest prime in the set of Goldbach pairs.

    """

    xs_small = []
    ys_max_so_far = []
    max_prime = None
    for even_n in range(start, end + 1, 2):
        pairs = goldbach_pairs.get(even_n)
        if pairs:
            xs_small.append(even_n)

            if max_prime is None or pairs[0][0] > max_prime:
                max_prime = pairs[0][0]
            ys_max_so_far.append(max_prime)

    n_points = len(xs_small)
    marker_size = get_marker_size(n_points) ** 2
    plt.figure(figsize=(12, 6))
    plt.scatter(
        xs_small,
        ys_max_so_far,
        s=marker_size,
        color="blue",
        alpha=0.8,
        label="Smallest Prime",
    )

    plt.xlabel("Even Number")
    plt.ylabel("Prime Number")
    plt.title(f"Larges lowest prime in Goldbach Pairs [{start},{end}]")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    if output:
        plt.savefig(output)
    else:
        plt.show()
