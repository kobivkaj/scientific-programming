import csv
import imaplib
filename = "data/data.csv"
rows = []
def contains_item(string, items, count):
    counter = 0
    for item in items:
        if item in string:
            count[counter] += 1
        counter +=1


with open(filename, 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    labels = ["English","German" ,"French", "Spanish", "Italian"]
    sizes = [0,0,0,0,0]
    counter = 0
    sum = 0
    for row in csvreader:
        contains_item(row, labels ,sizes)
import matplotlib.pyplot as plt
plt.pie(sizes, labels=labels, autopct='%1.1f%%') 
plt.title('Language Distribution')
plt.show()
