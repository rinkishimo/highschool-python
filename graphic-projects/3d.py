import tkinter, math, random

class Modeler3d:
    def __init__(self, cnv, zoom=1, distance=500):
        self.cnv = cnv
        self.zoom = zoom
        self.distance = distance
    
    def width_half(self):
        return self.cnv.winfo_width() / 2

    def height_half(self):
        return self.cnv.winfo_height() / 3

    def __str__(self):
        return f'w/2 = {self.cnv_width_half()}, h/2 = {self.cnv_height_half()}, distance = {distance}, zoom = {self.zoom}'

    def flattenPoint(self, point3d):
        (x, y, z) = (point3d[0], point3d[1], point3d[2])
        projectedY = int(self.height_half() - ((y * self.distance) / (z + self.distance)) * self.zoom)
        projectedX = int(self.width_half() + ((x * self.distance) / (z + self.distance)) * self.zoom)
        return (projectedX, projectedY)

    def get_2d_points(self, points3d):
        points2d = []
        for point in points3d:
            points2d.append(self.flattenPoint(point))
        return points2d

    def draw(self, object3d):
        body2d = self.get_2d_points(object3d.points)
        self.cnv.delete(object3d.name)
        for ciara in object3d.lines:
            self.cnv.create_line(body2d[ciara[0]], body2d[ciara[1]], tag=object3d.name, width=2)
        self.cnv.update()
        return self
    
    def wait(self, miliseconds):
        self.cnv.after(miliseconds)

class Object3d:
    def __init__(self, name, points, lines, r=None):
        self.name = name
        self.points = points
        self.lines = lines
        self.r = r if r != None else self.count_ref_point()

    def enlarge_coords(self, x_ratio, y_ratio, z_ratio):
        new_points = []
        for point in self.points:
            new_point = (point[0] * x_ratio, point[1] * y_ratio, point[2] * z_ratio)
            new_points.append(new_point)
        self.points = new_points
        self.r = (self.r[0]* x_ratio, self.r[1] * y_ratio, self.r[2] * z_ratio)
        #self.update_ref_point()
        return self

    def move(self, delta_x=0, delta_y=0, delta_z=0):
        new_points = []
        for point in self.points:
            new_point = (point[0] + delta_x, point[1] + delta_y, point[2] + delta_z)
            new_points.append(new_point)
        self.points = new_points
        self.r = (self.r[0] + delta_x, self.r[1] + delta_y, self.r[2] + delta_z)
        #self.update_ref_point()
        return self

    def move_to(self, x, y, z):
        #self.move(x - self.ref_point[0], y - self.ref_point[1], z - self.ref_point[2])
        self.move(x - self.r[0], y - self.r[1], z - self.r[2])
        self.r = (x, y, z)
        return self

    def _sin_cos(self, angle):
        c = math.cos(math.radians(angle))
        s = math.sin(math.radians(angle))
        return s, c

    def _rotate_point(self, px, py, cx, cy, sin, cos):
        return (cos * (px - cx) - sin * (py - cy) + cx, 
                sin * (px - cx) + cos * (py - cy) + cy)

    def rotate(self, x_deg=0, y_deg=0, z_deg=0):
        rx, ry, rz = self.r
        if (x_deg != 0):
            sin, cos = self._sin_cos(x_deg)
            new_points = []
            for point in self.points:
                ny, nz = self._rotate_point(point[1], point[2], ry, rz, sin, cos)
                new_point = (point[0], ny, nz)
                new_points.append(new_point)
            self.points = new_points
        if (y_deg != 0):
            sin, cos = self._sin_cos(y_deg)
            new_points = []
            for point in self.points:
                nx, nz = self._rotate_point(point[0], point[2], rx, rz, sin, cos)
                new_point = (nx, point[1], nz)
                new_points.append(new_point)
            self.points = new_points
        if (z_deg != 0):
            sin, cos = self._sin_cos(z_deg)
            new_points = []
            for point in self.points:
                nx, ny = self._rotate_point(point[0], point[1], rx, ry, sin, cos)
                new_point = (nx, ny, point[2])
                new_points.append(new_point)
            self.points = new_points

        #self.update_ref_point()
        return self



    def count_ref_point(self):
        x, y, z = 0, 0, 0
        for point in self.points:
            x += point[0]
            y += point[1]
            z += point[2]
        cnt = len(self.points)
        return (x / cnt, y / cnt, z / cnt)



canvas = tkinter.Canvas(width=720, height=500)
canvas.pack(fill="both", expand=True)
canvas.update()

print(canvas.winfo_width(), canvas.winfo_height())

modeler = Modeler3d(canvas)

# body = [(0,4,0), (0,4,2), (3,4,2), (3,4,0), (0,0,2), (3,0,2), (3,0,0)]
# ciary = [(0,1), (1,2), (2,3), (3,0), (4,5), (5,6), (6,4), (0,4), (0,6), (1,4), (2,5), (3,6)]

body = [(-3,-3,-3), (3,-3,-3), (3,-3,3), (-3,-3,3),
        (-3,3,-3), (2,3,-3), (3,2,-3), (3,3,-2),
        (3,3,3), (-3,3,3)]
ciary = [(0,1), (0,3), (0,4), (1,2), (1,6), (2,3), (2,8), (3,9), 
        (4,5), (4,9), (5,6), (5,7), (6,7), (7,8), (8,9)]


hranol = Object3d('hranol', body, ciary) #, r=(0,0,0))
hranol.enlarge_coords(30, 30, 30).move_to(0, -150, 0)

modeler.draw(hranol).wait(2000)
step_time = 75

for i in range(30):
    hranol.move(delta_x=-10)
    modeler.draw(hranol).wait(step_time)

for i in range(20):
    hranol.move(delta_y=10)
    modeler.draw(hranol).wait(step_time)

for i in range(30):
    hranol.move(delta_z=20)
    modeler.draw(hranol).wait(step_time)

for i in range(20):
    hranol.move(delta_y=-10)
    modeler.draw(hranol).wait(step_time)

for i in range(30):
    hranol.move(delta_z=-20)
    modeler.draw(hranol).wait(step_time)

for i in range(30):
    hranol.move(delta_x=10)
    modeler.draw(hranol).wait(step_time)

for y in range(40 * 2):
        hranol.rotate(y_deg=-9)
        modeler.draw(hranol).wait(step_time)



while True:
    use = random.choice([(1, 0, 0), (0, 1, 0), (0, 0, 1)])
    spin = random.choice([-9, 9])
    xa, ya, za = use[0] * spin, use[1] * spin, use[2] * spin
    steps = random.randrange(3) + 2

    for i in range(steps * 10):
        hranol.rotate(x_deg=xa, y_deg=ya, z_deg=za)
        modeler.draw(hranol).wait(step_time)

    zd = random.choice([5])
    for i in range(5):
        hranol.move(delta_z=zd)
        modeler.draw(hranol).wait(step_time)

    print(hranol.r)


canvas.mainloop()