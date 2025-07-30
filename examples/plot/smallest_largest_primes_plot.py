import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from goldbach.goldbach_pairs import GoldbachDecomposer
from goldbach.plots.smallest_largest_primes import PlotSmallestLargestPrimes
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Plot smallest and largest primes in Goldbach decompositions."
    )
    parser.add_argument(
        "--start", type=int, default=10, help="Start of even number range"
    )
    parser.add_argument("--end", type=int, default=100, help="End of even number range")
    args = parser.parse_args()
    decomposer = GoldbachDecomposer()
    PlotSmallestLargestPrimes.plot(decomposer, start=args.start, end=args.end)


if __name__ == "__main__":
    main()
