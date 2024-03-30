from Time import Time
from functions import extract_hour_minute


class Row:
    def __init__(self, _id, company, line, departure_time, arrival_time, start_stop, end_stop,
                 start_stop_lat, start_stop_lon, end_stop_lat, end_stop_lon):
        self._id = _id
        self.company = company
        self.line = line
        self.departure_time = Time(*extract_hour_minute(departure_time))
        self.arrival_time = Time(*extract_hour_minute(arrival_time))
        self.start_stop = start_stop
        self.end_stop = end_stop
        self.coordinates_start = (start_stop_lat, start_stop_lon)
        self.coordinates_end = (end_stop_lat, end_stop_lon)

    def __str__(self):
        return f"Row(id={self._id}, company='{self.company}', line='{self.line}', " \
               f"departure_time='{self.departure_time}', arrival_time='{self.arrival_time}', " \
               f"start_stop='{self.start_stop}', end_stop='{self.end_stop}', " \
               f"coordinates_start={self.coordinates_start}, " \
               f"coordinates_end={self.coordinates_end})"
