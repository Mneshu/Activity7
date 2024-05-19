import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns


data_read=pd.read_csv("C:/Users/Sfundesihle/Desktop/test/dataset - 2020-09-24.csv")

sns.set_theme()

sns.set_style("whitegrid")

sns.set_style("whitegrid")


sns.lineplot(x='Clean sheets', y='Saves', data=data_read)
plt.show()


sns.set_context("talk")
sns.lineplot(x='Clean sheets', y='Saves', data=data_read)
plt.show()

sns.kdeplot(data=data_read['Wins'],
shade=True)

sns.rugplot(data_read['Wins'])


sns.boxplot(x='Club', y='Wins', data=data_read)

sns.violinplot(x='Club', y='Losses', data=data_read)

sns.swarmplot(x='Losses', y='Wins', data=data_read)

sns.pairplot(data_read, hue='Appearances')

sns.jointplot(x='Wins', y='Appearances', data=data_read,
kind='scatter')