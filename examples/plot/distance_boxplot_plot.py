import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from goldbach.goldbach_pairs import GoldbachPairs
from goldbach.plots.distance_boxplots import plot_distance_boxplots
import argparse


def main():
    parser = argparse.ArgumentParser(description="Boxplot of Goldbach pair gaps.")
    parser.add_argument(
        "--start", type=int, default=10, help="Start of even number range"
    )
    parser.add_argument("--end", type=int, default=100, help="End of even number range")
    parser.add_argument(
        "--normalize", action="store_true", help="Normalize distances by n"
    )
    parser.add_argument(
        "--showfliers", action="store_true", help="Show outliers in boxplot"
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Output file to save the plot (e.g. imgs/plot.png)",
    )
    args = parser.parse_args()
    goldbach_pairs = GoldbachPairs()
    plot_distance_boxplots(
        goldbach_pairs,
        start=args.start,
        end=args.end,
        normalize=args.normalize,
        showfliers=args.showfliers,
        output=args.output,
    )


if __name__ == "__main__":
    main()
