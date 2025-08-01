#!/usr/bin/env python3
"""
Print the density of critical even numbers across subranges.

Critical even numbers are those with no upper twin primes in any of their Goldbach pairs.
This script analyzes their distribution across different subranges.
"""

import argparse
import sys
import os

# Add the parent directory to the path to import goldbach module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from goldbach.goldbach_pairs import GoldbachPairs


def main():
    parser = argparse.ArgumentParser(
        description="Print density of critical even numbers across subranges"
    )
    parser.add_argument(
        "--start", type=int, default=6, help="Start of the range (default: 6)"
    )
    parser.add_argument(
        "--end", type=int, default=1000, help="End of the range (default: 1000)"
    )
    parser.add_argument(
        "--subrange-size",
        type=int,
        default=100,
        help="Size of each subrange (default: 100)",
    )
    parser.add_argument(
        "--show-numbers", action="store_true", help="Show the actual critical numbers"
    )

    args = parser.parse_args()

    if args.start % 2 != 0:
        args.start += 1  # Ensure start is even
    if args.end % 2 != 0:
        args.end -= 1  # Ensure end is even

    print(f"Critical Even Numbers Density Analysis")
    print(f"Range: [{args.start}, {args.end}]")
    print(f"Subrange size: {args.subrange_size}")
    print("=" * 60)

    goldbach_pairs = GoldbachPairs()

    # Get density data
    density_data = goldbach_pairs.critical_density_by_subrange(
        args.start, args.end, args.subrange_size
    )

    # Print subrange breakdown
    print(f"{'Subrange':<20} {'Critical':<10} {'Total':<8} {'Density':<10}")
    print("-" * 50)

    total_critical = 0
    total_evens = 0

    for (
        subrange_start,
        subrange_end,
        critical_count,
        total_evens_subrange,
    ) in density_data:
        density_pct = (
            (critical_count / total_evens_subrange * 100)
            if total_evens_subrange > 0
            else 0
        )
        print(
            f"[{subrange_start:4}, {subrange_end:4}]        {critical_count:<10} {total_evens_subrange:<8} {density_pct:6.1f}%"
        )

        total_critical += critical_count
        total_evens += total_evens_subrange

        # Show actual critical numbers if requested
        if args.show_numbers and critical_count > 0:
            critical_numbers = goldbach_pairs.get_critical_even_numbers(
                subrange_start, subrange_end
            )
            print(f"    Critical numbers: {critical_numbers}")

    print("-" * 50)
    overall_density = (total_critical / total_evens * 100) if total_evens > 0 else 0
    print(
        f"{'Total':<20} {total_critical:<10} {total_evens:<8} {overall_density:6.1f}%"
    )

    print(f"\nSummary:")
    print(f"Total critical even numbers: {total_critical}")
    print(f"Total even numbers analyzed: {total_evens}")
    print(f"Overall density: {overall_density:.2f}%")


if __name__ == "__main__":
    main()
