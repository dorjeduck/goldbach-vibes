import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from goldbach.decomposer import GoldbachDecomposer
from goldbach.plots.distance_boxplots import PlotDistanceBoxplots
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Boxplot of Goldbach decomposition distances."
    )
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
    args = parser.parse_args()
    decomposer = GoldbachDecomposer()
    PlotDistanceBoxplots.plot(
        decomposer,
        start=args.start,
        end=args.end,
        normalize=args.normalize,
        showfliers=args.showfliers,
    )


if __name__ == "__main__":
    main()
