"""
Simple Example
==============

Simple example using the alpha shape toolbox

"""
import alphashape
import matplotlib.pyplot as plt
from descartes import PolygonPatch

# Define input points
points = [(0., 0.), (0., 1.), (1., 1.), (1., 0.),
          (0.5, 0.25), (0.5, 1.), (0.25, 0.5), (0.8, 0.6)]

# Determine the optimized alpha parameter
alpha = alphashape.optimizealpha(points)

# # Generate the alpha shape
alpha_shape = alphashape.alphashape(points, alpha)

# # Initialize plot
fig, ax = plt.subplots()

# # Plot input points
ax.scatter(*zip(*points))

# # Plot alpha shape
ax.add_patch(PolygonPatch(alpha_shape, alpha=.2))

plt.show()