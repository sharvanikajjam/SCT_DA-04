# 📊 Task 04: Data Visualization

## 📌 Objective

The objective of this task is to visualize the dataset using graphs and charts to understand patterns, trends, and relationships in the data.

---

## 🛠️ Tools Used

* Python 🐍
* Pandas
* Matplotlib
* Visual Studio Code (VS Code)

---

## 📂 Dataset

* Dataset used: **Global Superstore Dataset**
* Cleaned dataset from Task 02

---

## 🚀 Steps Performed

### 1. Import Libraries

Imported required libraries such as Pandas and Matplotlib.

### 2. Load Dataset

Loaded the cleaned dataset using `read_csv()`.

### 3. Data Preparation

* Checked column names
* Selected important columns for visualization

### 4. Create Visualizations

* 📈 **Line Chart** – Sales over time
* 📊 **Bar Chart** – Sales by Category
* 🥧 **Pie Chart** – Sales distribution by Region
* 📉 **Histogram** – Distribution of Sales

### 5. Customize Graphs

* Added titles
* Labeled axes
* Improved readability

---

## 💻 Code

```python id="6skk1u"
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Cleaned_Data.csv")

# Line chart (Sales over time)
df['Order Date'] = pd.to_datetime(df['Order Date'])
df.groupby('Order Date')['Sales'].sum().plot()
plt.title("Sales Over Time")
plt.show()

# Bar chart (Sales by Category)
df.groupby('Category')['Sales'].sum().plot(kind='bar')
plt.title("Sales by Category")
plt.show()

# Pie chart (Sales by Region)
df.groupby('Region')['Sales'].sum().plot(kind='pie', autopct='%1.1f%%')
plt.title("Sales by Region")
plt.show()

# Histogram (Sales distribution)
df['Sales'].plot(kind='hist')
plt.title("Sales Distribution")
plt.show()
```

---

## ▶️ How to Run (VS Code)

1. Open project folder in VS Code
2. Ensure `Cleaned_Data.csv` is present
3. Create a Python file (e.g., `task04.py`)
4. Paste the code
5. Run using terminal:

```
python task04.py
```

---

## 📊 Output

* Line chart showing sales trend
* Bar chart for category-wise sales
* Pie chart for regional sales distribution
* Histogram showing sales distribution

---

## 📌 Conclusion

Data visualization helps in understanding trends and patterns easily. In this task, we created different types of charts to analyze the dataset effectively.

---

## 🙌 Author

* Your Name
Sharvani Kajjam
