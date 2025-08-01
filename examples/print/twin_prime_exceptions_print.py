#!/usr/bin/env python3
"""
Find even numbers that cannot be expressed as the sum of two twin primes.

According to mathematical research, there are exactly 35 such exceptions,
with the largest being 4208. This script searches for and lists these exceptions.
"""

import argparse
import sys
import os

# Add the parent directory to the path to import goldbach module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from goldbach.goldbach_pairs import GoldbachPairs


def main():
    parser = argparse.ArgumentParser(
        description="Find even numbers with no twin prime Goldbach pairs"
    )
    parser.add_argument(
        "--start", type=int, default=4, help="Start of the range (default: 4)"
    )
    parser.add_argument(
        "--end", type=int, default=5000, help="End of the range (default: 5000)"
    )

    args = parser.parse_args()

    if args.start % 2 != 0:
        args.start += 1  # Ensure start is even
    if args.end % 2 != 0:
        args.end -= 1  # Ensure end is even

    goldbach_pairs = GoldbachPairs()

    # Find all exceptions
    exceptions = []
    total_checked = 0

    for n in range(args.start, args.end + 1, 2):
        total_checked += 1
        twin_prime_count = goldbach_pairs.count_twin_prime_goldbach_pairs(n)

        if twin_prime_count == 0:
            exceptions.append(n)

    print(f"Twin Prime Goldbach Exceptions for range [{args.start}, {args.end}]:")
    print()
    print(f"Exceptions found (#{len(exceptions)}): {exceptions}")


if __name__ == "__main__":
    main()
