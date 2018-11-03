from PIL import Image
import pygame
import colorsys

def load_and_resize_image(path, size):
    # Load the image
    image = Image.open(path)

    # Resize it using the wanted size
    image = image.resize(size, Image.BILINEAR)

    # Convert it to a pygame image from the image bytes, size and mode
    return pygame.image.fromstring(image.tobytes(), image.size, image.mode)

def get_overlap_point(surface1, rect1, surface2, rect2):
    # Get the masks of both surfaces
    mask1 = pygame.mask.from_surface(surface1)
    mask2 = pygame.mask.from_surface(surface2)

    # Set the offset between the 2 masks as the position differences
    offset = (rect2.x - rect1.x, rect2.y - rect1.y)

    # Get the relative overlap point from first surface if the two surfaces overlap each other
    relative_overlap_point = mask1.overlap(mask2, offset)

    # If the overlap point exists, calculate the real overlap point in the screen using the position of the first surface
    if relative_overlap_point is not None:
        real_overlap_point = (relative_overlap_point[0] + rect1.x - 2, relative_overlap_point[1] + rect1.y - 2)
    else:
        real_overlap_point = None

    return real_overlap_point

def color_is_black(color):
    # Check if the color is in the low range so it's black
    return (color[0] in range(0, 10) and
            color[1] in range(0, 10) and
            color[2] in range(0, 10))

def get_hue_from_color(color):
    # Convert the color to an hsv color to get it's hue
    hsv_color = colorsys.rgb_to_hsv(color[0] / 255,
                                    color[1] / 255,
                                    color[2] / 255)

    # Get the actual hue from the hsv color
    return int(hsv_color[0] * 360)

def compare_colors(color1, color2):
    # Get the hue values of both colors
    color1_hue = get_hue_from_color(color1)
    color2_hue = get_hue_from_color(color2)

    return color1_hue == color2_hue

def get_dominant_color_from_image(path):
    # Load the image
    image = Image.open(path)

    # Get all the colors from the image (count, color) and order them by the count
    image_colors = image.getcolors()
    image_colors = sorted(image_colors, key=lambda x: x[0], reverse=True)

    # Return the most used color
    return image_colors[0][1]