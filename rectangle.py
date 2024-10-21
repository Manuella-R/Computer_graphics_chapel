import cairo
import math
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 350, 300)
context = cairo.Context(surface)
# Define the dimensions of the image
width, height = 400, 300

# Create a surface to draw on
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
context = cairo.Context(surface)

# Set the background color (white)
context.set_source_rgb(1, 1, 1)  # RGB for white
context.paint()

# Set the rectangle color (blue)
context.set_source_rgb(0, 0, 0)  # RGB for blue

# Define the rectangle dimensions and position
x, y, rect_width, rect_height = 50, 50, 300, 200

# Draw the rectangle
context.rectangle(x, y, rect_width, rect_height)
context.fill()  # Fill the rectangle with the current color

# Save the image to a file
surface.write_to_png("rectangle.png")

print("Rectangle drawn and saved as 'rectangle.png'")

