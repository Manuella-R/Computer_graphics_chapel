import cairo

# Create a surface with a transparent background
width, height = 1000, 1000
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
context = cairo.Context(surface)

# Set transparent background
context.set_source_rgba(0, 0, 0, 0)
context.paint()

# Set color for the trapezium (black)
context.set_source_rgb(0, 0, 0)

# Coordinates of the trapezium's six vertices (including the two vertices for the second block)
x1, y1 = 250, 900  # Bottom left of the first block
x2, y2 = 250, 650  # Top left of the first block
x3, y3 = 300, 550  # Top right of the first block
x4, y4 = 550, 550  # Bottom right of the first block
x5, y5 = 600, 650  # Top right of the second block
x6, y6 = 600, 900  # Bottom right of the second block

# Draw the first trapezium (connecting points x1 -> x2 -> x3 -> x4)
context.move_to(x1, y1)  # Move to the first point (bottom left of the first block)
context.line_to(x2, y2)  # Line to top left of the first block
context.line_to(x3, y3)  # Line to top right of the first block
context.line_to(x4, y4)  # Line to bottom right of the first block
context.close_path()     # Close the first shape

# Fill the first trapezium
context.fill()

# Now draw the second trapezium (connecting points x4 -> x5 -> x6 -> x1)
context.move_to(x4, y4)  # Start from the bottom right of the first block
context.line_to(x5, y5)  # Draw line to top right of the second block
context.line_to(x6, y6)  # Line to bottom right of the second block
context.line_to(x1, y1)  # Line back to the starting point of the first block
context.close_path()     # Close the shape

# Fill the second trapezium
context.fill()

# Save the image to a file
surface.write_to_png("main_block.png")

print("Trapezium image saved as 'main_block.png'")
