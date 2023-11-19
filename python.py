import csv
import math

def read_file(filename):
    with open(filename, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=';')
        fields = csvreader.fieldnames
        rows = list(csvreader)
        print("Total ROWS:", len(rows))
        return fields, rows

def first_number(data):
    num_counts = {str(i): 0 for i in range(1, 10)}

    for row in data:
        value = row["value"]
        first_num = str(value)[0]

        if first_num in num_counts:
            num_counts[first_num] += 1

    for num, count in num_counts.items():
        print(f"{num}: {count}x ({math.floor(count / (len(rows)) * 100)}%)")

filename = "transactions.csv"
fields, rows = read_file(filename)

first_number(rows)
