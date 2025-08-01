#!/usr/bin/env python3
"""
Plot the density of critical even numbers across subranges.

Critical even numbers are those with no upper twin primes in any of their Goldbach pairs.
This script analyzes their distribution across different subranges.
"""

import argparse
import sys
import os

# Add the parent directory to the path to import goldbach module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from goldbach.goldbach_pairs import GoldbachPairs
from goldbach.plots.critical_density import plot_critical_density


def main():
    parser = argparse.ArgumentParser(
        description="Plot density of critical even numbers across subranges"
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
        "--output",
        type=str,
        help="Output file path (if not provided, displays the plot)",
    )

    args = parser.parse_args()

    if args.start % 2 != 0:
        args.start += 1  # Ensure start is even
    if args.end % 2 != 0:
        args.end -= 1  # Ensure end is even

    print(f"Analyzing critical even numbers density from {args.start} to {args.end}")
    print(f"Subrange size: {args.subrange_size}")

    goldbach_pairs = GoldbachPairs()

    # Generate and display the plot
    density_data = plot_critical_density(
        goldbach_pairs,
        start=args.start,
        end=args.end,
        subrange_size=args.subrange_size,
        output=args.output,
    )

    # Print summary statistics
    total_critical = sum(critical_count for _, _, critical_count, _ in density_data)
    total_evens = sum(total_evens for _, _, _, total_evens in density_data)
    overall_density = (total_critical / total_evens * 100) if total_evens > 0 else 0

    print(f"\nSummary:")
    print(f"Total critical even numbers: {total_critical}")
    print(f"Total even numbers analyzed: {total_evens}")
    print(f"Overall density: {overall_density:.2f}%")

    print(f"\nSubrange breakdown:")
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
            f"[{subrange_start}, {subrange_end}]: {critical_count}/{total_evens_subrange} ({density_pct:.1f}%)"
        )


if __name__ == "__main__":
    main()
