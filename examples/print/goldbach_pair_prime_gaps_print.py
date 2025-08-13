#!/usr/bin/env python3
"""
Print Goldbach pair prime gaps with different modes.

This script demonstrates the smallest, largest, or all prime gaps
for Goldbach pairs of even numbers in a given range.
"""

import argparse
import sys
import os

# Add the parent directory to the path to import goldbach module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from goldbach.goldbach_pairs import GoldbachPairs


def main():
    parser = argparse.ArgumentParser(description="Print Goldbach pair prime gaps")
    parser.add_argument(
        "--start", type=int, default=6, help="Start of the range (default: 6)"
    )
    parser.add_argument(
        "--end", type=int, default=30, help="End of the range (default: 30)"
    )
    parser.add_argument(
        "--gap-mode",
        type=str,
        default="all",
        choices=["all", "smallest", "largest"],
        help="Which gaps to show: 'all' (default), 'smallest', or 'largest'",
    )

    args = parser.parse_args()

    if args.start % 2 != 0:
        args.start += 1  # Ensure start is even
    if args.end % 2 != 0:
        args.end -= 1  # Ensure end is even

    goldbach_pairs = GoldbachPairs()

    print(
        f"Goldbach Pair Prime Gaps ({args.gap_mode.title()}) for range [{args.start}, {args.end}]:"
    )
    print("=" * 60)

    for n in range(args.start, args.end + 1, 2):
        pairs = goldbach_pairs.get(n)

        if args.gap_mode == "all":
            gaps = goldbach_pairs.prime_gaps(n)
            print(f"{n}: pairs={pairs}, gaps={gaps}")
        elif args.gap_mode == "smallest":
            gap = goldbach_pairs.smallest_prime_gap(n)
            print(f"{n}: smallest_gap={gap}")
        elif args.gap_mode == "largest":
            gap = goldbach_pairs.largest_prime_gap(n)
            print(f"{n}: largest_gap={gap}")


if __name__ == "__main__":
    main()
