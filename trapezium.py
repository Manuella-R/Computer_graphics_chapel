import cairo

# Create a surface with a transparent background
width, height = 800, 800
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
context = cairo.Context(surface)

# Set transparent background
context.set_source_rgba(0, 0, 0, 0)
context.paint()

# Set color for the trapezium
context.set_source_rgb(0, 0, 0)  # Black trapezium

# Coordinates of the trapezium's four vertices
# Example of an isosceles trapezium (two equal non-parallel sides)
x1, y1 = 100, 650  # Top left
x2, y2 = 250, 650  # Top right
x3, y3 = 250, 750  # Bottom right
x4, y4 = 50, 750   # Bottom left

x5, y5 = 600, 650  # Top left
x6, y6 = 750, 650  # Top right
x7, y7 = 800, 750  # Bottom right
x8, y8 = 600, 750   # Bottom left

# Draw the trapezium
context.move_to(x1, y1)  # Move to the first point (top left)
context.line_to(x2, y2)  # Draw line to the second point (top right)
context.line_to(x3, y3)  # Draw line to the third point (bottom right)
context.line_to(x4, y4)  # Draw line to the fourth point (bottom left)
context.close_path()     # Close the shape

context.move_to(x5, y5)  # Move to the first point (top left)
context.line_to(x6, y6)  # Draw line to the second point (top right)
context.line_to(x7, y7)  # Draw line to the third point (bottom right)
context.line_to(x8, y8)  # Draw line to the fourth point (bottom left)
context.close_path()     # Close the shape

# Fill the trapezium
context.fill()

# Save the image to a file
surface.write_to_png("trapezium.png")

print("Trapezium image saved as 'trapezium.png'")

