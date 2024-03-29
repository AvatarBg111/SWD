import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.animation import FuncAnimation
import numpy as np

def update(frame):
    img.set_data(rotate_image(image, frame))
    # Update googly eyes position
    left_eye.set_data(rotate_eye(50, 80, frame))
    right_eye.set_data(rotate_eye(130, 80, frame))
    return img, left_eye, right_eye

def rotate_eye(x, y, frame):
    angle = np.radians((frame / 60) * 360 * 20)  # Calculate rotation angle based on RPM
    # Offset the eyes slightly to create a funny effect
    offset = 5 * np.sin(angle)
    return x + offset, y

def rotate_image(image, frame):
    angle = (frame / 60) * 360 * 20  # Calculate rotation angle based on RPM
    return np.rot90(image, angle // 90)  # Rotate the image

# Load the image
image_path = "example_image.jpg"  # Change this to the path of your image
image = mpimg.imread(image_path)

# Create a figure and axis
fig, ax = plt.subplots()

# Display the initial image
img = ax.imshow(image)
plt.axis('off')  # Turn off axis

# Add googly eyes
left_eye = ax.plot([], [], 'o', color='black', markersize=10)[0]
right_eye = ax.plot([], [], 'o', color='black', markersize=10)[0]

# Animate the rotation
ani = FuncAnimation(fig, update, frames=range(0, 360), interval=50)

plt.show()
