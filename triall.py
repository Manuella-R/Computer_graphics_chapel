import cairo
import math

# Set up the image surface
WIDTH, HEIGHT = 400, 400
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

# Background fill (transparent)
ctx.set_source_rgba(0, 0, 0, 0)  # Transparent background
ctx.paint()

# Set up line width for consistent strokes
ctx.set_line_width(2)

# Draw the main center building structure
ctx.rectangle(130, 170, 140, 150)  # Main building
ctx.set_source_rgb(0, 0, 0)  # Black fill
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)  # White stroke
ctx.stroke()

# Draw the front door (arched shape)
ctx.move_to(160, 320)
ctx.line_to(160, 270)
ctx.arc(200, 270, 40, math.pi, 0)
ctx.line_to(240, 320)
ctx.set_source_rgb(1, 1, 1)
ctx.fill()

# Draw the circular window above the door
ctx.arc(200, 210, 15, 0, 2 * math.pi)  # Circular window
ctx.set_source_rgb(1, 1, 1)
ctx.fill()

# Draw the tower part above the main building
ctx.rectangle(160, 100, 80, 70)  # Tower
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

# Draw the arched window in the tower
ctx.move_to(180, 140)
ctx.line_to(180, 170)
ctx.arc(200, 140, 20, math.pi, 0)
ctx.line_to(220, 170)
ctx.set_source_rgb(1, 1, 1)
ctx.fill()

# Draw the roof part of the tower
ctx.move_to(140, 100)
ctx.line_to(260, 100)
ctx.line_to(230, 80)
ctx.line_to(170, 80)
ctx.close_path()
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

# Draw the cross on top of the tower
ctx.move_to(195, 40)
ctx.line_to(195, 80)
ctx.move_to(185, 60)
ctx.line_to(205, 60)
ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(5)
ctx.stroke()

# Draw the two side structures (rectangular)
ctx.rectangle(50, 270, 80, 50)  # Left building
ctx.rectangle(270, 270, 80, 50)  # Right building
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

# Draw windows on the side structures
for (x, y) in [(60, 285), (100, 285), (280, 285), (320, 285)]:
    ctx.rectangle(x, y, 20, 20)
    ctx.set_source_rgb(1, 1, 1)
    ctx.fill()

# Save the image as 'chapel_updated.png'
surface.write_to_png('chapel_updated.png')

print("Image saved as 'chapel_updated.png'")
