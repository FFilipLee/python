import math
from Stop import Stop
from Time import Time


def distance(coordinates_a, coordinates_b):
    # coordinates in a form of tuple (lat,long), output is in kilometers
    a_lat_rad = math.radians(float(coordinates_a[0]))
    a_lon_rad = math.radians(float(coordinates_a[1]))
    b_lat_rad = math.radians(float(coordinates_b[0]))
    b_lon_rad = math.radians(float(coordinates_b[1]))

    r = 6371

    a_x = r * a_lon_rad * math.cos(a_lat_rad)
    a_y = r * a_lat_rad
    b_x = r * b_lon_rad * math.cos(b_lat_rad)
    b_y = r * b_lat_rad

    return math.sqrt((a_x - b_x) ** 2 + (a_y - b_y) ** 2)


def minutes_to_time(minutes):
    hours = minutes / 60
    minutes = minutes - hours * 60

    return Time(hours, minutes)


def add_minutes_to_time(time_a: Time, minutes):
    new_minutes = time_a.minute + minutes
    new_hours = time_a.hour + int(new_minutes / 60)
    new_minutes = new_minutes % 60
    return Time(new_hours, new_minutes)


def time_difference(time_a: Time, time_b: Time):
    if time_a <= time_b:
        return time_diff_a_to_b(time_a, time_b)
    else:
        return time_diff_a_to_b(time_b, time_a)


def time_diff_a_to_b(time_a: Time, time_b: Time):
    return (time_b.hour - time_a.hour) * 60 + (time_b.minute - time_a.minute)


def extract_hour_minute(time_str):
    hour, minute, _ = time_str.split(':')

    hour = int(hour)
    minute = int(minute)

    return hour, minute


def heuristic_t(station_a: Stop, station_b: Stop):
    # 3/2 because 1 h = 60 min, 40 km/h approx. avg speed
    return (3/2) * distance(station_a.coordinates, station_b.coordinates)


def heuristic_t_optimized(station_a: Stop, station_b: Stop):
    return 4 * distance(station_a.coordinates, station_b.coordinates)


def heuristic_p_stop(station_a: Stop, station_b: Stop):
    if station_a.from_line != station_b.from_line and station_a is not None and station_b is not None:
        return 25
    return 0


def heuristic_p_line(station_a: Stop, line):
    if station_a.from_line != line and station_a is not None:
        return 25
    return 0


if __name__ == '__main__':
    print(distance((51.11162272, 17.05996513), (51.10971261, 17.06511141)))

    test_object_a = Stop('a', 51.11162272, 17.05996513)
    test_object_b = Stop('b', 51.10971261, 17.06511141)

    print(heuristic_t(test_object_a, test_object_b))
