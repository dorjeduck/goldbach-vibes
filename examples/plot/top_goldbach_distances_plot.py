#!/usr/bin/env python3
"""
Generate a bar plot showing the top N numbers with largest Goldbach distances.

The Goldbach distance for a number n is defined as the smallest prime gap
among all Goldbach pairs of 2*n, divided by 2.
"""

import argparse
import sys
import os

# Add the parent directory to the path to import goldbach module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from goldbach.plots.top_goldbach_distances import plot_top_goldbach_distances


def main():
    parser = argparse.ArgumentParser(
        description="Generate a bar plot of top N largest Goldbach distances"
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
        "--output", type=str, help="Output filename (default: auto-generated)"
    )

    args = parser.parse_args()

    print(
        f"Creating top {args.top} Goldbach distances plot for range [{args.start}, {args.end}]..."
    )

    plot_top_goldbach_distances(
        start=args.start, end=args.end, top_n=args.top, output_file=args.output
    )

    if args.output:
        print(f"Plot saved to imgs/{args.output}")
    else:
        filename = f"top_goldbach_distances_{args.start}_{args.end}_top{args.top}.png"
        print(f"Plot saved to imgs/{filename}")


if __name__ == "__main__":
    main()
