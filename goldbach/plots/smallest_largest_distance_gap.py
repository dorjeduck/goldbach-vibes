"""
Plot distance between smallest and largest p in Goldbach decompositions.
"""

from .utils import get_marker_size
import matplotlib.pyplot as plt



def plot_smallest_largest_distance_gap(goldbach_pairs, start=4, end=100, output=None):
    """
    For each even number in [start, end], plot the distance between the smallest and largest p in the decompositions.
    """
    xs = []
    ys = []
    for even_n in range(start, end + 1, 2):
        decomps = goldbach_pairs.goldbach_pairs(even_n)
        if decomps:
            xs.append(even_n)
            ys.append(decomps[-1][1] - decomps[0][0])
    plt.figure(figsize=(10, 5))
    plt.plot(xs, ys, marker="o", linestyle="", color="green")
    plt.xlabel("Even Number")
    plt.ylabel("Largest - Smallest Prime in Goldbach Pair")
    plt.title(f"Smallest-Largest Goldbach Pair Distance in [{start},{end}]")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    if output:
        plt.savefig(output)
    else:
        plt.show()
