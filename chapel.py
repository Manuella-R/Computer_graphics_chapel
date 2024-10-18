import cairo
import math

# Create a surface with transparent background
width, height = 600, 400
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
context = cairo.Context(surface)

# Set transparent background
context.set_source_rgba(0, 0, 0, 0)
context.paint()

# Move the entire drawing downwards by 80 units
context.translate(0, 80)

# Set the drawing color (black for the church)
context.set_source_rgb(0, 0, 0)

# Draw the main rectangle (main church building)
context.rectangle(250, 150, 100, 120)
context.fill()

# Draw the two side buildings (left and right)
context.rectangle(150, 200, 100, 70)
context.fill()
context.rectangle(350, 200, 100, 70)
context.fill()

# Draw the roof for the main church
context.move_to(250, 150)
context.line_to(300, 100)  # Peak of the roof
context.line_to(350, 150)
context.close_path()
context.fill()

# Narrow steeple with flared base (trapezoid shape)
steeple_top_width = 20   # Width at the top of the steeple
steeple_base_width = 30  # Slightly wider base of the steeple
steeple_top_x = 290      # X-coordinate of the top of the steeple (centered)
steeple_base_x = 285     # X-coordinate of the base of the steeple (wider)

# Draw the steeple base (trapezoid)
context.move_to(steeple_top_x, 60)  # Top left of the steeple
context.line_to(steeple_top_x + steeple_top_width, 60)  # Top right of the steeple
context.line_to(steeple_base_x + steeple_base_width, 150)  # Bottom right of the steeple
context.line_to(steeple_base_x, 150)  # Bottom left of the steeple
context.close_path()
context.fill()

# Draw the steeple roof
context.move_to(steeple_top_x, 60)
context.line_to(300, 30)  # Peak of the steeple remains centered
context.line_to(steeple_top_x + steeple_top_width, 60)
context.close_path()
context.fill()

# Draw the enlarged cross on top of the steeple (twice as big)
context.set_line_width(6)  # Cross stroke width doubled
context.move_to(300, 40)   # Cross starting from slightly lower (y = 35)
context.line_to(300, 0)    # Extend the cross height
context.stroke()

context.move_to(288, 13)   # Lower the cross arms (y = 20)
context.line_to(312, 13)
context.stroke()

# Draw a small black rectangle between the trapezoids
rect_x = 260  # X-coordinate to center the rectangle (slightly reduced width)
rect_y = 50   # Y-coordinate for the bottom of the rectangle (lowered position)
rect_width = 80  # Shortened width of the rectangle
rect_height = 10   # Height of the rectangle

# Draw the rectangle (black fill)
context.rectangle(rect_x, rect_y, rect_width, rect_height)
context.set_source_rgb(0, 0, 0)  # Black fill
context.fill_preserve()  # Fill and preserve the outline

# Stroke the rectangle with a thinner white outline
context.set_source_rgb(1, 1, 1)  # White stroke
context.set_line_width(2)  # Thinner stroke width
context.stroke()

# Draw the front door of the church
context.set_source_rgb(1, 1, 1)  # Set color to white for the door
context.rectangle(275, 200, 50, 70)
context.fill()

# Draw small windows on the side buildings
context.rectangle(170, 220, 30, 30)
context.fill()
context.rectangle(400, 220, 30, 30)
context.fill()

# Draw a circular window on the main church building
context.arc(300, 180, 10, 0, 2 * 3.14)  # Draw a circle (x, y, radius, start_angle, end_angle)
context.fill()

# Save the image to a file
surface.write_to_png("chapel_image.png")

print("Image saved as 'chapel_image.png'")
