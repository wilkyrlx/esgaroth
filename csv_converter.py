import csv

input = open('World_Lakes.csv', 'r')
output = open('Shortened.csv', 'w', newline='')
writer = csv.writer(output)
for row in csv.reader(input):
    if row[3] == "United States of America" or row[3] == "Canada":
        writer.writerow(row)
input.close()
output.close()
