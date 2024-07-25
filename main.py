import os

from src.analysis import analyze_turn_angles, find_repeating_patterns
from src.prime_functions import generate_primes
from src.visualizations import create_animation, plot_spiral, plot_red_line_angles_distribution

# Directory paths
image_dir = os.path.join(os.path.dirname(__file__), "images")
video_dir = os.path.join(os.path.dirname(__file__), "videos")

# Create directories if they don't exist
os.makedirs(image_dir, exist_ok=True)
os.makedirs(video_dir, exist_ok=True)

# Parameters
num_primes = 100
angles_range = (0.1, 90)
step_size = 0.01

# Generate primes
primes = generate_primes(num_primes)

# Plot a single frame with a specific turn angle
# plot_spiral(primes, 30, save_path=image_dir)
# plot_red_line_angles_distribution(primes, 30, image_dir)

# Create and save an animation
create_animation(primes, angles_range, step_size, save_path=video_dir)
