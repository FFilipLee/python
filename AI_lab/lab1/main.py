import csv
from Row import Row
from Stop import Stop
from Time import Time
from functions import extract_hour_minute
import re
import copy
from dijkstra import dijkstra
from a_star import a_star, a_star_t_optimized
import time


if __name__ == '__main__':
    stop_dict = {}

    with open('connection_graph.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)

        # skipping the first row with column titles
        next(reader)

        for row in reader:
            current_row = Row(*row)

            if current_row.start_stop not in stop_dict:
                stop_dict[current_row.start_stop] = Stop(current_row.start_stop, current_row.coordinates_start)

            if current_row.end_stop not in stop_dict[current_row.start_stop].neighbours:
                stop_dict[current_row.start_stop].neighbours[current_row.end_stop] = []

            stop_dict[current_row.start_stop].neighbours[current_row.end_stop].append(current_row)

    init_station = input('Enter initial station: ')
    while init_station not in stop_dict.keys():
        init_station = input('Such station does not exist, enter initial station again: ')

    final_station = input('Enter final station: ')
    while final_station not in stop_dict.keys():
        final_station = input('Such station does not exist, enter final station again: ')

    while init_station == final_station:
        final_station = input('Initial station and final station are identical, enter different final station: ')

    optimization_criteria = input('Optimization criteria for A*: t - shortest time, p - least amount of transfers: ')
    while optimization_criteria not in ('t', 'p'):
        optimization_criteria = input('Wrong criteria, enter t or p: ')

    time_str = input('Enter departure time in a form HH:mm:ss, eg. 06:48:00: ')
    while re.search("([0-1]\\d|2[0-3]):[0-5]\\d:\\d\\d", time_str) is None:
        time_str = input('Wrong format, enter departure time in a form HH:mm:ss, eg. 06:48:00: ')
    departure_time = Time(*extract_hour_minute(time_str))

    if optimization_criteria == 't':
        stop_dict_copy_1 = copy.copy(stop_dict)

        start_time = time.perf_counter()
        print(dijkstra(init_station, final_station, departure_time, stop_dict_copy_1))
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Dijkstra time: {elapsed_time} seconds\n")

        stop_dict_copy_2 = copy.copy(stop_dict)

        start_time = time.perf_counter()
        print(a_star_t_optimized(init_station, final_station, departure_time, stop_dict_copy_2))
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"A* optimized time: {elapsed_time} seconds\n")

    stop_dict_copy_3 = copy.copy(stop_dict)

    start_time = time.perf_counter()
    print(a_star(init_station, final_station, optimization_criteria, departure_time, stop_dict_copy_3))
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"A* time: {elapsed_time} seconds")
