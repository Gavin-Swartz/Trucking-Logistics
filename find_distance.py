from geopy.distance import geodesic
import csv

# Lists for storing data
location_name = []
location_lat = []
location_long = []


# Get information from locations.csv
with open('locations.csv') as locations_file:
    csv_reader = csv.reader(locations_file, delimiter=',')
    top_line = True
    for row in csv_reader:
        if top_line:
            top_line = False
        else:
            location_name.append(row[0])
            location_lat.append(row[2])
            location_long.append(row[3])


# Combine latitude and longitude into one string for each location
location_coordinates = []
index = 0
for location in location_lat:
    coordinates = location_lat[index], location_long[index]
    location_coordinates.append(', '.join(coordinates))
    index += 1


location_information = []
location_index = 0
for location in location_name:
    info = [location_name[location_index], location_coordinates[location_index]]
    location_information.append(info)
    location_index += 1


# Get distance from geodesic
start = ['Starting Location']
end = ['Ending Location']
distance = ['Distance']


# Calculate distances and put into lists of data
for starting_location in location_information:
    for ending_location in location_information:
        first_city_name = starting_location[0]
        second_city_name = ending_location[0]

        start.append(first_city_name)
        end.append(second_city_name)
        miles = geodesic(starting_location[1], ending_location[1]).miles
        distance.append(miles)


# Enter into distances.csv
with open('distances.csv', mode='w', newline='') as distance_file:
    distance_writer = csv.writer(distance_file, delimiter=',')

    index = 0
    for data_row in distance:
        distance_writer.writerow([start[index], end[index], distance[index]])
        index += 1


