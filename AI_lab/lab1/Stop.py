class Stop:

    def __init__(self, name, coordinates):
        self.name = name
        self.coordinates = coordinates
        self.travel_time = None
        self.from_stop = None
        self.from_line = None
        self.neighbours = {}

    def __str__(self):
        return f"Stop(name={self.name}, coordinates='{self.coordinates})"
