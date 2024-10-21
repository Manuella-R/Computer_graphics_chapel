import cairo
import math

# Set up the image surface
WIDTH, HEIGHT = 400, 300
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

# Background fill
ctx.set_source_rgb(0.8, 0.8, 0.8)  # Light gray background
ctx.paint()

# Set up line width for consistent strokes
ctx.set_line_width(2)

# Draw the base below the cross (top part)
ctx.move_to(180, 90)
ctx.line_to(210, 90)
ctx.line_to(200, 50)
ctx.line_to(190, 50)
ctx.close_path()
ctx.set_source_rgb(0, 0, 0)  # Black fill
ctx.fill()

# Join the two parts of the top
ctx.move_to(190, 50)
ctx.line_to(200, 50)
ctx.line_to(195, 40)
ctx.line_to(190, 50)
ctx.set_source_rgb(0, 0, 0)
ctx.fill()

# Draw the cross
ctx.move_to(195, 50)
ctx.line_to(195, 15)
ctx.move_to(185, 25)
ctx.line_to(205, 25)
ctx.set_source_rgb(0, 0, 0)
ctx.stroke()

# Bar below the cross
ctx.rectangle(160, 91, 70, 9)
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

# Draw side rectangular structures (the two smaller buildings/shells)
ctx.rectangle(50, 220, 80, 40)  # Left building
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

ctx.rectangle(260, 220, 80, 40)  # Right building
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

# Small white windows on both sides
for (x, y) in [(60, 230), (90, 230), (280, 230), (310, 230)]:
    ctx.rectangle(x, y, 20, 15)
    ctx.set_source_rgb(1, 1, 1)
    ctx.fill()

# Draw trapezoids on both sides
ctx.move_to(80, 190)
ctx.line_to(130, 190)
ctx.line_to(130, 220)
ctx.line_to(40, 220)
ctx.close_path()
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

ctx.move_to(260, 190)
ctx.line_to(310, 190)
ctx.line_to(350, 220)
ctx.line_to(260, 220)
ctx.close_path()
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

# Draw the center block of the building
ctx.move_to(130, 170)
ctx.line_to(130, 270)
ctx.line_to(260, 270)
ctx.line_to(260, 170)
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

# Center block windows
ctx.rectangle(160, 220, 34, 47)
ctx.rectangle(196, 220, 34, 47)
ctx.fill()

# Roof above the door
ctx.move_to(150, 220)
ctx.line_to(195, 200)
ctx.line_to(240, 220)
ctx.line_to(240, 210)
ctx.line_to(195, 190)
ctx.line_to(150, 210)
ctx.close_path()
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

# Central block structure
ctx.move_to(130, 170)
ctx.line_to(260, 170)
ctx.line_to(240, 160)
ctx.line_to(150, 160)
ctx.close_path()
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

# Center block roof
ctx.move_to(120, 180)
ctx.line_to(150, 160)
ctx.line_to(240, 160)
ctx.line_to(270, 180)
ctx.line_to(270, 170)
ctx.line_to(240, 150)
ctx.line_to(150, 150)
ctx.line_to(120, 170)
ctx.close_path()
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

# Center window (circular)
ctx.arc(195, 175, 10, 0, 2 * math.pi)
ctx.set_source_rgb(1, 1, 1)
ctx.fill()

# Top part of the center
ctx.rectangle(170, 100, 50, 50)
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.stroke()

ctx.move_to(180, 120)
ctx.line_to(180, 147)
ctx.line_to(210, 147)
ctx.line_to(210, 120)
ctx.arc(195, 120, 15, math.pi, 0)
ctx.set_source_rgb(1, 1, 1)
ctx.fill_preserve()
ctx.stroke()

# Save the image as 'chapel.png'
surface.write_to_png('chapel.png')

print("Image saved as 'chapel.png'")
