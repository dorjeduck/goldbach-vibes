import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from goldbach import GoldbachPairs
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Print details for each even number: Goldbach pairs and count of lower twin prime pairs."
    )
    parser.add_argument(
        "--start", type=int, default=10, help="Start of even number range"
    )
    parser.add_argument("--end", type=int, default=100, help="End of even number range")
    args = parser.parse_args()
    goldbach_pairs = GoldbachPairs()
    for even_n in range(args.start, args.end + 1, 2):
        pairs = goldbach_pairs.get(even_n)
        twin_primes = set()
        for p, q in pairs:
            if p + 2 in goldbach_pairs.primes_set:
                twin_primes.add(p)
            if q + 2 in goldbach_pairs.primes_set:
                twin_primes.add(q)
        twin_count = goldbach_pairs.count_pairs_with_lower_twin_prime(even_n)
        print(f"Even: {even_n}")
        print(f"  Goldbach pairs: {pairs}")
        print(f"  Pairs with lower twin prime: {twin_count}")
        print(f"  Lower twin primes: {sorted(twin_primes)}")
        print()


if __name__ == "__main__":
    main()
