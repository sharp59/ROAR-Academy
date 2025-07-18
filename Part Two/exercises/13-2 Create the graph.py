import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create x data points (e.g., 100 points from -10 to 10)
x = [1.0, 2.0, 3.0]
y = [2.0, 4.0, 1.0]

# Step 3: Plot y vs x
plt.xlim(1.0, 3.0)
plt.ylim(1.0, 4.0)

plt.plot(x, y, color = "blue")

# Step 4: Show the graph
plt.xlabel("x - axis")
plt.ylabel("y - axis")
plt.title("Sample graph")
plt.grid(False)
plt.show()
