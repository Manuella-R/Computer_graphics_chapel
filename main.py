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

# Coordinates of the trapezium's four vertices
# Example of an isosceles trapezium (two equal non-parallel sides)
x7, y7 = 100, 650  # Top left
x8, y8 = 250, 650  # Top right
x9, y9 = 250, 750  # Bottom right
x10, y10 = 50, 750   # Bottom left

x11, y11 = 600, 650  # Top left
x12, y12 = 750, 650  # Top right
x13, y13 = 800, 750  # Bottom right
x14, y14 = 600, 750   # Bottom left

# Draw the trapezium
context.move_to(x7, y7)  # Move to the first point (top left)
context.line_to(x8, y8)  # Draw line to the second point (top right)
context.line_to(x9, y9)  # Draw line to the third point (bottom right)
context.line_to(x10, y10)  # Draw line to the fourth point (bottom left)
context.close_path()     # Close the shape

context.move_to(x11, y11)  # Move to the first point (top left)
context.line_to(x12, y12)  # Draw line to the second point (top right)
context.line_to(x13, y13)  # Draw line to the third point (bottom right)
context.line_to(x14, y14)  # Draw line to the fourth point (bottom left)
context.close_path()     # Close the shape

# Fill the trapezium
context.fill()

# Define the rectangle dimensions and position
x, y, rect_width, rect_height = 100, 750, 300, 300

# Draw the rectangle
context.rectangle(x, y, rect_width, rect_height)
context.fill()  # Fill the rectangle with the current color

# Save the image to a file
surface.write_to_png("Chapel_roan.png")

print("Trapezium image saved as 'Chapel_roan.png'")
