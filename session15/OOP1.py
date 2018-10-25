import math


class Point:
    """Represents a point in 2-D space.
    attributes: x, y
    """


def print_point(p):
    """Print a Point object in human-readable format."""
    print('({}, {}).'.format(p.x, p.y))


def distance_between_points(p1, p2):
    """Computes the distance between two Point objects.
    p1: Point
    p2: Point
    returns: float
    """
    x_diff = p2.x - p1.x
    y_diff = p2.y - p1.y
    distance = math.sqrt(x_diff**2 + y_diff ** 2)
    return distance


class Rectangle:
    """Represents a rectangle. 
    attributes: width, height, corner.
    """


def find_center(rect):
    """Returns a Point at the center of a Rectangle.
    rect: Rectangle
    returns: new Point
    """
    p = Point()
    p.x = rect.corner.x + rect.width / 2.0
    p.y = rect.corner.y + rect.height / 2.0
    return p


def grow_rectangle(rect, dwidth, dheight):
    """Modifies the Rectangle by adding to its width and height.
    rect: Rectangle object.
    dwidth: change in width (can be negative).
    dheight: change in height (can be negative).
    """
    rect.width += dwidth
    rect.height += dheight


def print_rectangle(rect):
    print('width:', rect.width, 'height:', rect.height)
    print('the lower-left corner:')
    print_point(rect.corner)
class Circle:
    """Represents circle
 
   attributes: center, radius
   """
 
def point_in_circle(circ, checkpoint):
    """Checks if point is within or on boundary of circle.
 
   circ: Circle object
   checkpoint: point object to be checked
   """
    import math
    return distance_between_points(circ.center, checkpoint) <= circ.radius
 
 
def rect_in_circle(circ, rect):
    """Checks if  rectangle lies entirely in or on boundary of  circle.
 
   circ: Circle object
   rect: Rectangle object
   """
    corner2 = Point()
    corner2 = get_corner(rect, 'botright')
    corner3 = Point()
    corner3 = get_corner(rect, 'topright')
    corner4 = Point()
    corner4 = get_corner(rect, 'topleft')
    return point_in_circle(circ, rect.corner) and point_in_circle(circ, corner2) and point_in_circle(circ, corner3) and point_in_circle(circ, corner4)
 
 
def rect_circle_overlap(circ, rect):
    """Checks if anyy corner of rectangle lies in or on boundary of a circle.
 
   circ: Circle object
   rect: Rectangle object
   """
    corner2 = Point()
    corner2 = get_corner(rect, 'botright')
    corner3 = Point()
    corner3 = get_corner(rect, 'topright')
    corner4 = Point()
    corner4 = get_corner(rect, 'topleft')
    return point_in_circle(circ, rect.corner) or point_in_circle(circ, corner2) or point_in_circle(circ, corner3) or point_in_circle(circ, corner4)
 
 
def main():
    my_point = Point()
    print(Point.__doc__)
    my_point.x = 3
    my_point.y = 4
    print('My point', end=' ')
    print_point(my_point)

    print('Is my_point an instance of Point?', isinstance(my_point, Point))
    print('Is my_point an instance of Rectangle?',
          isinstance(my_point, Rectangle))
    print('Does my_point have an attribute x?', hasattr(my_point, 'x'))
    print('Does my_point have an attribute z?', hasattr(my_point, 'z'))

    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0

    print('Does box have an attribute x?', hasattr(box, 'x'))

    print('Does box have an attribute corner?', hasattr(box, 'corner'))

    print('Rectangle has these:', dir(box))

    center = find_center(box)
    print('center', end=' ')
    print_point(center)

    print(box.width)
    print(box.height)
    print('grow')
    grow_rectangle(box, 50, 100)
    print(box.width)
    print(box.height)


if __name__ == '__main__':
    main() 
    
    
    # homework is is exc 2 in oop1, and try oop2 try the code not excersices 