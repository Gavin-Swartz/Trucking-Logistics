import csv

start_locations = []
end_locations = []

with open('shipments.csv') as shipments_file:
    csv_reader = csv.reader(shipments_file, delimiter=',')
    top_line = True

    for row in csv_reader:
        if top_line:
            top_line = False
        else:
            start_locations.append(row[0])
            end_locations.append(row[1])
