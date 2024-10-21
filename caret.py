import math
import cairo


# Function to draw a caret symbol with adjustable angle
def draw_caret(cr, x, y, length, angle_deg):
    # Convert angle from degrees to radians
    angle_rad = math.radians(angle_deg)

    # Half the length of each line
    half_len = length / 2

    # Calculate the endpoints of the caret lines
    # Line 1 (left side of caret)
    x1_left = x - half_len * math.cos(angle_rad / 2)
    y1_left = y + half_len * math.sin(angle_rad / 2)

    # Line 2 (right side of caret)
    x1_right = x + half_len * math.cos(angle_rad / 2)
    y1_right = y + half_len * math.sin(angle_rad / 2)

    # Set line width
    cr.set_line_width(5)

    # Draw left line
    cr.move_to(x, y)
    cr.line_to(x1_left, y1_left)

    # Draw right line
    cr.move_to(x, y)
    cr.line_to(x1_right, y1_right)

    # Stroke the lines
    cr.stroke()


# Create a surface and Cairo context
width, height = 200, 200
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
cr = cairo.Context(surface)

# Set background color (white)
cr.set_source_rgb(1, 1, 1)
cr.paint()

# Set the caret color (black)
cr.set_source_rgb(0, 0, 0)

# Draw caret symbol with an adjustable angle at position (100, 100)
draw_caret(cr, 100, 100, 80, 50)  # 80 is the length, and 45 is the angle between the two lines

# Save the result to an image file
surface.write_to_png("church.png")
