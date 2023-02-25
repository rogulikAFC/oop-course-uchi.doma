class Point2D:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def get_distance(self):
        x_dist = 0 + self.x
        y_dist = 0 + self.y

        return int(round((x_dist * x_dist + y_dist * y_dist)**0.5, 0))

    def get_info(self):
        coords = [self.x, self.y]
        coords_str = ', '.join(str(n) for n in coords)

        return f'Точка с координатами ({coords_str})'


class Point3D:
    def __init__(self, x, y, z):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)

    def get_distance(self):
        x_dist = self.x
        y_dist = self.y
        z_dist = self.z

        return int(round((x_dist**2 + y_dist**2 + z_dist**2)**0.5, 0))

    def get_info(self):
        cords = [self.x, self.y, self.z]
        cords_str = ', '.join(str(n) for n in cords)

        return f'Точка с координатами ({cords_str})'


point_type = input('type: ')
# point_type = 'Point3D'
cords = input('cords: ').split()

point = None

if point_type == 'Point2D':
    point = Point2D(cords[0], cords[1])

elif point_type == 'Point3D':
    point = Point3D(cords[0], cords[1], cords[2])

print(point.get_distance())
print(point.get_info())
