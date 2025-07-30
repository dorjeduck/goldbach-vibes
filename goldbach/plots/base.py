"""
Base class for Goldbach plotters. Provides shared plotting utilities.
"""


class GoldbachPlotBase:
    @staticmethod
    def get_marker_size(n_points):
        """
        Return a marker size that decreases smoothly as the number of points increases.
        Uses an inverse square root scaling, clamped to a reasonable range.
        """
        import numpy as np

        max_size = 50
        min_size = 1
        size = max_size / np.sqrt(max(n_points, 1))
        return int(round(max(min_size, size)))
