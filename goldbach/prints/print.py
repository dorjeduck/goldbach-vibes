def print_decomposition_counts(decomposer, start, end):
    if start % 2 != 0:
        start += 1
    if end % 2 != 0:
        end -= 1
    for n in range(start, end + 1, 2):
        decomps = decomposer.goldbach_decompositions(n)
        print(f"{n}: {len(decomps)}")



def print_decomposition_list(decomposer, start, end):
    if start % 2 != 0:
        start += 1
    if end % 2 != 0:
        end -= 1
    for n in range(start, end + 1, 2):
        decomps = decomposer.goldbach_decompositions(n)
        label = "decomposition" if len(decomps) == 1 else "decompositions"
        print(f"{n}: {len(decomps)} {label}")
        for p, q in decomps:
            print(f"  {n} = {p} + {q}")
        print()