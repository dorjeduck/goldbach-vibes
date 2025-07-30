import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from goldbach.decomposer import GoldbachDecomposer
import argparse


def print_decomposition_counts(decomposer, start, end):
    if start % 2 != 0:
        start += 1
    if end % 2 != 0:
        end -= 1
    for n in range(start, end + 1, 2):
        decomps = decomposer.goldbach_decompositions(n)
        print(f"{n}: {len(decomps)}")


def main():
    parser = argparse.ArgumentParser(
        description="Print number of Goldbach decompositions per even number."
    )
    parser.add_argument(
        "--start", type=int, default=10, help="Start of even number range"
    )
    parser.add_argument("--end", type=int, default=100, help="End of even number range")
    args = parser.parse_args()
    decomposer = GoldbachDecomposer()
    print_decomposition_counts(decomposer, args.start, args.end)


if __name__ == "__main__":
    main()
