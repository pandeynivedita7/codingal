import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Iris.csv")

# Remove Id column if present
if "Id" in df.columns:
    df = df.drop(columns=["Id"])
sns.jointplot(
    data=df,
    x="SepalLengthCm",
    y="SepalWidthCm",
    kind="scatter"#scatter plot
)
plt.show()
sns.jointplot(
    data=df,
    x="PetalLengthCm",
    y="PetalWidthCm",
    kind="kde",#KDE reveals data concentration using contour shading.
    fill=True
)
sns.jointplot(
    data=df,
    x="SepalLengthCm",
    y="PetalLengthCm",
    kind="hex"#Hexagonal bins show dense regions clearly.
)
sns.jointplot(
    data=df,
    x="PetalLengthCm",
    y="PetalWidthCm",
    kind="reg"#Regression line with scatter points
)
plt.show()
sns.jointplot(
    data=df,
    x="PetalLengthCm",
    y="PetalWidthCm",
    hue="Species",
    kind="kde",
    fill=True
)
plt.show()

