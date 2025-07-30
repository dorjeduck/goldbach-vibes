import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from goldbach.decomposer import GoldbachDecomposer
from goldbach.plots.decomposition_distances import PlotDecompositionDistances
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Plot Goldbach decomposition distances."
    )
    parser.add_argument(
        "--start", type=int, default=10, help="Start of even number range"
    )
    parser.add_argument("--end", type=int, default=100, help="End of even number range")
    args = parser.parse_args()
    decomposer = GoldbachDecomposer()
    PlotDecompositionDistances.plot(decomposer, start=args.start, end=args.end)


if __name__ == "__main__":
    main()
