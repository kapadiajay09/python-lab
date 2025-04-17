import math


def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2 + (point1[2] - point2[2])**2)



def input_coordinates():
    x_coords = [float(input(f"Enter x coordinate for point {i+1}: ")) for i in range(10)]
    y_coords = [float(input(f"Enter y coordinate for point {i+1}: ")) for i in range(10)]
    z_coords = [float(input(f"Enter z coordinate for point {i+1}: ")) for i in range(10)]
    return list(zip(x_coords, y_coords, z_coords))


points = input_coordinates()


nearest_neighbors = []

for i, point in enumerate(points):
    min_distance = float('inf')
    nearest_neighbor = None
    for j, other_point in enumerate(points):
        if i != j:
            dist = distance(point, other_point)
            if dist < min_distance:
                min_distance = dist
                nearest_neighbor = other_point
    nearest_neighbors.append((point, nearest_neighbor))

# Display the result
for point, neighbor in nearest_neighbors:
    print(f"Point: {point}, Nearest Neighbor: {neighbor}")