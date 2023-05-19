import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-10, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
fig, axs = plt.subplots(3, figsize=(8, 8))
axs[0].plot(x, y1, color='blue', linewidth=2)
axs[0].set_title('Sine Wave')
axs[1].plot(x, y2, color='red', linewidth=2)
axs[1].set_title('Cosine Wave')
axs[2].plot(x, y3, color='green', linewidth=2)
axs[2].set_title('Tangent Wave')
for ax in axs.flat:
    ax.set(xlabel='x-axis', ylabel='y-axis')
fig.suptitle('Trigonometric Waves', fontsize=16)
plt.show()
