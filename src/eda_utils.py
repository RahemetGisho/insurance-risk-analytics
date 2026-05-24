import matplotlib.pyplot as plt
import seaborn as sns


def plot_histogram(df, column):
    plt.figure(figsize=(8, 5))
    sns.histplot(df[column], kde=True)
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()


def plot_boxplot(df, column):
    plt.figure(figsize=(8, 5))
    sns.boxplot(x=df[column])
    plt.title(f"Boxplot of {column}")
    plt.show()


def missing_values(df):
    return df.isnull().sum().sort_values(ascending=False)
