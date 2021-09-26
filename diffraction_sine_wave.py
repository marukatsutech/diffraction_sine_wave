# Diffraction (Sine wave); How does wavelength affect diffraction?
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches


def draw_slit():
    wall_height = 5.
    p_upper = slit_width / 2.
    p_lower = - wall_height - slit_width / 2.
    # Draw on ax1
    r_upper1 = patches.Rectangle(xy=(-0.2, p_upper), width=0.2, height=wall_height, fc='gray')
    ax1.add_patch(r_upper1)
    r_lower1 = patches.Rectangle(xy=(-0.2, p_lower), width=0.2, height=wall_height, fc='gray')
    ax1.add_patch(r_lower1)
    # Draw on ax2
    r_upper2 = patches.Rectangle(xy=(-0.2, p_upper), width=0.2, height=wall_height, fc='gray')
    ax2.add_patch(r_upper2)
    r_lower2 = patches.Rectangle(xy=(-0.2, p_lower), width=0.2, height=wall_height, fc='gray')
    ax2.add_patch(r_lower2)


def set_axis():
    # Set ax1
    ax1.set_xlim(x_min, x_max)
    ax1.set_ylim(y_min, y_max)
    ax1.set_title('k =' + str(k1))
    ax1.set_xlabel('x * pi')
    ax1.set_ylabel('y (Width of slit = 0.4)')
    ax1.grid()
    ax1.set_aspect("equal")
    # Set ax2
    ax2.set_xlim(x_min, x_max)
    ax2.set_ylim(y_min, y_max)
    ax2.set_title('k =' + str(k2))
    ax2.set_xlabel('x * pi')
    # ax2.set_ylabel('y')
    ax2.grid()
    ax2.set_aspect("equal")


def update(f):
    ax1.cla()  # Clear ax1
    ax2.cla()  # Clear ax1
    set_axis()

    # draw slit
    draw_slit()
    # draw arc
    radius1 = (2 + 0.5 / k1)    # 2PI + quarter length of wave(= 2 / 4)
    diameter1 = radius1 * 2
    a1 = patches.Arc(xy=(0, 0), width=diameter1, height=diameter1, angle=0, theta1=-90, theta2=-270, ec='gray', linestyle=':')
    ax1.add_patch(a1)
    radius2 = (2 + 0.5 / k2)
    diameter2 = radius2 * 2
    a2 = patches.Arc(xy=(0, 0), width=diameter2, height=diameter2, angle=0, theta1=-90, theta2=-270, ec='gray', linestyle=':')
    ax2.add_patch(a2)

    global theta, theta_step
    # Draw on ax1
    cos_theta = np.cos(theta)
    sin_theta = np.sin(theta)
    rot = np.array([[cos_theta, - sin_theta], [sin_theta, cos_theta]])  # Matrix of rotation
    rotated1 = np.dot(rot, sine_curve1)
    rotated_offset_plus1 = rotated1 + offset_plus
    rotated_offset_minus1 = rotated1 + offset_minus
    # ax1.plot(x, y, linestyle='-')
    # Draw 3 sine waves
    ax1.plot(rotated1[0], rotated1[1], linestyle='-')   # Draw center sine wave
    ax1.plot(rotated_offset_plus1[0], rotated_offset_plus1[1], linestyle='-')       # Draw upper sine wave
    ax1.plot(rotated_offset_minus1[0], rotated_offset_minus1[1], linestyle='-')     # Draw lower sine wave
    # Draw the center line of sine wave
    ax1.plot([0., 5. * math.cos(theta)], [0., 5. * math.sin(theta)], linestyle='-.', c='red')
    # Draw additional line and dot
    p01 = [radius1 * math.cos(theta), radius1 * math.sin(theta)]
    p11 = [radius1 * math.cos(theta) + math.cos(theta + math.pi / 2), radius1 * math.sin(theta) + math.sin(theta + math.pi / 2)]
    ax1.plot([p01[0], p11[0]], [p01[1], p11[1]], linestyle='-.', c='red')
    c = patches.Circle(xy=p01, radius=0.1, fc='red')
    ax1.add_patch(c)
    # Draw sum of 3 sine-values at arc-point
    sin_center1 = math.sin(k1 * radius1 * math.pi)
    sin_upper1 = math.sin(k1 * math.sqrt((radius1 * math.cos(theta) - 0.)**2 + (radius1 * math.sin(theta) - slit_width / 2)**2) * math.pi)
    sin_lower1 = math.sin(k1 * math.sqrt((radius1 * math.cos(theta) - 0.)**2 + (radius1 * math.sin(theta) + slit_width / 2)**2) * math.pi)
    ax1.text(x_min, y_max * 0.9, "           Sum at red dot=" + str(f'{sin_upper1 + sin_center1 + sin_lower1:.3f}'))

    # Draw on ax2
    rotated2 = np.dot(rot, sine_curve2)
    rotated_offset_plus2 = rotated2 + offset_plus
    rotated_offset_minus2 = rotated2 + offset_minus
    # ax2.plot(x, y, linestyle='-')
    # Draw 3 sine waves
    ax2.plot(rotated2[0], rotated2[1], linestyle='-')
    ax2.plot(rotated_offset_plus2[0], rotated_offset_plus2[1], linestyle='-')
    ax2.plot(rotated_offset_minus2[0], rotated_offset_minus2[1], linestyle='-')
    # Draw the center line of sine wave
    ax2.plot([0., 6. * math.cos(theta)], [0., 6. * math.sin(theta)], linestyle='-.', c='red')
    # Draw additional line and dot
    p02 = [radius2 * math.cos(theta), radius2 * math.sin(theta)]
    p12 = [radius2 * math.cos(theta) + math.cos(theta + math.pi / 2), radius2 * math.sin(theta) + math.sin(theta + math.pi / 2)]
    ax2.plot([p02[0], p12[0]], [p02[1], p12[1]], linestyle='-.', c='red')
    c = patches.Circle(xy=p02, radius=0.1, fc='red')
    ax2.add_patch(c)
    # Draw sum of 3 sine-values at arc
    sin_center2 = math.sin(k2 * radius2 * math.pi)
    sin_upper2 = math.sin(k2 * math.sqrt((radius2 * math.cos(theta) - 0.) ** 2 + (radius2 * math.sin(theta) - slit_width / 2) ** 2) * math.pi)
    sin_lower2 = math.sin(k2 * math.sqrt((radius2 * math.cos(theta) - 0.) ** 2 + (radius2 * math.sin(theta) + slit_width / 2) ** 2) * math.pi)
    ax2.text(x_min, y_max * 0.9, "           Sum at red dot=" + str(f'{sin_upper2 + sin_center2 + sin_lower2:.3f}'))

    theta = theta + theta_step
    if theta >= np.pi / 2. or theta <= - np.pi / 2.:
        theta_step = - theta_step


# Global variables
x_min = -1.
x_max = 4.
y_min = -4.
y_max = 4.

k1 = 1.
k2 = 3.
theta = 0.
theta_step = 0.01
slit_width = 0.4
offset_plus = np.vstack((np.zeros(500), np.full(500, slit_width / 2)))
offset_minus = np.vstack((np.zeros(500), np.full(500, -slit_width / 2)))

x = np.linspace(0, x_max * 2, 500)
y1 = np.sin(k1 * x * math.pi)  # Note: math.pi for adjustment x axis as x * pi
sine_curve1 = np.vstack((x, y1))
y2 = np.sin(k2 * x * math.pi)
sine_curve2 = np.vstack((x, y2))

# Generate figure and axes
fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

# Draw animation
set_axis()
anim = animation.FuncAnimation(fig, update, interval=200)
plt.show()
