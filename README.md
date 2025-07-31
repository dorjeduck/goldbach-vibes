# Goldbach Vibes

Goldbach Vibes is a Python project for exploring the Goldbach Conjecture through code, printing, and plotting. This project is an vibe coding experiment and provides tools to analyze and visualize Goldbach pairs.

## About Goldbach Conjecture

The Goldbach Conjecture states that every even integer greater than 2 can be expressed as the sum of two prime numbers. For example:

- 10: 2 Goldbach pairs
  - 10 = 3 + 7
  - 10 = 5 + 5
- 12: 1 Goldbach pair
  - 12 = 5 + 7

Goldbach Vibes lets you explore these Goldbach pairs programmatically and visually.


## Examples

### Plotting Goldbach Pair Counts

```bash
python examples/plot/goldbach_pair_counts_plot.py --start 6 --end 50
```

Plots

![Goldbach Pair Count Plot](imgs/goldbach_pairs_counts_6_50.png)

#### Goldbach's Comet

![Goldbach Pair Count Plot](imgs/goldbach_pairs_counts_6_2000.png)

### Plotting Goldbach Pair Prime Gaps

Goldbach pair prime gaps visualize the difference between the two primes (q - p) in each Goldbach pair (p,q) for even numbers in a given range.

```bash
python examples/plot/goldbach_pair_prime_gaps_plot.py --start 6 --end 50 
```

Plots:

![Goldbach Pair Prime Gaps Plot](imgs/goldbach_pair_prime_gaps_6_50.png)
![Goldbach Pair Prime Gaps Plot](imgs/goldbach_pair_prime_gaps_6_2000.png)

### Plotting Prime Frequencies in Goldbach Pairs

Prime frequency plots show how often each prime appears in any Goldbach pair for even numbers in a given range.

```bash
python examples/plot/prime_frequency_numberline_plot.py --start 6 --end 50
```

Plots:

![Prime Frequency Plot](imgs/prime_frequency_numberline_6_50.png)
![Prime Frequency Plot](imgs/prime_frequency_numberline_6_1000.png)


## Changelog

- 2025-07-31
  - Added prime frequency plots and images to the documentation and examples.

- 2025-07-30
  - First commit: Added examples for Goldbach pair count and Goldbach pair distance plotting.

---

*Goldbach Vibes* is open for contributions and further exploration!
