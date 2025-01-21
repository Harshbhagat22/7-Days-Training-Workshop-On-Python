from sklearn.datasets import make_circles
import matplotlib.pyplot as plt

# Generate synthetic data with make_circles
x, y = make_circles(n_samples=200, noise=0.1, shuffle=True, random_state=42)

# Plot the generated data
plt.scatter(x[:, 0], x[:, 1])
plt.show()
