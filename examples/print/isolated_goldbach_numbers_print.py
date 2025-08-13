#!/usr/bin/env python3
"""
Search for isolated Goldbach numbers and demonstrate their apparent non-existence.

Isolated Goldbach numbers are even numbers where NONE of their Goldbach pairs contain any twin prime
(neither upper nor lower twin primes). This script demonstrates the remarkable mathematical finding
that such numbers appear to be non-existent in practical ranges, revealing the profound density
of twin primes among the primes.
"""

import argparse
import sys
import os

# Add the parent directory to the path to import goldbach module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from goldbach.goldbach_pairs import GoldbachPairs


def main():
    parser = argparse.ArgumentParser(
        description="Search for isolated Goldbach numbers to demonstrate their apparent non-existence"
    )
    parser.add_argument(
        "--start", type=int, default=6, help="Start of the range (default: 6)"
    )
    parser.add_argument(
        "--end", type=int, default=5000, help="End of the range (default: 5000)"
    )

    args = parser.parse_args()

    if args.start % 2 != 0:
        args.start += 1  # Ensure start is even
    if args.end % 2 != 0:
        args.end -= 1  # Ensure end is even

    print("ISOLATED GOLDBACH NUMBERS ANALYSIS")
    print("=" * 60)
    print()
    print("Definition: Isolated Goldbach numbers are even numbers where none")
    print("of their Goldbach pairs contain any twin prime (upper or lower).")
    print()
    print(f"Searching range [{args.start}, {args.end}]...")
    print()

    goldbach_pairs = GoldbachPairs()

    # Progress indicator for large ranges
    progress_step = max(1, (args.end - args.start) // 20)
    isolated_found = 0

    for n in range(args.start, args.end + 1, 2):
       
        if goldbach_pairs.is_isolated_goldbach_number(n):
            isolated_found += 1
            pairs = goldbach_pairs.get(n)
            print(f"ISOLATED NUMBER FOUND: {n} with pairs: {pairs}")

    total_evens = len(range(args.start, args.end + 1, 2))

    print()
    print("RESULTS:")
    print("=" * 60)
    print(f"Range analyzed: [{args.start}, {args.end}]")
    print(f"Total even numbers: {total_evens:,}")
    print(f"Isolated Goldbach numbers found: {isolated_found}")
    print()

    if isolated_found == 0:
        print("RESULT: No isolated Goldbach numbers found in this range.")
    else:
        print(f"Density: {isolated_found/total_evens*100:.6f}%")


if __name__ == "__main__":
    main()
