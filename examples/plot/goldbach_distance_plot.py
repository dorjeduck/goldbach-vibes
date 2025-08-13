#!/usr/bin/env python3
"""
Plot Goldbach distances for a range of numbers.

The Goldbach distance for a number n is defined as the smallest prime gap
among all Goldbach pairs of 2*n, divided by 2.
"""

import sys
import os
import argparse

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from goldbach import GoldbachPairs
from goldbach.plots.goldbach_distance import plot_goldbach_distance


def main():
    parser = argparse.ArgumentParser(
        description="Plot Goldbach distances for a range of numbers"
    )
    parser.add_argument(
        "--start", type=int, default=3, help="Start of number range (default: 3)"
    )
    parser.add_argument(
        "--end", type=int, default=50, help="End of number range (default: 50)"
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Output file to save the plot (e.g. imgs/goldbach_distance_plot.png)",
    )

    args = parser.parse_args()

    print(f"Creating Goldbach distance plot for range [{args.start}, {args.end}]...")

    goldbach_pairs = GoldbachPairs()

    # Generate filename if output not specified
    output_path = args.output
    if not output_path:
        output_path = f"imgs/goldbach_distance_{args.start}_{args.end}.png"

        # Create imgs directory if it doesn't exist
        os.makedirs("imgs", exist_ok=True)

    plot_goldbach_distance(
        goldbach_pairs,
        start=args.start,
        end=args.end,
        output=output_path,
    )


if __name__ == "__main__":
    main()
