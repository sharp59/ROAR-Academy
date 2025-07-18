## This is course material for Introduction to Python Scientific Programming
## Example code: matplotlib_clock.py
## Author: Allen Y. Yang
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

from datetime import datetime, timezone
import matplotlib.pyplot as plt
import os
import numpy as np

# Initialization, define some constant

second_hand_length = 200
second_hand_width = 2
minute_hand_length = 150
minute_hand_width = 6
hour_hand_length = 100
hour_hand_width = 10
center = np.array([256, 256])

def clock_hand_vector(angle, length):
    return np.array([length * np.sin(angle), -length * np.cos(angle)])

# draw an image background
fig, ax = plt.subplots()

ax.set_xlim(0, 512)
ax.set_ylim(0, 512)
ax.set_aspect('equal')  # Keep the aspect ratio square
ax.axis('off')

while True:
    # First retrieve the time
    now_time = datetime.now()
    hour = now_time.hour
    if hour>12: hour = hour - 12
    minute = now_time.minute
    second = now_time.second

    # Calculate end points of hour, minute, second

    gmt_time = gmt_time = datetime.now(timezone.utc)

    gmt_vector = clock_hand_vector(((gmt_time.hour + gmt_time.minute / 60 + gmt_time.second / 3600))/ 24 * 2 * np.pi, 150)
    hour_vector = clock_hand_vector((hour + minute / 60 + second / 3600)/12*2*np.pi, hour_hand_length)
    minute_vector = clock_hand_vector((minute + second / 60)/60*2*np.pi, minute_hand_length)
    second_vector = clock_hand_vector(second/60*2*np.pi, second_hand_length)

    plt.arrow(center[0], center[1], hour_vector[0], hour_vector[1], head_length = 3, linewidth = hour_hand_width, color = 'black')
    plt.arrow(center[0], center[1], minute_vector[0], minute_vector[1], linewidth = minute_hand_width, color = 'black')
    plt.arrow(center[0], center[1], second_vector[0], second_vector[1], linewidth = second_hand_width, color = 'red')
    plt.arrow(center[0], center[1], gmt_vector[0], gmt_vector[1], linewidth = 5, color = 'yellow')

    plt.pause(0.03)
    ax.cla()
    ax.set_xlim(0, 512)
    ax.set_ylim(0, 512)
    ax.set_aspect('equal')
    ax.axis('off')