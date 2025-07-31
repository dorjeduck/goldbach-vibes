import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from goldbach import GoldbachPairs
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Print all Goldbach decompositions per even number."
    )
    parser.add_argument(
        "--start", type=int, default=10, help="Start of even number range"
    )
    parser.add_argument("--end", type=int, default=100, help="End of even number range")
    args = parser.parse_args()
    goldbach_pairs = GoldbachPairs()

    res_max = None
    for even_number in range(args.start, args.end + 1, 2):
        res = goldbach_pairs.pair_with_smallest_lower_prime(even_number)
        
        if res_max is None or res[0] > res_max[0]:
            res_max = res
          
    print(res_max)


if __name__ == "__main__":
    main()
