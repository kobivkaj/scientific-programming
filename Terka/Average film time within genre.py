import csv
from pickle import NONE
filename = "data/data.csv"
rows = []

def contains_item(string, items, size, time_sum):
    counter = 0
    for item in items:
        if item in string:
            size[counter] += 1
            time_sum[counter] += time(string)
        counter +=1

def time(row):
    for i in row:
        if isinstance(i, str) and "min" in i[-3:] and i[0:2].isdigit():
            i = i.replace("min", "")
            i = int(i)
            return i
    return 0
def average(list1, list2):
    for i in range(len(list1)):
        list1[i] = round(list1[i] / list2[i])
    return list1

with open(filename, 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    labels = ["Drama","Comedy" ,"Documentary", "Action", "Thriller", "Animation", "Adventure", "Horror", "Family", "Romantic Comedy", "Crime", "Romantic", "Sci-Fi", "Biographical", "Fantasy", "Erotic", "Musical"]
    sizes = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    time_sum = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    counter = 0
    sum = 0
    for row in csvreader:
        contains_item(row, labels ,sizes, time_sum)
average = average(time_sum, sizes)
sorted_data = sorted(zip(labels, average), key=lambda x: x[1], reverse=False)
categories, values = zip(*sorted_data)

for i in range(len(sizes)):
    print(f'{categories[i]} == {values[i]}')
    
import matplotlib.pyplot as plt
import numpy as np
# Create a figure and axis
fig, ax = plt.subplots()

# Create the bar chart
bars = ax.barh(np.arange(len(categories)), values)

# Set the y-axis ticks and labels
ax.set_yticks(np.arange(len(categories)))
ax.set_yticklabels(categories)

# Add labels to the bars
for i, bar in enumerate(bars):
    ax.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, values[i],
            ha='left', va='center')

# Set labels and title
ax.set_xlabel('Time')
ax.set_ylabel('Categories')
ax.set_title('Average film time within the genre')

# Display the chart
plt.show()
