import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def generate_primes(n):
    def sieve(limit):
        is_prime = np.ones(limit + 1, dtype=bool)
        is_prime[:2] = False
        for p in range(2, int(limit**0.5) + 1):
            if is_prime[p]:
                is_prime[p * p : limit + 1 : p] = False
        return np.nonzero(is_prime)[0]

    limit = int(n * np.log(n) * 1.2)
    primes = sieve(limit)
    return primes[:n]


def draw_spiral_for_angle(primes, turn_angle):
    x, y = 0, 0
    coords = [(x, y)]
    angle = 0
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


def update(frame):
    turn_angle = frame
    x_coords, y_coords = draw_spiral_for_angle(primes, turn_angle)

    # Update the spiral plot
    spiral_line.set_data(x_coords, y_coords)

    # Update the red lines from the center to each point
    for line, (x, y) in zip(red_lines, zip(x_coords[1:], y_coords[1:])):
        line.set_data([0, x], [0, y])

    ax.set_title(f"Turn Angle: {frame} degrees")
    ax.set_xlim(min(x_coords) - 1, max(x_coords) + 1)
    ax.set_ylim(min(y_coords) - 1, max(y_coords) + 1)


# Parameters
num_primes = 100
angles_range = (1, 90)
step_size = 0.1

# Generate primes
primes = generate_primes(num_primes)

# Set up figure and axis
fig, ax = plt.subplots(figsize=(10, 10))

# Initialize the spiral line
(spiral_line,) = ax.plot([], [], "b-")

# Initialize the red lines from the center to each point
red_lines = [ax.plot([], [], "r-")[0] for _ in range(num_primes)]

# Set up axis properties
ax.set_aspect("equal", adjustable="box")
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

# Create animation
ani = FuncAnimation(
    fig,
    update,
    frames=np.arange(angles_range[0], angles_range[1] + step_size, step_size),
    repeat=True,
    interval=120,
)

# Save animation
ani.save("prime_spiral_animation.mp4", writer="ffmpeg", dpi=100)

plt.show()
