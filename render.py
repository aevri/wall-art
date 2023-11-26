import numpy as np
from scipy.ndimage import gaussian_filter
import random
import matplotlib.pyplot as plt


def draw_circle(canvas, center, radius, color):
    height, width, _ = canvas.shape
    x_coords, y_coords = np.meshgrid(np.arange(width), np.arange(height))
    distances = np.sqrt((x_coords - center[0])**2 + (y_coords - center[1])**2)
    mask = distances <= radius
    canvas[mask] = color


def main():
    width = 800
    height = 800
    mid_y = height // 2
    canvas = np.ones((height, width, 3))

    x = np.linspace(0, 1, width).reshape(1, width, 1)
    y = np.linspace(0, 1, height).reshape(height, 1, 1)

    #lime_green = np.array([[0.196, 0.804, 0.196]])
    #forest_green = np.array([[0.133, 0.545, 0.133]])
    #sea_green = np.array([[0.180, 0.545, 0.341]])
    eucalyptus_green = np.array([[0.392, 0.706, 0.588]])
    eucalyptus_green2 = np.array([[0.412, 0.706, 0.588]])
    eucalyptus_green3 = np.array([[0.372, 0.706, 0.588]])
    eucalyptus_green4 = np.array([[0.392, 0.726, 0.588]])
    eucalyptus_green5 = np.array([[0.392, 0.706, 0.608]])
    eucalyptus_green6 = np.array([[0.392, 0.686, 0.588]])

    sage_green = np.array([[0.557, 0.663, 0.557]])
    racing_green = np.array([[0.0, 0.5, 0.0]])

    color_scale = np.linspace(racing_green, eucalyptus_green5, 100)

    canvas *= eucalyptus_green * x + eucalyptus_green2 * (1 - x)
    canvas = racing_green * y + canvas * (1 - y)

    num_circles = 70

    for _ in range(num_circles):
        radius = random.randint(10, mid_y * 0.25)
        center_x = random.randint(0, width)
        center_y = random.randint(0, height)
        color = np.random.rand(1, 3)
        color[0, 1] = 0.5 * color[0, 1] + 0.5
        color = random.choice(color_scale)
        draw_circle(canvas, (center_x, center_y), radius, color)

        # Apply Gaussian filter to each color channel separately
        for i in range(3):
            canvas[:, :, i] = gaussian_filter(canvas[:, :, i], sigma=2)

    # Save the image as "out.png"
    canvas = (canvas * 255).astype(np.uint8)
    plt.imsave("out.png", canvas)


if __name__ == "__main__":
    main()
