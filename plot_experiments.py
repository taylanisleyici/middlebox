import pandas as pd
import matplotlib.pyplot as plt

# Read data
data = pd.read_csv('experiment.txt', header=None, names=['delay', 'rtt'], sep=',\s*')

# Create figure
plt.figure(figsize=(10, 6))

# Plot with log scale on x-axis
plt.semilogx(data['delay'], data['rtt'], 'bo-')

# Customize plot
plt.grid(True)
plt.xlabel('Mean Delay (s)')
plt.ylabel('Round Trip Time (ms)')
plt.title('Network Latency vs Artificial Delay')

# Add points and values
for x, y in zip(data['delay'], data['rtt']):
    plt.annotate(f'{y:.1f}ms', 
                (x, y),
                xytext=(5, 5),
                textcoords='offset points')

# Adjust layout and save
plt.tight_layout()
plt.savefig('experiment_results.png', dpi=300, bbox_inches='tight')
plt.close()