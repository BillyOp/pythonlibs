class Station:
    # Number of stations in the class variable
    total_station_objects = 0
    total_bikes_in_all_stations = 0

    def __init__(self, id, name, totalDocks, availableDocks, availableBikes):
        self.id = id
        self.name = name
        self.totalDocks = totalDocks
        self.availableDocks = availableDocks
        self.availableBikes = availableBikes
        Station.total_station_objects += 1
        Station.total_bikes_in_all_stations += availableBikes

    def current_number_of_stations(self):
        return Station.total_station_objects

    def getTotalBikes(self):
        return Station.total_bikes_in_all_stations

    def getStationName(self):
        return self.name

    def getTotalDocks(self):
        return self.totalDocks

    def getBikesInStation(self):
        return self.availableBikes

    def isDockAvailable(self):
        if(self.availableDocks):
            return True
        else:
            return False

    def areBikesAvailable(self):
        if(self.availableBikes):
            return True
        return False



