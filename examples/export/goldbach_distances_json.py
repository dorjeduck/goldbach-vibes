#!/usr/bin/env python3
"""
Export Goldbach distances to JSON format.

Creates a JSON file containing range information and an array of Goldbach distances.
"""

import argparse
import json
import sys
import os

# Add the parent directory to the path to import goldbach module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from goldbach.goldbach_pairs import GoldbachPairs


def export_goldbach_distances_json(start, end, output_file=None):
    """
    Export Goldbach distances to JSON format.

    Args:
        start: Start of the range (inclusive)
        end: End of the range (inclusive)
        output_file: Output filename (optional)
    """
    # Generate Goldbach distances
    gp = GoldbachPairs()
    gp.ensure_sieve(end + 50)  # Extra buffer for distance calculations
    distances = []

    for n in range(start, end + 1):
        distance = gp.goldbach_distance(n)
        distances.append(distance)

    # Create JSON data structure
    data = {
        "range": {"start": start, "end": end},
        "goldbach_distances": distances,
    }

    # Determine output filename
    if output_file is None:
        output_file = f"goldbach_distances_{start}_{end}.json"

    # Ensure output directory exists
    os.makedirs("data", exist_ok=True)
    output_path = os.path.join("data", output_file)

    # Write JSON file
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)

    print(f"Goldbach distances exported to {output_path}")
    print(f"Range: [{start}, {end}]")
    return output_path


def main():
    parser = argparse.ArgumentParser(
        description="Export Goldbach distances to JSON format"
    )
    parser.add_argument(
        "--start", type=int, default=2, help="Start of the range (default: 2)"
    )
    parser.add_argument(
        "--end", type=int, default=100, help="End of the range (default: 100)"
    )
    parser.add_argument(
        "--output", type=str, help="Output filename (default: auto-generated)"
    )

    args = parser.parse_args()

    print(f"Exporting Goldbach distances for range [{args.start}, {args.end}]...")

    export_goldbach_distances_json(
        start=args.start, end=args.end, output_file=args.output
    )


if __name__ == "__main__":
    main()
