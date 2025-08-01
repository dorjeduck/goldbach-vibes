#!/usr/bin/env python3
"""
Print the number of Goldbach pairs made from twin primes for each even number in a range.

Twin primes are primes that are part of twin prime pairs (p, p+2).
This analysis shows how many Goldbach pairs can be formed using only these special primes.
"""

import argparse
import sys
import os

# Add the parent directory to the path to import goldbach module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from goldbach.goldbach_pairs import GoldbachPairs


def main():
    parser = argparse.ArgumentParser(
        description="Print Goldbach pairs made from twin primes"
    )
    parser.add_argument(
        "--start", type=int, default=6, help="Start of the range (default: 6)"
    )
    parser.add_argument(
        "--end", type=int, default=50, help="End of the range (default: 50)"
    )
    parser.add_argument(
        "--show-details",
        action="store_true",
        help="Show the actual twin prime pairs used",
    )

    args = parser.parse_args()

    if args.start % 2 != 0:
        args.start += 1  # Ensure start is even
    if args.end % 2 != 0:
        args.end -= 1  # Ensure end is even

    print(f"Twin Prime Goldbach Pairs Analysis")
    print(f"Range: [{args.start}, {args.end}]")
    print("=" * 50)

    goldbach_pairs = GoldbachPairs()

    # Get the set of twin primes for reference
    twin_primes = goldbach_pairs.get_twin_primes_set(args.end)
    print(f"Twin primes up to {args.end}: {sorted(twin_primes)}")
    print("-" * 50)

    total_pairs = 0
    total_twin_prime_pairs = 0

    for n in range(args.start, args.end + 1, 2):
        all_pairs = goldbach_pairs.get(n)
        twin_prime_count = goldbach_pairs.count_twin_prime_goldbach_pairs(n)

        print(f"{n:3}: {twin_prime_count}/{len(all_pairs)} twin prime pairs")

        total_pairs += len(all_pairs)
        total_twin_prime_pairs += twin_prime_count

        if args.show_details and twin_prime_count > 0:
            # Show which twin prime pairs are used
            twin_pairs = []
            for p in sorted(twin_primes):
                q = n - p
                if q >= p and q in twin_primes:
                    twin_pairs.append((p, q))
            print(f"    Twin prime pairs: {twin_pairs}")

    print("-" * 50)
    percentage = (total_twin_prime_pairs / total_pairs * 100) if total_pairs > 0 else 0
    print(
        f"Total: {total_twin_prime_pairs}/{total_pairs} ({percentage:.1f}%) are twin prime pairs"
    )


if __name__ == "__main__":
    main()
