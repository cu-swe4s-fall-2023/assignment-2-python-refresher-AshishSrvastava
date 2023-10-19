import sys
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Check if the required arguments are provided
if len(sys.argv) != 6:
    print("Usage: python plot_time_series.py data_file out_file title x_label y_label")
    sys.exit(1)

data_file = sys.argv[1]
out_file = sys.argv[2]
title = sys.argv[3]
x_label = sys.argv[4]
y_label = sys.argv[5]

# Read the data from the input file
x_data = []  # X-axis data
y_data = []  # Y-axis data

with open(data_file, "r") as file:
    next(file)  # Skip the header line
    for line in file:
        x, y = line.strip().split(",")
        x_data.append(float(x))
        y_data.append(float(y))

# Create a time series plot
fig, ax = plt.subplots()
ax.plot(x_data, y_data, marker="o", linestyle="-")

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.set_xlabel(x_label)
ax.set_ylabel(y_label)
ax.set_title(title)

plt.savefig(out_file, bbox_inches="tight")
