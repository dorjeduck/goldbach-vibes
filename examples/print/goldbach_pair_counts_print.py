import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from goldbach import GoldbachPairs
from goldbach.prints.print import print_goldbach_pair_counts
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Print number of Goldbach decompositions per even number."
    )
    parser.add_argument(
        "--start", type=int, default=10, help="Start of even number range"
    )
    parser.add_argument("--end", type=int, default=100, help="End of even number range")
    args = parser.parse_args()
    goldbach_pairs = GoldbachPairs()
    print_goldbach_pair_counts(goldbach_pairs, args.start, args.end)


if __name__ == "__main__":
    main()
