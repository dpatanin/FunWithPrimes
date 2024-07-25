import os
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


# Function to draw spiral for a specific angle
def draw_spiral_for_angle(primes, turn_angle):
    x, y = 0, 0
    coords = [(x, y)]
    step = np.radians(turn_angle)
    angles = np.arange(0, -len(primes) * step, -step)
    cos_vals = np.cos(angles)
    sin_vals = np.sin(angles)

    for i, prime in enumerate(primes):
        dx, dy = cos_vals[i], sin_vals[i]
        x, y = x + dx * prime, y + dy * prime
        coords.append((x, y))

    x_coords, y_coords = zip(*coords)
    return x_coords, y_coords


# Function to plot a single frame
def plot_spiral(primes, turn_angle, save_path):
    x_coords, y_coords = draw_spiral_for_angle(primes, turn_angle)

    fig, ax = plt.subplots(figsize=(10, 10))
    ax.plot(x_coords, y_coords, "b-")

    for x, y in zip(x_coords[1:], y_coords[1:]):
        ax.plot([0, x], [0, y], "r-")

    ax.set_aspect("equal", adjustable="box")
    ax.set_xlim(min(x_coords) - 1, max(x_coords) + 1)
    ax.set_ylim(min(y_coords) - 1, max(y_coords) + 1)
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    plt.title(f"Turn Angle: {turn_angle} degrees")

    # Save the plot
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{timestamp}_angle_{turn_angle}.png"
    filepath = os.path.join(save_path, filename)
    plt.savefig(filepath)
    plt.close(fig)


# Function to create an animation
def create_animation(primes, angles_range, step_size, save_path):
    fig, ax = plt.subplots(figsize=(10, 10))

    (spiral_line,) = ax.plot([], [], "b-")
    red_lines = [ax.plot([], [], "r-")[0] for _ in range(len(primes))]

    def update(frame):
        turn_angle = frame
        x_coords, y_coords = draw_spiral_for_angle(primes, turn_angle)

        spiral_line.set_data(x_coords, y_coords)

        for line, (x, y) in zip(red_lines, zip(x_coords[1:], y_coords[1:])):
            line.set_data([0, x], [0, y])

        ax.set_title(f"Turn Angle: {frame} degrees")
        ax.set_xlim(min(x_coords) - 1, max(x_coords) + 1)
        ax.set_ylim(min(y_coords) - 1, max(y_coords) + 1)

    ax.set_aspect("equal", adjustable="box")
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)

    ani = FuncAnimation(
        fig,
        update,
        frames=np.arange(angles_range[0], angles_range[1] + step_size, step_size),
        repeat=True,
        interval=40,
    )

    # Save the animation
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = (
        f"{timestamp}_range_{angles_range[0]}_{angles_range[1]}_step_{step_size}.mp4"
    )
    filepath = os.path.join(save_path, filename)
    ani.save(filepath, writer="ffmpeg", dpi=40)
    plt.close(fig)


# Function to plot pattern analysis
def plot_pattern_analysis(patterns, save_path):
    angles = list(patterns.keys())
    counts = [
        (
            patterns[angle]
            if isinstance(patterns[angle], int)
            else np.mean(patterns[angle])
        )
        for angle in angles
    ]

    plt.figure(figsize=(10, 6))
    plt.plot(angles, counts, marker="o")
    plt.xlabel("Turn Angle (degrees)")
    plt.ylabel("Mean Count of Points per Curve")
    plt.title("Pattern Analysis of Points per Spiral Curve")
    plt.grid(True)

    # Save the plot
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{timestamp}_pattern_analysis.png"
    filepath = os.path.join(save_path, filename)
    plt.savefig(filepath)
    plt.close()
