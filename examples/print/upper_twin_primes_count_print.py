import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from goldbach import GoldbachPairs
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Print the number of Goldbach pairs with upper twin primes for each even number in a range."
    )
    parser.add_argument(
        "--start", type=int, default=10, help="Start of even number range"
    )
    parser.add_argument("--end", type=int, default=100, help="End of even number range")
    args = parser.parse_args()
    goldbach_pairs = GoldbachPairs()
    print(f"Even\tNumberOfUpperTwinPrimePairs")
    for even_n in range(args.start, args.end + 1, 2):
        count = goldbach_pairs.count_pairs_with_upper_twin_prime(even_n)
        print(f"{even_n}\t{count}")


if __name__ == "__main__":
    main()
