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

# Get distances of each shipment
with open('distances.csv') as distances_file:
    distances_csv_reader = csv.reader(distances_file, delimiter=',')
    top_line = True

    route_stretches_index = 0
    for row in distances_csv_reader:
        if top_line:
            top_line = False
        else:
            if start_locations[route_stretches_index] in row[0] and end_locations[route_stretches_index] in row[1]:
                print(row[0], 'to', row[1], 'is', row[2], 'miles')
                route_stretches_index += 1
