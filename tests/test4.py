import numpy as np
import matplotlib.pyplot as plt

# A simple transformation
B = np.array([
    [2.0, 0.6, 0.3],
    [0.2, 1.3, -0.5],
    [0.0, 0.4, 1.8],
])

# SVD
U, S, Vt = np.linalg.svd(B)

S = S @ np.array([
    [1.5,0,0],
    [0,1.5,0],
    [0,0,1.5]
])

# Unit circle
theta = np.linspace(0, 2*np.pi, 400)
circle = np.vstack([np.cos(theta), np.sin(theta), np.zeros_like(theta)])

# Transformed ellipse
ellipse = B @ circle

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

ax.plot(circle[0], circle[1], circle[2], label='Unit circle (XY plane)')
ax.plot(ellipse[0], ellipse[1], ellipse[2], label='Transformed curve B @ circle')

origin = np.zeros(3)
for i in range(3):
    vec_in = Vt[i] * S[i]  # direction in input space scaled by singular value
    ax.quiver(origin[0], origin[1], origin[2],
              vec_in[0], vec_in[1], vec_in[2],
              length=1.0, normalize=False, label=f'Right SV {i+1} (scaled)')

# Optionally, show left singular vectors in output space (U) for comparison
# These indicate principal directions after applying B.
for i in range(3):
    vec_out = U[:, i] * S[i]
    ax.quiver(origin[0], origin[1], origin[2],
              vec_out[0], vec_out[1], vec_out[2],
              length=1.0, normalize=False, linestyle='dashed', label=f'Left SV {i+1} (scaled)')

# Make axes equal-ish
all_pts = np.hstack([circle, ellipse])
mins = all_pts.min(axis=1)
maxs = all_pts.max(axis=1)
ranges = maxs - mins
centers = (maxs + mins) / 2
max_range = ranges.max() * 0.6 + 1e-9

ax.set_xlim(centers[0] - max_range, centers[0] + max_range)
ax.set_ylim(centers[1] - max_range, centers[1] + max_range)
ax.set_zlim(centers[2] - max_range, centers[2] + max_range)
try:
    ax.set_box_aspect((1, 1, 1))
except Exception:
    pass

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D SVD Visualization: unit circle → transformed curve + singular vectors')
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1.0))
plt.tight_layout()
plt.show()
