import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def angle_with_x_axis(self):
        return math.degrees(math.atan2(self.y, self.x))

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y

    def cross_product(self, other):
        return self.x * other.y - self.y * other.x

class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross_product(self, other):
        return Vector3D(self.y * other.z - self.z * other.y,
                        self.z * other.x - self.x * other.z,
                        self.x * other.y - self.y * other.x)


choice = input("Enter vector type (2D/3D): ").lower()
if choice == "2d":
    x1, y1 = map(float, input("Enter first 2D vector (x y): ").split())
    x2, y2 = map(float, input("Enter second 2D vector (x y): ").split())
    v1 = Vector2D(x1, y1)
    v2 = Vector2D(x2, y2)
elif choice == "3d":
    x1, y1, z1 = map(float, input("Enter first 3D vector (x y z): ").split())
    x2, y2, z2 = map(float, input("Enter second 3D vector (x y z): ").split())
    v1 = Vector3D(x1, y1, z1)
    v2 = Vector3D(x2, y2, z2)
else:
    print("Invalid choice")
    v1, v2 = None, None

if v1 and v2:
    print(f"Magnitude of first vector: {v1.magnitude()}")
    print(f"Magnitude of second vector: {v2.magnitude()}")
    print(f"Distance between vectors: {v1.distance(v2)}")
    print(f"Dot product: {v1.dot_product(v2)}")
    print(f"Cross product: {v1.cross_product(v2)}")