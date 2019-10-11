import matplotlib.pyplot as plt
plt.switch_backend("agg")  # Switch to a non-interactive backend. Otherwise, the Flask app will crash.

import numpy as np
import mpld3


def build(n):
    # Somewhat based on mpld3 examples
    fig, ax = plt.subplots()

    scatter = ax.scatter(np.random.normal(size=n),
                        np.random.normal(size=n),
                        c=np.random.random(size=n),
                        s=1000 * np.random.random(size=n),
                        alpha=0.3,
                        cmap=plt.cm.jet)
    ax.grid(color='white', linestyle='solid')

    ax.set_title("Scatter Plot", size=20)
    return mpld3.fig_to_dict(fig)
