import math
from tkinter import *

root = Tk()
root.geometry("900x900")
root.title("2D Collision Simulator")
canvas = Canvas(root, width=600, height=452, bg="white")
canvas.pack()


def create_balls():
    global ball1, ball2
    ball1 = Balls(
        150 + (x_position1_slider.get() * 15),
        226 - (y_position1_slider.get() * 15),
        x_velo1_slider.get(),
        y_velo1_slider.get(),
        mass1_slider.get(),
        True,
        "blue"
    )

    ball2 = Balls(
        450 + (x_position2_slider.get() * 15),
        226 - (y_position2_slider.get() * 15),
        x_velo2_slider.get(),
        y_velo2_slider.get(),
        mass2_slider.get(),
        False,
        "red"
    )

started = False
slow_clicked = False
slowmo = 0
slow_id = 0
var1 = IntVar()
var2 = IntVar()
has_collided = False
time_count = 0
init_kinetic_energy = 0.0
change_kinetic_energy = 0.0


def start():
    global started
    started = True
    create_balls()


def begin():
    global has_collided, time_count
    mass1_slider.set(5)
    mass2_slider.set(5)
    x_velo1_slider.set(0)
    x_velo2_slider.set(0)
    y_velo1_slider.set(0)
    y_velo2_slider.set(0)
    x_position1_slider.set(0)
    x_position2_slider.set(0)
    y_position1_slider.set(0)
    y_position2_slider.set(0)
    var1.set(1)
    var2.set(0)
    has_collided = False
    time_count = 0


def restarted():
    global started, slow_clicked, slowmo, init_kinetic_energy, change_kinetic_energy

    started = False
    slow_clicked = False
    slowmo = 0
    init_kinetic_energy = 0.0
    change_kinetic_energy = 0.0
    create_balls()
    begin()


def slow():
    global slowmo, slow_clicked
    if not slow_clicked:
        slowmo = 100
        slow_clicked = True
    else:
        slowmo = 0
        slow_clicked = False
        canvas.delete(slow_id)


def elastic_check():
    if var1.get() == 1:
        var2.set(0)


def inelastic_check():
    if var2.get() == 1:
        var1.set(0)


def timer():
    global started, time_count
    canvas.create_text(500, 20, text=f"Time: {round(time_count,3)}", font=("Arial", 14, "bold"), fill="grey")
    if started:
        time_count += 0.03


def kinetic_energy():
    global has_collided, started, init_kinetic_energy, change_kinetic_energy
    if not started:
        velo1 = math.sqrt(ball1.x_velo ** 2 + ball1.y_velo ** 2)
        velo2 = math.sqrt(ball2.x_velo ** 2 + ball2.y_velo ** 2)
        init_kinetic_energy = ((ball1.mass*(velo1**2)) + (ball2.mass*(velo2**2)))/2
    canvas.create_text(120, 410, text=f"Initial Ek: {round(init_kinetic_energy,3)}J", font=("Arial", 14, "bold"), fill="grey")
    if has_collided:
        if var1.get() == 1:
            velof1 = math.sqrt(ball1.x_velo ** 2 + ball1.y_velo ** 2)
            velof2 = math.sqrt(ball2.x_velo ** 2 + ball2.y_velo ** 2)
            change_kinetic_energy = (((ball1.mass*(velof1**2)) + (ball2.mass*(velof2**2)))/2) - init_kinetic_energy
        else:
            velof_inelastic = math.sqrt(ball1.x_velo ** 2 + ball1.y_velo ** 2)
            change_kinetic_energy = (((ball1.mass + ball2.mass)*velof_inelastic**2)/2) - init_kinetic_energy
    canvas.create_text(120, 430, text=f"Change in Ek: {round(change_kinetic_energy,3)}J", font=("Arial", 14, "bold"), fill="grey")

start_button = Button(root, text="Start", width=10, command=start)
start_button.pack(pady=20)

restart_button = Button(root, text="Restart", width=10, command=restarted)
restart_button.pack(pady=20)

slow_button = Button(root, text="Slow On/Off", width=10, command=slow)
slow_button.pack(pady=20)

elastic_check_button = Checkbutton(root, text="Elastic", variable=var1, command=elastic_check)
inelastic_check_button = Checkbutton(root, text="Inelastic", variable=var2, command=inelastic_check)
elastic_check_button.pack(pady=20)
inelastic_check_button.pack(pady=20)

mass1_slider = Scale(root, from_=0.1, to=10, resolution=0.1, orient=HORIZONTAL, label="Mass of object 1 (kg):")
mass1_slider.place(x=100, y=470, width=200)

x_velo1_slider = Scale(root, from_=-10, to=10, resolution=0.1, orient=HORIZONTAL, label="x velocity of object 1 (m/s):")
x_velo1_slider.place(x=100, y=540, width=200)

y_velo1_slider = Scale(root, from_=-10, to=10, resolution=0.1, orient=HORIZONTAL, label="y velocity of object 1 (m/s):")
y_velo1_slider.place(x=100, y=610, width=200)

x_position1_slider = Scale(root, from_=-5, to=5, resolution=0.1, orient=HORIZONTAL, label="Horizontal position of object 1 (m):")
x_position1_slider.place(x=100, y=680, width=200)

y_position1_slider = Scale(root, from_=-10, to=10, resolution=0.1, orient=HORIZONTAL, label="Vertical position of object 1 (m):")
y_position1_slider.place(x=100, y=750, width=200)


mass2_slider = Scale(root, from_=0.1, to=10, resolution=0.1, orient=HORIZONTAL, label="Mass of object 2 (kg):")
mass2_slider.place(x=600, y=470, width=200)

x_velo2_slider = Scale(root, from_=-10, to=10, resolution=0.1, orient=HORIZONTAL, label="x velocity of object 2 (m/s):")
x_velo2_slider.place(x=600, y=540, width=200)

y_velo2_slider = Scale(root, from_=-10, to=10, resolution=0.1, orient=HORIZONTAL, label="y velocity of object 2 (m/s):")
y_velo2_slider.place(x=600, y=610, width=200)

x_position2_slider = Scale(root, from_=-5, to=5, resolution=0.1, orient=HORIZONTAL, label="Horizontal position of object 2 (m):")
x_position2_slider.place(x=600, y=680, width=200)

y_position2_slider = Scale(root, from_=-10, to=10, resolution=0.1, orient=HORIZONTAL, label="Vertical position of object 2 (m):")
y_position2_slider.place(x=600, y=750, width=200)

begin()

class Balls:
    def __init__(self, x, y, x_velo, y_velo, mass, is_ball1, colour):
        self.x = x
        self.y = y
        self.x_velo = x_velo
        self.y_velo = y_velo
        self.mass = mass
        self.is_ball1 = is_ball1
        self.colour = colour

    def draw(self):
        global started
        if started:
            self.x += self.x_velo*0.45
            self.y -= self.y_velo*0.45
        else:
            if self.is_ball1:
                self.mass = mass1_slider.get()
                self.x = 150 + (x_position1_slider.get() * 15)
                self.y = 226 - (y_position1_slider.get() * 15)
                self.x_velo = x_velo1_slider.get()
                self.y_velo = y_velo1_slider.get()
            else:
                self.mass = mass2_slider.get()
                self.x = 450 + (x_position2_slider.get() * 15)
                self.y = 226 - (y_position2_slider.get() * 15)
                self.x_velo = x_velo2_slider.get()
                self.y_velo = y_velo2_slider.get()

        radius = (math.sqrt(self.mass / math.pi)) * 24
        canvas.create_oval(
            self.x - radius, self.y - radius,
            self.x + radius, self.y + radius,
            fill="beige",
            outline=self.colour,
        )
        canvas.create_line(
            self.x,
            self.y,
            self.x+(self.x_velo*15),
            self.y - (self.y_velo*15),
            arrow=LAST, arrowshape=(20, 15, 6),
            fill=self.colour
        )
        if self.x_velo != 0 or self.y_velo != 0:
            velo = round(math.sqrt(self.x_velo**2 + self.y_velo**2),3)
            if self.y_velo < 0:
                buffer_x = 25
                buffer_y = -25
            else:
                buffer_x = 0
                buffer_y = 0
            canvas.create_text(self.x+(self.x_velo*15)+buffer_x, self.y-(self.y_velo*15)-15+buffer_y, text = f"|v| = {velo} m/s")



def check_collision(ball1, ball2):
    r1 = math.sqrt(ball1.mass / math.pi) * 24
    r2 = math.sqrt(ball2.mass / math.pi) * 24
    dx = ball2.x - ball1.x
    dy = ball2.y - ball1.y
    distance = math.sqrt(dx**2 + dy**2)
    return distance < r1 + r2


def update():
    global slow_id, has_collided
    canvas.delete("all")
    canvas.create_line(475 , 430, 490, 430, fill="grey", width=3)
    canvas.create_text(510 , 428, text="= 1m ", fill="grey")
    if slow_clicked:
        slow_id = canvas.create_text(90, 20, text="Slowed", font=("Arial", 14, "bold"), fill="grey")
    ball1.draw()
    ball2.draw()

    if not has_collided and check_collision(ball1, ball2):
        if var1.get() == 1:
            dx = ball2.x - ball1.x
            dy = ball2.y - ball1.y
            distance = math.sqrt(dx ** 2 + dy ** 2)
            nx = dx / distance
            ny = dy / distance
            v1n = (ball1.x_velo * nx) + (ball1.y_velo * ny)
            v2n = (ball2.x_velo * nx) + (ball2.y_velo * ny)
            v1n_final = (((ball1.mass - ball2.mass) * v1n) + (2 * ball2.mass * v2n)) / (ball1.mass + ball2.mass)
            v2n_final = (((ball2.mass - ball1.mass) * v2n) + (2 * ball1.mass * v1n)) / (ball1.mass + ball2.mass)
            ball1.x_velo += (v1n_final - v1n) * nx
            ball1.y_velo += (v1n_final - v1n) * ny
            ball2.x_velo += (v2n_final - v2n) * nx
            ball2.y_velo += (v2n_final - v2n) * ny
        else:
            ball1.x_velo = ((ball1.mass * ball1.x_velo) + (ball2.mass * ball2.x_velo)) / (ball1.mass + ball2.mass)
            ball2.x_velo = ball1.x_velo
            ball1.y_velo = ((ball1.mass * ball1.y_velo) + (ball2.mass * ball2.y_velo)) / (ball1.mass + ball2.mass)
            ball2.y_velo = ball1.y_velo
        has_collided = True
    if not check_collision(ball1, ball2):
        has_collided = False

    timer()
    kinetic_energy()

    root.after(30+slowmo, update)

create_balls()
update()
root.mainloop()
