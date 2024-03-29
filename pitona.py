import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def visualize_image(image_path):
    # Load the image
    img = mpimg.imread(image_path)
    
    # Display the image
    plt.imshow(img)
    plt.axis('off')  # Turn off axis
    plt.show()

# Example usage:
image_path = "image_go_brrr.jpg"  # Change this to the path of your image
visualize_image(image_path)
