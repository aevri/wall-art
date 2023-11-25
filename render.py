import numpy as np
import matplotlib.pyplot as plt

# Create a white square image
image = np.ones((800, 800, 3), dtype=np.uint8) * 255

# Save the image as "out.png"
plt.imsave("out.png", image)