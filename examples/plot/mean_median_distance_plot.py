import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from goldbach import GoldbachPairs
from goldbach.plots.mean_median_distances import plot_mean_median_distances
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Plot mean/median Goldbach decomposition distances."
    )
    parser.add_argument(
        "--start", type=int, default=10, help="Start of even number range"
    )
    parser.add_argument("--end", type=int, default=100, help="End of even number range")
    parser.add_argument(
        "--normalize", action="store_true", help="Normalize distances by n"
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Output file to save the plot (e.g. imgs/plot.png)",
    )
    args = parser.parse_args()
    goldbach_pairs = GoldbachPairs()
    plot_mean_median_distances(
        goldbach_pairs,
        start=args.start,
        end=args.end,
        normalize=args.normalize,
        output=args.output,
    )


if __name__ == "__main__":
    main()
