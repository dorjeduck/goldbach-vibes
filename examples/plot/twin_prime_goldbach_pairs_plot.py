#!/usr/bin/env python3
"""
Plot the number of Goldbach pairs made from twin primes for each even number in a range.

Twin primes are primes that are part of twin prime pairs (p, p+2).
This analysis shows how many Goldbach pairs can be formed using only these special primes.
"""

import argparse
import sys
import os

# Add the parent directory to the path to import goldbach module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from goldbach.goldbach_pairs import GoldbachPairs
from goldbach.plots.twin_prime_goldbach_pairs import plot_twin_prime_goldbach_pairs


def main():
    parser = argparse.ArgumentParser(
        description="Plot Goldbach pairs made from twin primes"
    )
    parser.add_argument(
        "--start", type=int, default=6, help="Start of the range (default: 6)"
    )
    parser.add_argument(
        "--end", type=int, default=100, help="End of the range (default: 100)"
    )
    parser.add_argument(
        "--output",
        type=str,
        help="Output file path (if not provided, displays the plot)",
    )

    args = parser.parse_args()

    if args.start % 2 != 0:
        args.start += 1  # Ensure start is even
    if args.end % 2 != 0:
        args.end -= 1  # Ensure end is even

    print(f"Analyzing twin prime Goldbach pairs from {args.start} to {args.end}")

    goldbach_pairs = GoldbachPairs()

    # Generate and display the plot
    plot_twin_prime_goldbach_pairs(
        goldbach_pairs, start=args.start, end=args.end, output=args.output
    )

    # Print some examples
    print(f"\nExamples:")
    for n in range(args.start, min(args.start + 10, args.end + 1), 2):
        count = goldbach_pairs.count_twin_prime_goldbach_pairs(n)
        print(f"{n}: {count} twin prime Goldbach pairs")


if __name__ == "__main__":
    main()
