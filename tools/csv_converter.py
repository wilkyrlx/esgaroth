import csv

filepath = "input-files\\"

input = open(filepath + 'World_Lakes.csv', 'r')
output = open(filepath + 'North_America_Lakes.csv', 'w', newline='')
writer = csv.writer(output)
for row in csv.reader(input):
    if row[3] == "United States of America" or row[3] == "Canada":
        writer.writerow(row)
input.close()
output.close()
