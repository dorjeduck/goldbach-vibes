import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from goldbach.goldbach_pairs import GoldbachPairs
from goldbach.plots.prime_frequencies_numberline import (
    plot_prime_frequencies_numberline,
)
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Plot prime frequencies on the number line in Goldbach decompositions."
    )
    parser.add_argument(
        "--start", type=int, default=10, help="Start of even number range"
    )
    parser.add_argument("--end", type=int, default=100, help="End of even number range")
    parser.add_argument(
        "--show_all_odds", action="store_true", help="Show all odd numbers on x-axis"
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Output file to save the plot (e.g. imgs/plot.png)",
    )
    args = parser.parse_args()
    decomposer = GoldbachPairs()
    plot_prime_frequencies_numberline(
        decomposer,
        start=args.start,
        end=args.end,
        show_all_odds=args.show_all_odds,
        output=args.output,
    )


if __name__ == "__main__":
    main()
