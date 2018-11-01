from PIL import Image
import pygame

def load_and_resize_image(path, size):
    # Load the image
    image = Image.open(path)

    # Resize it using the wanted size
    image = image.resize(size, Image.BILINEAR)

    # Convert it to a pygame image from the image bytes, size and mode
    return pygame.image.fromstring(image.tobytes(), image.size, image.mode)