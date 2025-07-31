def print_goldbach_pair_counts(goldbach_pairs, start, end):
    if start % 2 != 0:
        start += 1
    if end % 2 != 0:
        end -= 1
    for n in range(start, end + 1, 2):
        pairs = goldbach_pairs.get(n)
        print(f"{n}: {len(pairs)}")


def print_goldbach_pair_list(goldbach_pairs, start, end):
    if start % 2 != 0:
        start += 1
    if end % 2 != 0:
        end -= 1
    for n in range(start, end + 1, 2):
        pairs = goldbach_pairs.get(n)
        label = "Goldbach pair" if len(pairs) == 1 else "Goldbach pairs"
        print(f"{n}: {len(pairs)} {label}")
        for p, q in pairs:
            print(f"  {n} = {p} + {q}")
        print()
