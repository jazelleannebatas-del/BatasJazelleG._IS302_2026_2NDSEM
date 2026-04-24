import math

class Shape_jab:
    def area_jab(self_jab):
        pass  # Placeholder for polymorphism

class Rectangle_jab(Shape_jab):
    def __init__(self_jab, width_jab, height_jab):
        self_jab.width_jab = width_jab
        self_jab.height_jab = height_jab

    def area_jab(self_jab):
        return self_jab.width_jab * self_jab.height_jab

class Circle_jab(Shape_jab):
    def __init__(self_jab, radius_jab):
        self_jab.radius_jab = radius_jab

    def area_jab(self_jab):
        return math.pi * self_jab.radius_jab** 2

class Triangle_jab(Shape_jab):
    def __init__(self_jab, base_jab, height_jab):
        self_jab.base_jab = base_jab
        self_jab.height_jab = height_jab

    def area_jab(self_jab):
        return 0.5 * self_jab.base_jab * self_jab.height_jab

# Example usage
rectangle_jab = Rectangle_jab(10, 5)
circle_jab = Circle_jab(5)
triangle_jab = Triangle_jab(8, 6)

print(f"Rectangle Area: {rectangle_jab.area_jab()}")
print(f"Circle Area: {circle_jab.area_jab():.1f}")
print(f"Triangle Area: {triangle_jab.area_jab()}")
