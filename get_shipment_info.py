import csv

start_locations = []
end_locations = []

# Get shipments and put into lists for later use
with open('shipments.csv') as shipments_file:
    csv_reader = csv.reader(shipments_file, delimiter=',')
    top_line = True

    for row in csv_reader:
        if top_line:
            top_line = False
        else:
            start_locations.append(row[0])
            end_locations.append(row[1])

# Find the distances of each shipment
with open('distances.csv') as distances_file:
    csv_reader = csv.reader(distances_file, delimiter=',')
    top_line = True

    for row in csv_reader:
        if top_line:
            top_line = False
        else:
            if 'Omaha' in row[0] and 'Lincoln' in row[1]:
                print(row[2])
