import os

from src.analysis import analyze_turn_angles, find_repeating_patterns
from src.prime_functions import generate_primes
from src.visualizations import create_animation, plot_pattern_analysis, plot_spiral

# Directory paths
image_dir = os.path.join(os.path.dirname(__file__), "images")
video_dir = os.path.join(os.path.dirname(__file__), "videos")

# Create directories if they don't exist
os.makedirs(image_dir, exist_ok=True)
os.makedirs(video_dir, exist_ok=True)

# Parameters
num_primes = 100
angles_range = (1, 90)
step_size = 0.1

# Generate primes
primes = generate_primes(num_primes)

# Plot a single frame with a specific turn angle
plot_spiral(primes, 30, save_path=image_dir)

# Create and save an animation
create_animation(primes, angles_range, step_size, save_path=video_dir)

# Analyze patterns
# angle_points = analyze_turn_angles(primes, angles_range, step_size)
# patterns = find_repeating_patterns(angle_points, save_path=image_dir)

# Plot pattern analysis
# plot_pattern_analysis(patterns)

# # Print angles with repeating patterns
# for angle, count in patterns.items():
#     if isinstance(count, int):
#         print(f"Turn Angle: {angle} degrees has {count} points per curve.")
