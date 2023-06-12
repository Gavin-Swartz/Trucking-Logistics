import csv

start_locations = []
end_locations = []

# Get shipments and put into lists for later use
with open('shipments.csv') as shipments_file:
    csv_reader = csv.reader(shipments_file, delimiter=',')
    top_line = True

    for rows in csv_reader:
        if top_line:
            top_line = False
        else:
            start_locations.append(rows[0])
            end_locations.append(rows[1])

# Get distances of each shipment
top_line = True
route_stretches_index = 0  # Increases to match index of the route stretch
while route_stretches_index < len(start_locations):
    for routes in start_locations:
        with open('distances.csv') as distances_file:
            distances_csv_reader = csv.reader(distances_file, delimiter=',')
            for rows in distances_csv_reader:
                if top_line:
                    top_line = False
                elif start_locations[route_stretches_index] in rows[0] and end_locations[route_stretches_index] in \
                        rows[1]:
                    print(rows[0], 'to', rows[1], 'is', rows[2], 'miles')
                    route_stretches_index += 1
                    break
