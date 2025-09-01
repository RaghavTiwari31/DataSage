import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Example dataset (you can replace with your Excel data)
data = pd.DataFrame({
    "Experience": np.random.randint(1, 10, 50),
    "Salary": np.random.randint(30000, 80000, 50),
    "Projects": np.random.randint(1, 6, 50),
    "Hours_Worked": np.random.randint(30, 60, 50)
})

# Generate correlation matrix
corr = data.corr()

# Plot heatmap
plt.figure(figsize=(6, 5))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap of Dataset Attributes")
plt.show()
