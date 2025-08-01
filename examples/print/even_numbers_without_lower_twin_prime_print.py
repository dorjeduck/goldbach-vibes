import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from goldbach import GoldbachPairs
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Print even numbers in a range that do not have any Goldbach pair with a lower twin prime."
    )
    parser.add_argument(
        "--start", type=int, default=10, help="Start of even number range"
    )
    parser.add_argument("--end", type=int, default=100, help="End of even number range")
    args = parser.parse_args()
    goldbach_pairs = GoldbachPairs()
    print("Even numbers without any Goldbach pair with a lower twin prime:")
    for even_n in range(args.start, args.end + 1, 2):
        count = goldbach_pairs.count_pairs_with_lower_twin_prime(even_n)
        if count == 0:
            print(even_n)


if __name__ == "__main__":
    main()
