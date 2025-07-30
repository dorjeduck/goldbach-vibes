import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from goldbach.goldbach_pairs import GoldbachDecomposer
from goldbach.plots.prime_frequencies import PlotPrimeFrequencies
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Plot top N most frequent primes in Goldbach decompositions."
    )
    parser.add_argument(
        "--start", type=int, default=10, help="Start of even number range"
    )
    parser.add_argument("--end", type=int, default=100, help="End of even number range")
    parser.add_argument(
        "--top_n", type=int, default=20, help="Number of top primes to show"
    )
    args = parser.parse_args()
    decomposer = GoldbachDecomposer()
    PlotPrimeFrequencies.plot(
        decomposer, start=args.start, end=args.end, top_n=args.top_n
    )


if __name__ == "__main__":
    main()
