# python read json file
import json
from station import Station

with open('data.json', 'r') as file:
    if file.readable():
        stations_json = file.read()
        stations_dict = json.loads(stations_json)
        print(stations_dict)

        station_list = stations_dict["stationBeanList"]

        # id
        # stationName
        # totalDocks
        # availableDocks
        # availableBikes
        list_of_stations = []
        for station in station_list:
            list_of_stations.append(Station(station['id'], station['stationName'], station['totalDocks'], station['availableDocks'], station['availableBikes']))

        print(len(list_of_stations))

        print("Station Name | Available Bikes in the Station")
        for station in list_of_stations:
            print(f'Station Name: {station.getStationName()} \n Available Bikes: {station.getBikesInStation()}')
            print("----------------------------------------------------------------------------------------------\n\n")

        print(Station.total_bikes_in_all_stations)
        print(Station.total_station_objects)
        print(len(list_of_stations))





