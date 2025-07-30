"""
Main entry point for Goldbach analysis and plotting.
"""

from goldbach.decomposer import GoldbachDecomposer
from goldbach.plots.decomposition_distances import PlotDecompositionDistances

if __name__ == "__main__":
    decomposer = GoldbachDecomposer()
    # Example: print decomposition distances for 10, 20, 100
    for even_n in [10, 20, 100]:
        print(
            f"Decomposition distances for {even_n}: {decomposer.decomposition_distances(even_n)}"
        )
    # Example: plot decomposition distances for a range
    PlotDecompositionDistances.plot(decomposer, 10, 100)
