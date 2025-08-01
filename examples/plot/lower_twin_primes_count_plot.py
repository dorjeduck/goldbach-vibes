import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from goldbach import GoldbachPairs
from goldbach.plots.lower_twin_primes_count import plot_lower_twin_primes_count
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Plot the number of Goldbach pairs with lower twin primes for each even number in a range."
    )
    parser.add_argument(
        "--start", type=int, default=10, help="Start of even number range"
    )
    parser.add_argument("--end", type=int, default=100, help="End of even number range")
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Output file to save the plot (e.g. imgs/lower_twin_primes_count.png)",
    )
    args = parser.parse_args()
    goldbach_pairs = GoldbachPairs()
    plot_lower_twin_primes_count(
        goldbach_pairs,
        start=args.start,
        end=args.end,
        output=args.output,
    )


if __name__ == "__main__":
    main()
