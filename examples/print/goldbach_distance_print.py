#!/usr/bin/env python3
"""
Print Goldbach distances for a range of numbers.

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
        description="Print Goldbach distances for a range of numbers"
    )
    parser.add_argument(
        "--start", type=int, default=3, help="Start of the range (default: 3)"
    )
    parser.add_argument(
        "--end", type=int, default=25, help="End of the range (default: 25)"
    )
    parser.add_argument(
        "--show-details", action="store_true", help="Show Goldbach pairs and gaps"
    )

    args = parser.parse_args()

    goldbach_pairs = GoldbachPairs()

    print(f"Goldbach Distances for range [{args.start}, {args.end}]:")
    print("=" * 60)

    if args.show_details:
        print("(Distance = smallest_prime_gap(2*n) / 2)")
        print()

    valid_count = 0
    max_distance = -1
    max_distance_numbers = []

    for n in range(args.start, args.end + 1):
        distance = goldbach_pairs.goldbach_distance(n)
        even_n = 2 * n

        if distance >= 0:
            valid_count += 1

            # Track maximum distance
            if distance > max_distance:
                max_distance = distance
                max_distance_numbers = [n]
            elif distance == max_distance:
                max_distance_numbers.append(n)

            if args.show_details:
                pairs = goldbach_pairs.get(even_n)
                gaps = goldbach_pairs.prime_gaps(even_n)
                smallest_gap = goldbach_pairs.smallest_prime_gap(even_n)
                print(f"n={n} (2*n={even_n}): distance={distance}")
                print(f"  Pairs: {pairs}")
                print(f"  Gaps: {gaps}, smallest: {smallest_gap}")
                print()
            else:
                print(f"n={n}: distance={distance}")
        else:
            if args.show_details:
                print(f"n={n} (2*n={even_n}): No Goldbach pairs found")

    print()
    print(f"Summary: {valid_count} numbers with valid Goldbach distances")

    if max_distance >= 0:
        if len(max_distance_numbers) == 1:
            print(
                f"Maximum distance: {max_distance} (achieved by n={max_distance_numbers[0]})"
            )
        else:
            numbers_str = ", ".join(map(str, max_distance_numbers))
            print(f"Maximum distance: {max_distance} (achieved by n={numbers_str})")


if __name__ == "__main__":
    main()
