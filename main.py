import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# Dictionary containing attractor specific parameters for generating the plot
params = {
    'names': {
        1: "Lorenz",
        2: "Aizawa",
        3: "Bouali_Type_3",
        4: "Rossler",
        5: "Dadras",
        # 6: "Dequan_Li",
    },
    'recommendations': {
        1: "1, 1, 1",
        2: "1, 1, 1",
        3: "1, 1, 0",
        4: "0.1, 0, -0.1",
        5: "5, 0, -4",
        # 6: "0.01, 0, 0"
    },
    'steps': {
        1: 4000,
        2: 8000,
        3: 50000,
        4: 10000,
        5: 8000,
        # 6: 8000
    }
}

dt = 0.01

# Functions with constants for various strange attractors
def lorenz(x, y, z, dt):
    rho = 28.0
    sigma = 10.0
    beta = 8.0 / 3.0
    dx = sigma * (y - x) * dt
    dy = (x * (rho - z) - y) * dt
    dz = (x * y - beta * z) * dt
    return x + dx, y + dy, z + dz


def aizawa(x, y, z, dt):
    alpha = 0.95
    beta = 0.7
    gamma = 0.65
    delta = 3.5
    epsilon = 0.25
    zeta = 0.1
    dx = ((z - beta) * x - delta * y) * dt
    dy = (delta * x + (z - beta) * y) * dt
    dz = (gamma + alpha * z - (z * z * z / 3) - (x * x + y * y) * (1 + epsilon * z) + zeta * z * x * x * x) * dt
    return x + dx, y + dy, z + dz


def bouali_type_3(x, y, z, dt):
    gamma = 1
    mu = 0.001
    alpha = 3
    beta = 2.2
    dx = ((alpha * x * (1 - y)) - (beta * z)) * dt
    dy = ((-gamma) * y * (1 - (x * x))) * dt
    dz = (mu * x) * dt
    return x + dx, y + dy, z + dz


def rossler(x, y, z, dt):
    a = 0.2
    b = 0.2
    c = 5.7
    dx = (-(y + z)) * dt
    dy = (x + (a * y)) * dt
    dz = (b + z * (x - c)) * dt
    return x + dx, y + dy, z + dz


def dadras(x, y, z, dt):
    a = 3
    b = 2.7
    c = 1.7
    d = 2
    h = 9
    dx = (y - (a * x) + (b * y * z)) * dt
    dy = ((c * y) - (x * z) + z) * dt
    dz = ((d * x * y) - (h * z)) * dt
    return x + dx, y + dy, z + dz

'''
# Can't figure out initial conditions for Dequan Li so its still WIP
def dequan_li(x, y, z, dt):
    a = 40.0
    c = 1.833
    d = 0.16
    e = 0.65
    k = 55.0
    f = 20.0
    dx = (a * (y - x) + d * x * z) * dt
    dy = ((k * x) + (f * y) - (x * z)) * dt
    dz = ((c * z) + (x * y) - (e * x * x)) * dt
    return x + dx, y + dy, z + dz
'''

# Generates plot coordinates and the 3D plot
def attractor_processing(attractor_num):
    global view

    # To exit program
    if attractor_num == 6:
        view = False

    elif attractor_num in [1,2,3,4,5]:

        x, y, z = [], [], []
        coords = []

        numTraj = int(input("Enter the number of trajectories: "))

        for i in range(numTraj):
            print(f"Around {params['recommendations'][attractor_num]} is recommended")
            a, b, c = input("Enter a comma-separated initial position: ").split(',')
            x.append(float(a.strip()))
            y.append(float(b.strip()))
            z.append(float(c.strip()))

        for i in range(numTraj):
            print("Initial position: (x, y, z) = (%.2f, %.2f, %.2f)" % (x[i], y[i], z[i]))


        attractor = (params['names'][attractor_num]).lower()
        var = globals()[attractor]
        pointnum = params['steps'][attractor_num]

        # Creating empty arrays [size: number of plot points * 3 (for each of the x,y,z coordinates)] to store coordinates of each Trajectory
        for i in range(numTraj):
            coords.append(np.zeros((pointnum, 3)))

        # Generating coordinates
        for i in range(numTraj):
            for j in range(pointnum):
                x[i], y[i], z[i] = var(x[i], y[i], z[i], dt)
                coords[i][j] = x[i], y[i], z[i]

        # Setting up 3D scene
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.set_xlabel("X Axis")
        ax.set_ylabel("Y Axis")
        ax.set_zlabel("Z Axis")
        ax.set_title("%s Attractor" % (attractor.title()))

        # Plotting attractor
        for i in range(numTraj):
            ax.plot(coords[i][:, 0], coords[i][:, 1], coords[i][:, 2], label="Trajectory %d" % (i + 1))
            plt.draw()

        # Displaying plot
        plt.legend()
        plt.show()

        print()

    else:
        print("Invalid input. Try again.")


# Input Loop
view = True
while view:
    # Printing Attractors
    for key in params['names']:
        print(f"{key}: {params['names'][key]}")
        
    attractor_num = int(input("Enter among 1-5 for the strange attractor you want to view or 'off' to terminate program: "))
    attractor_processing(attractor_num)

    continue



