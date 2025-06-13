# Lab Exercise - 7:
# Aim: Implement Simple Data Visualization using Matplotlib (Python Code using matplotlib)

# Import necessary libraries
import matplotlib.pyplot as plt

# Sample data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [10, 45, 50, 75]

# Line Plot
plt.figure(figsize=(8, 5))
plt.plot(categories, values, marker='o', markersize=7, color='blue', label='Line Plot')
plt.title('Line Plot Example', fontsize=13)
plt.xlabel('Categories', fontsize=12)
plt.ylabel('Values', fontsize=12)
plt.legend()
plt.grid(True)
plt.show()

# Bar Chart
plt.figure(figsize=(8, 5))
plt.bar(categories, values, color='r', alpha=0.7)
plt.title('Bar Chart Example', fontsize=13)
plt.xlabel('Categories', fontsize=12)
plt.ylabel('Values', fontsize=12)
plt.show()

# Scatter Plot
plt.figure(figsize=(8, 5))
plt.scatter(categories, values, color='blue', marker='o')
plt.title('Scatter Plot')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

# Pie Chart
plt.figure()
plt.pie(values, labels=categories, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()
