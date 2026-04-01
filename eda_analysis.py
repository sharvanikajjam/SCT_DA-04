import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("----- Marketing Campaign EDA Started -----")

# Load dataset
df = pd.read_csv("marketing_campaign.csv")

print(df.head())

# Dataset info
print(df.info())

# Missing values
print(df.isnull().sum())

# Marketing Channel Distribution
plt.figure()
sns.countplot(x='Channel', data=df)
plt.title("Marketing Channel Distribution")
plt.show()

# ROI Analysis
plt.figure()
sns.barplot(x='Channel', y='ROI', data=df)
plt.title("ROI by Channel")
plt.show()

# Marketing Funnel
plt.figure()
sns.barplot(x='Stage', y='Count', data=df)
plt.title("Marketing Funnel")
plt.show()

print("EDA Completed Successfully")