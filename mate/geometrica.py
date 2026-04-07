import math


def distance(x1, y1, x2, y2):
    """Calculate distance between two points."""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def midpoint(x1, y1, x2, y2):
    """Calculate midpoint between two points."""
    return ((x1 + x2) / 2, (y1 + y2) / 2)


def circle_area(radius):
    """Calculate area of a circle."""
    return math.pi * radius ** 2


def circle_perimeter(radius):
    """Calculate perimeter (circumference) of a circle."""
    return 2 * math.pi * radius


def rectangle_area(width, height):
    """Calculate area of a rectangle."""
    return width * height


def rectangle_perimeter(width, height):
    """Calculate perimeter of a rectangle."""
    return 2 * (width + height)


def triangle_area(base, height):
    """Calculate area of a triangle."""
    return (base * height) / 2


def triangle_perimeter(a, b, c):
    """Calculate perimeter of a triangle."""
    return a + b + c


def triangle_area_heron(a, b, c):
    """Calculate area of a triangle using Heron's formula."""
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def sphere_volume(radius):
    """Calculate volume of a sphere."""
    return (4 / 3) * math.pi * radius ** 3


def sphere_surface_area(radius):
    """Calculate surface area of a sphere."""
    return 4 * math.pi * radius ** 2


def cylinder_volume(radius, height):
    """Calculate volume of a cylinder."""
    return math.pi * radius ** 2 * height


def cylinder_surface_area(radius, height):
    """Calculate surface area of a cylinder."""
    return 2 * math.pi * radius * (radius + height)


def polygon_area(vertices):
    """Calculate area of a polygon using the shoelace formula.
    vertices: list of (x, y) tuples in order."""
    n = len(vertices)
    if n < 3:
        return 0
    area = 0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2


def angle_between_vectors(v1, v2):
    """Calculate angle between two vectors in radians."""
    dot_product = v1[0] * v2[0] + v1[1] * v2[1]
    magnitude1 = math.sqrt(v1[0] ** 2 + v1[1] ** 2)
    magnitude2 = math.sqrt(v2[0] ** 2 + v2[1] ** 2)
    cos_angle = dot_product / (magnitude1 * magnitude2)
    return math.acos(cos_angle)
