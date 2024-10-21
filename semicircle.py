import cairo
import math

# Set up the image surface dimensions
WIDTH, HEIGHT = 200, 150
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

# Fill background with white
ctx.rectangle(0, 0, WIDTH, HEIGHT)
ctx.set_source_rgb(1, 1, 1)  # White background
ctx.fill()

# Set black color for the semicircle
ctx.set_source_rgb(0, 0, 0)

# Define the radius and center of the semicircle
radius = WIDTH // 4
center_x = WIDTH // 2
center_y = HEIGHT // 2

# Draw the semicircle (arc from π to 2π, which gives the lower half of the circle)
ctx.arc(center_x, center_y, radius, math.pi, 2 * math.pi)

# Fill the semicircle
ctx.fill()

# Save the image to a PNG file
surface.write_to_png("semi_circle.png")

# Finish up
surface.finish()

print("Semicircle image created as 'semi_circle.png'")
