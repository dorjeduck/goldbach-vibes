import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from goldbach import GoldbachPairs
from goldbach.plots.prime_frequencies import plot_prime_frequencies
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
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Output file to save the plot (e.g. imgs/plot.png)",
    )
    args = parser.parse_args()
    goldbach_pairs = GoldbachPairs()
    plot_prime_frequencies(
        goldbach_pairs,
        start=args.start,
        end=args.end,
        top_n=args.top_n,
        output=args.output,
    )


if __name__ == "__main__":
    main()
