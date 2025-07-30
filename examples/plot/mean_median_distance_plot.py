import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from goldbach.goldbach_pairs import GoldbachDecomposer
from goldbach.plots.mean_median_distances import PlotMeanMedianDistances
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
    args = parser.parse_args()
    decomposer = GoldbachDecomposer()
    PlotMeanMedianDistances.plot(
        decomposer, start=args.start, end=args.end, normalize=args.normalize
    )


if __name__ == "__main__":
    main()
