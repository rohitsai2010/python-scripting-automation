import csv


data = [
    ['Name', 'Age'],
    ['riyaz', 23],
    ['tanisha', 26],
    ['anshuman', 21]
]

with open('people.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)


with open('people.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
