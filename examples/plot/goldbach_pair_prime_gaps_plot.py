import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from goldbach.goldbach_pairs import GoldbachPairs
from goldbach.plots.goldbach_pair_prime_gaps import PlotGoldbachPrimeGaps
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Plot Goldbach decomposition distances."
    )
    parser.add_argument(
        "--start", type=int, default=10, help="Start of even number range"
    )
    parser.add_argument("--end", type=int, default=100, help="End of even number range")
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Output file to save the plot (e.g. imgs/plot.png)",
    )
    args = parser.parse_args()
    decomposer = GoldbachPairs()
    PlotGoldbachPrimeGaps.plot(
        decomposer, start=args.start, end=args.end, output=args.output
    )


if __name__ == "__main__":
    main()
