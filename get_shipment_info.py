import csv

with open('shipments.csv') as shipments_file:
    csv_reader = csv.reader(shipments_file, delimiter=',')
    top_line = True

    for row in csv_reader:
        if top_line:
            top_line = False
        else:
            print(row[0])
            print(row[1])
