#!/usr/bin/env python3
"""
Analyze Goldbach distances from JSON files and provide statistical information.
"""

import argparse
import json
import sys
import os
from collections import Counter
import math


def analyze_goldbach_distances(json_file):
    """
    Analyze Goldbach distances from a JSON file and print statistics.

    Args:
        json_file: Path to the JSON file containing Goldbach distances
    """
    # Load JSON data
    try:
        with open(json_file, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{json_file}' not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in file '{json_file}'.")
        return

    # Extract data
    range_info = data.get("range", {})
    distances = data.get("goldbach_distances", [])

    if not distances:
        print("Error: No Goldbach distances found in the JSON file.")
        return

    start = range_info.get("start", "Unknown")
    end = range_info.get("end", "Unknown")
    count = len(distances)

    print(f"=== Goldbach Distance Analysis ===\n")
    print(f"Range: [{start}, {end}]")
    print()

    # Basic statistics
    min_distance = min(distances)
    max_distance = max(distances)
    mean_distance = sum(distances) / len(distances)

    # Find numbers with maximum distance
    max_distance_numbers = []
    for i, distance in enumerate(distances):
        if distance == max_distance:
            number = start + i
            max_distance_numbers.append(number)

    # Median
    sorted_distances = sorted(distances)
    n = len(sorted_distances)
    if n % 2 == 0:
        median_distance = (sorted_distances[n // 2 - 1] + sorted_distances[n // 2]) / 2
    else:
        median_distance = sorted_distances[n // 2]

    # Standard deviation
    variance = sum((x - mean_distance) ** 2 for x in distances) / len(distances)
    std_deviation = math.sqrt(variance)

    print(f"Minimum distance: {min_distance}")
    if len(max_distance_numbers) == 1:
        print(f"Maximum distance: {max_distance} (at n={max_distance_numbers[0]})")
    else:
        print(
            f"Maximum distance: {max_distance} (at n={', '.join(map(str, max_distance_numbers))})"
        )
    print(f"Mean distance: {mean_distance:.3f}")
    print(f"Median distance: {median_distance:.3f}")
    print(f"Standard deviation: {std_deviation:.3f}")
    print()

    # Distribution analysis
    distance_counts = Counter(distances)
    unique_distances = len(distance_counts)

    print(f"Unique distances: {unique_distances}")
    print(f"Most common distances:")
    for distance, count in distance_counts.most_common(10):
        percentage = (count / len(distances)) * 100
        special_note = ""
        if distance == 0:
            special_note = " (primes)"
        elif distance == 1:
            special_note = " (between twin primes)"
        print(f"  Distance {distance}: {count} times ({percentage:.1f}%){special_note}")
    print()

    # Zero distance analysis (primes)
    zero_count = distance_counts.get(0, 0)
    prime_percentage = (zero_count / len(distances)) * 100

    print(f"Numbers with distance 0 (primes): {zero_count} ({prime_percentage:.1f}%)")

    # Distance 1 analysis (twin prime centers)
    distance_1_count = distance_counts.get(1, 0)
    twin_prime_percentage = (distance_1_count / len(distances)) * 100

    print(
        f"Numbers with distance 1 (between twin primes): {distance_1_count} ({twin_prime_percentage:.1f}%)"
    )

    # Non-zero distance analysis
    non_zero_distances = [d for d in distances if d > 0]
    if non_zero_distances:
        non_zero_mean = sum(non_zero_distances) / len(non_zero_distances)
        non_zero_min = min(non_zero_distances)
        non_zero_max = max(non_zero_distances)
        print(f"\nNon-zero distances: {len(non_zero_distances)} numbers")
        print(f"Mean non-zero distance: {non_zero_mean:.3f}")
        print(f"Range of non-zero distances: [{non_zero_min}, {non_zero_max}]")
    print()

    # Growth analysis - adapt to range size with max 10 subranges
    total_numbers = len(distances)
    if total_numbers > 50:  # Only show growth pattern for reasonably large datasets
        print(f"=== Growth Pattern ===")
        # Calculate chunk size to get exactly 10 subranges
        num_chunks = 10 if total_numbers >= 200 else max(5, total_numbers // 40)
        chunk_size = total_numbers // num_chunks

        ranges_shown = 0
        for i in range(0, len(distances), chunk_size):
            if ranges_shown >= 10:  # Hard limit to 10 ranges
                break
            chunk = distances[i : i + chunk_size]
            chunk_start = start + i  # start number + index offset
            chunk_end = min(start + i + len(chunk) - 1, end)  # Use actual chunk length
            chunk_max = max(chunk)
            chunk_mean = sum(chunk) / len(chunk)
            print(
                f"  Range [{chunk_start}, {chunk_end}]: max={chunk_max}, mean={chunk_mean:.2f}"
            )
            ranges_shown += 1


def main():
    parser = argparse.ArgumentParser(
        description="Analyze Goldbach distances from JSON files"
    )
    parser.add_argument(
        "json_file", help="Path to the JSON file containing Goldbach distances"
    )

    args = parser.parse_args()

    analyze_goldbach_distances(args.json_file)


if __name__ == "__main__":
    main()
