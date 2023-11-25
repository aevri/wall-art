import numpy as np
import matplotlib.pyplot as plt

width = 800
height = 800
canvas = np.ones((height, width, 3))

x = np.linspace(0, 1, width).reshape(1, width, 1)

lime_green = np.array([[0.196, 0.804, 0.196]])
forest_green = np.array([[0.133, 0.545, 0.133]])
spring_green = np.array([[0.000, 1.000, 0.498]])
sea_green = np.array([[0.180, 0.545, 0.341]])

canvas *= sea_green * x + forest_green * (1 - x)

# Save the image as "out.png"
canvas = (canvas * 255).astype(np.uint8)
plt.imsave("out.png", canvas)
