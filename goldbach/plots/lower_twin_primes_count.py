"""
Plot the number of lower twin primes in Goldbach pairs for each even number in a given range.
"""

import matplotlib.pyplot as plt


def plot_lower_twin_primes_count(goldbach_pairs, start=4, end=100, output=None):
    """
    For each even number in [start, end], plot the number of Goldbach pairs whose lower prime is a lower twin prime.
    """
    evens = list(range(start, end + 1, 2))
    counts = [goldbach_pairs.count_pairs_with_lower_twin_prime(n) for n in evens]
    plt.figure(figsize=(12, 6))
    plt.bar(evens, counts, color="teal")
    # Only label even numbers for orientation
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
    plt.ylabel("Number of Goldbach Pairs with Lower Twin Prime")
    plt.title(
        f"Number of Goldbach Pairs with Lower Twin Prime for Even Numbers in [{start},{end}]"
    )
    plt.grid(True, axis="y", alpha=0.3)
    plt.tight_layout()
    if output:
        plt.savefig(output)
    else:
        plt.show()
