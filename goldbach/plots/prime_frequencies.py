"""
Plot the top N most frequent primes in Goldbach decompositions.
"""

from .utils import get_marker_size
import matplotlib.pyplot as plt
from collections import Counter


def plot_prime_frequencies(goldbach_pairs, start=4, end=100, top_n=30, output=None):
    """
    For all even numbers in [start, end], count how often each prime appears in any Goldbach decomposition.
    Plot the top_n most frequent primes as a bar chart.
    """

    prime_counter = Counter()
    for even_n in range(start, end + 1, 2):
        gpairs = goldbach_pairs.get(even_n)
        for p, q in gpairs:
            if p <= end:
                prime_counter[p] += 1
            if q <= end:
                prime_counter[q] += 1
    # Only keep primes <= end
    filtered = [(prime, freq) for prime, freq in prime_counter.items() if prime <= end]
    filtered.sort(key=lambda x: x[1], reverse=True)
    most_common = filtered[:top_n]
    primes, freqs = zip(*most_common) if most_common else ([], [])
    plt.figure(figsize=(12, 6))
    plt.bar(primes, freqs, color="purple")
    plt.xlabel("Prime")
    plt.ylabel("Frequency in Goldbach Pairs")
    plt.title(f"Top {top_n} Most Frequent Primes in Goldbach Pairs for [{start},{end}]")
    plt.tight_layout()
    if output:
        plt.savefig(output)
    else:
        plt.show()
