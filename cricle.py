"""
>>> draw_circle(100)
"""

import math
import matplotlib.pyplot as plt

def draw_circle(radius: int) -> list[tuple[float, float]]:
    result = []

    theta = 0

    while theta <= math.pi / 2:
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)

        result.extend([
            (x, y), # quad 1
            (-x, y), # quad 2
            (-x, -y), # quad 3
            (x, -y), # quad 4
        ])

        theta = theta + 1. / radius

    return result

if __name__ == "__main__":
    points = draw_circle(10)
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    plt.scatter(x, y)
    plt.show()
