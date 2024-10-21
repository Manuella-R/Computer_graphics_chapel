import cairo
import math

# Set up the image surface dimensions
WIDTH, HEIGHT = 200, 150  # Adjust the size as per the image
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

# Fill background with black
ctx.rectangle(0, 0, WIDTH, HEIGHT)
ctx.set_source_rgb(0, 0, 0)  # Black background
ctx.fill()

# Set the white color for the arch
ctx.set_source_rgb(1, 1, 1)  # White arch

# Draw the bottom rectangle of the arch
rect_x = WIDTH * 0.25
rect_y = HEIGHT * 0.25
rect_width = WIDTH * 0.5
rect_height = HEIGHT * 0.5
ctx.rectangle(rect_x, rect_y, rect_width, rect_height)
ctx.fill()

# Draw the top semicircle of the arch
radius = WIDTH * 0.25
center_x = WIDTH / 2
center_y = HEIGHT * 0.25 + radius

ctx.arc(center_x, center_y, radius, math.pi, 2 * math.pi)  # Semicircle
ctx.fill()

# Save the image to a PNG file
surface.write_to_png("arch_shape.png")

# Finish up
surface.finish()

print("Arch image created as 'arch_shape.png'")
