import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('data2.txt', delimiter=',')

print(f"Mean: {np.mean(data):.2f}, Median: {np.median(data):.2f}, Min: {np.min(data):.2f}, Max: {np.max(data):.2f}")

bins = max(data)-min(data)
bins = int(bins)
plt.hist(data, bins, color='skyblue', edgecolor='black')
plt.xlabel('Time (s)')
plt.ylabel('Frequency')
plt.title('Distribution of Time; 100 Iterations')
plt.savefig("MoveHistogram.png")
plt.show()
