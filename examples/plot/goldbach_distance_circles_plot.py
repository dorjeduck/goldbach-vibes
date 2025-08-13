#!/usr/bin/env python3
"""
Generate a geometric visualization of Goldbach distances as circles.

Each number n is shown with a circle of radius d (Goldbach distance) centered at n.
The circles intersect the x-axis at n-d and n+d, which are both prime numbers.
"""

import argparse
import sys
import os

# Add the parent directory to the path to import goldbach module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from goldbach.plots.goldbach_distance_circles import plot_goldbach_distance_circles


def main():
    parser = argparse.ArgumentParser(
        description="Generate a geometric visualization of Goldbach distances as circles"
    )
    parser.add_argument(
        "--start", type=int, default=2, help="Start of the range (default: 2)"
    )
    parser.add_argument(
        "--end", type=int, default=30, help="End of the range (default: 30)"
    )
    parser.add_argument(
        "--output", type=str, help="Output filename (default: auto-generated)"
    )
    parser.add_argument(
        "--detailed",
        action="store_true",
        help="Use detailed mode (with info boxes and thicker circles) - clean mode is default",
    )

    args = parser.parse_args()

    print(
        f"Creating Goldbach distance circles plot for range [{args.start}, {args.end}]..."
    )

    plot_goldbach_distance_circles(
        start=args.start,
        end=args.end,
        output_file=args.output,
        clean_mode=not args.detailed,
    )

    if args.output:
        print(f"Plot saved to imgs/{args.output}")
    else:
        filename = f"goldbach_distance_circles_{args.start}_{args.end}.png"
        print(f"Plot saved to imgs/{filename}")


if __name__ == "__main__":
    main()
