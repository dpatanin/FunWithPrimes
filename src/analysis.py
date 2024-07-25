from typing import Any
import numpy as np

from src.visualizations import draw_spiral_for_angle


def analyze_turn_angles(primes: np.ndarray[Any, np.dtype[np.intp]], angles_range, step_size):
    angle_points = {}
    for turn_angle in np.arange(
        angles_range[0], angles_range[1] + step_size, step_size
    ):
        x_coords, y_coords = draw_spiral_for_angle(primes, turn_angle)

        distances = np.sqrt(np.diff(x_coords) ** 2 + np.diff(y_coords) ** 2)

        unique_distances, counts = np.unique(distances, return_counts=True)
        angle_points[turn_angle] = (unique_distances, counts)

    return angle_points


def find_repeating_patterns(angle_points):
    patterns = {}
    for angle, (distances, counts) in angle_points.items():
        repeating_pattern = counts.max() == counts.min()
        patterns[angle] = counts[0] if repeating_pattern else counts
    return patterns
