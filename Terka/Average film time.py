import csv

filename = "data/data.csv"
rows = []

with open(filename, 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    counter = 0
    sum = 0
    for row in csvreader:
        for i in row:
            if "min" in i[-3:] and i[0:2].isdigit():
                i = i.replace("min", "")
                counter += 1
                sum += int(i)
print("The result is:", sum /counter)

