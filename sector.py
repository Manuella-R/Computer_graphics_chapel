import cairo

# Create the surface and context
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 1200, 800)
ctx = cairo.Context(surface)

# Set background color (gray)
ctx.set_source_rgb(0.8, 0.8, 0.8)  # Light gray background
ctx.paint()

# Set stroke properties (white)
ctx.set_source_rgb(1, 1, 1)        # White color for the stroke
ctx.set_line_width(5)              # Stroke width

# Draw the main rectangle (house body)
ctx.rectangle(340, 350, 320, 150)  # x, y, width, height (main structure)

# Fill the house with black, but preserve the path for the stroke
ctx.set_source_rgb(0, 0, 0)        # Black fill for the house
ctx.fill_preserve()

# Stroke the house (outline it)
ctx.set_source_rgb(1, 1, 1)        # White stroke
ctx.stroke()

# Draw the trapezoid (roof)
ctx.move_to(340, 350)   # Bottom left of roof
ctx.line_to(700, 350)   # Bottom right of roof
ctx.line_to(600, 230)   # Top right (slanted roof)
ctx.line_to(340, 230)   # Top left (slanted roof)
ctx.close_path()

# Fill the roof with black, but preserve the path for the stroke
ctx.set_source_rgb(0, 0, 0)        # Black fill for the roof
ctx.fill_preserve()

# Stroke the roof (outline it)
ctx.set_source_rgb(1, 1, 1)        # White stroke
ctx.stroke()

# Draw two windows (white squares)
window_size = 60  # Size of the windows
window_spacing = 30  # Spacing between windows

# First window (left)
ctx.rectangle(420, 390, window_size, window_size)  # x, y, width, height
ctx.set_source_rgb(1, 1, 1)  # White fill for windows
ctx.fill_preserve()

# Stroke the window (outline)
ctx.set_source_rgb(1, 1, 1)  # White stroke
ctx.stroke()

# Second window (right)
ctx.rectangle(540, 390, window_size, window_size)  # x, y, width, height
ctx.set_source_rgb(1, 1, 1)  # White fill for windows
ctx.fill_preserve()

# Stroke the window (outline)
ctx.set_source_rgb(1, 1, 1)  # White stroke
ctx.stroke()

# Save the image
surface.write_to_png("church.png")
