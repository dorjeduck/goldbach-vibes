#!/usr/bin/env python3
"""
Print the top N numbers with the largest Goldbach distances in a range.

The Goldbach distance for a number n is defined as the smallest prime gap
among all Goldbach pairs of 2*n, divided by 2. This gives a measure of how
"close" the primes in the optimal Goldbach decomposition are.
"""

import argparse
import sys
import os

# Add the parent directory to the path to import goldbach module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from goldbach.goldbach_pairs import GoldbachPairs


def main():
    parser = argparse.ArgumentParser(
        description="Print the top N numbers with largest Goldbach distances"
    )
    parser.add_argument(
        "--start", type=int, default=3, help="Start of the range (default: 3)"
    )
    parser.add_argument(
        "--end", type=int, default=100, help="End of the range (default: 100)"
    )
    parser.add_argument(
        "--top",
        type=int,
        default=10,
        help="Number of top results to show (default: 10)",
    )
    parser.add_argument(
        "--show-details",
        action="store_true",
        help="Show Goldbach pairs and gaps for top results",
    )

    args = parser.parse_args()

    goldbach_pairs = GoldbachPairs()

    print(f"Top {args.top} Goldbach Distances in range [{args.start}, {args.end}]:")
    print("=" * 70)

    top_distances = goldbach_pairs.top_goldbach_distances(
        args.start, args.end, args.top
    )

    if not top_distances:
        print("No valid Goldbach distances found in the given range.")
        return

    # Group by distance for better display
    current_distance = None
    rank = 1

    for i, (n, distance) in enumerate(top_distances):
        if distance != current_distance:
            current_distance = distance
            if i > 0:
                print()  # Add spacing between different distance groups

        print(f"#{rank:2d}: n={n:3d}, distance={distance:2d}")

        if args.show_details:
            even_n = 2 * n
            pairs = goldbach_pairs.get(even_n)
            gaps = goldbach_pairs.prime_gaps(even_n)
            smallest_gap = goldbach_pairs.smallest_prime_gap(even_n)
            print(f"      2*n={even_n}, pairs: {pairs}")
            print(f"      gaps: {gaps}, smallest: {smallest_gap}")

        # Update rank only when distance changes
        if i + 1 < len(top_distances) and top_distances[i + 1][1] != distance:
            rank = i + 2

    print()
    print(f"Summary: Found {len(top_distances)} numbers in top {args.top} positions")
    if len(top_distances) > args.top:
        print(
            f"Note: {len(top_distances) - args.top} additional numbers tied for position {args.top}"
        )


if __name__ == "__main__":
    main()
