import cairo

# Create a surface with transparent background
width, height = 600, 400
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
context = cairo.Context(surface)

# Set transparent background
context.set_source_rgba(0, 0, 0, 0)
context.paint()

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

# Draw the steeple (tower)
context.rectangle(285, 70, 30, 80)
context.fill()

# Draw the steeple roof
context.move_to(285, 70)
context.line_to(300, 40)  # Peak of the steeple
context.line_to(315, 70)
context.close_path()
context.fill()

# Draw the cross on top of the steeple
context.set_line_width(3)
context.move_to(300, 30)
context.line_to(300, 15)
context.stroke()

context.move_to(295, 22.5)
context.line_to(305, 22.5)
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
surface.write_to_png("exact_church_image.png")

print("Image saved as 'exact_church_image.png'")
