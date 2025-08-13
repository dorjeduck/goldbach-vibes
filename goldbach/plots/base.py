"""
Base plotting functionality for Goldbach analysis.
"""

import matplotlib.pyplot as plt
import os
from ..goldbach_pairs import GoldbachPairs


class BasePlot:
    """Base class for all Goldbach plotting functionality."""

    def __init__(self):
        self.goldbach_pairs = GoldbachPairs()

    def save_plot(self, filename):
        """Save the current plot to the imgs directory."""
        # Ensure the imgs directory exists
        imgs_dir = "imgs"
        if not os.path.exists(imgs_dir):
            os.makedirs(imgs_dir)

        # Save the plot
        filepath = os.path.join(imgs_dir, filename)
        plt.savefig(filepath, dpi=300, bbox_inches="tight")
        plt.close()
