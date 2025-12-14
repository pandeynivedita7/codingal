import seaborn as sns          # Parent library for heatmaps
import matplotlib.pyplot as plt
import pandas as pd            # Library to load CSV files

# Load your local Iris.csv file
df = pd.read_csv("C:/Users/swapni/Downloads/codingal/CodingalGit/codingal/Python/Iris.csv")
# Compute correlation matrix
corr = df.corr(numeric_only=True)

# Plot heatmap
plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Heatmap of Iris Dataset Correlation")
plt.show()
