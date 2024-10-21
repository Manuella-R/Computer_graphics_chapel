import cairo
import math
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 350, 300)
context = cairo.Context(surface)
# right door
context.move_to(140,90)
context.line_to(140,200)
context.line_to(180,200)
context.line_to(180,110)
context.set_source_rgb(1,1,1)
context.fill()
context.move_to(140,110)
context.arc(140,110,40,3* math.pi/2,0)
context.set_source_rgb(1,1,1)
context.fill()
#left door
context.move_to(135, 90)
context.line_to(135, 200)
context.line_to(95, 200)
context.line_to(95, 110)
context.set_source_rgb(1, 1, 1)
context.close_path()
context.fill()
context.move_to(135, 90)
context.arc(135, 110, 40, math.pi , 3* math.pi/2)
context.set_source_rgb(1, 1, 1)
context.fill()
# ceiling design
context.move_to(200,110)
context.line_to(200,200)
context.line_to(270,200)
context.line_to(270,110)
context.set_source_rgb(1, 1, 1)
context.stroke()
context.arc(235,110,35, math.pi , 0)
context.set_source_rgb(1, 1, 1)
context.stroke()

surface.write_to_png("door.png")
