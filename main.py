import os

import numpy as np

from src.analysis import analyze_turn_angles, find_repeating_patterns
from src.prime_functions import (
    generate_prime_fractions,
    generate_prime_of_primes,
    generate_primes,
    subtract_primes_by_index,
)
from src.visualizations import (
    create_animation,
    plot_fractions,
    plot_red_line_angles_distribution,
    plot_spiral,
)

# Directory paths
image_dir = os.path.join(os.path.dirname(__file__), "images")
video_dir = os.path.join(os.path.dirname(__file__), "videos")

# Create directories if they don't exist
os.makedirs(image_dir, exist_ok=True)
os.makedirs(video_dir, exist_ok=True)

# Parameters
num_primes = 100000000
angles_range = (0.1, 90)
step_size = 0.01

# Generate Prime fractions
fractions = generate_prime_fractions(num_primes)

# Plot the fractions
print(fractions[-1])
# plot_fractions(fractions)

# Generate primes
# primes = subtract_primes_by_index(num_primes)

# Plot a single frame with a specific turn angle
# plot_spiral(primes, 90, save_path=image_dir, plot_red_lines=False)
# plot_red_line_angles_distribution(primes, 30, image_dir)

# Create and save an animation
# create_animation(primes, angles_range, step_size, save_path=video_dir)

# 0.22, 0.185, 0.174, 0.164 -> 50er steps
# 0.185, 0.126, 0.096, 0.077, 0.065, 0.056, 0.049 -> 10er potenz
