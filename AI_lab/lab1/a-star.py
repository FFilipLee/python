from functions import *


def a_star(init_station, final_station, optimization_criteria, departure_time, stop_dict: dict[str, Stop]):
    if optimization_criteria == "t":
        return a_star_t(init_station, final_station, departure_time, stop_dict)
    return a_star_p(init_station, final_station, departure_time, stop_dict)


def a_star_t(init_station, final_station, departure_time, stop_dict: dict[str, Stop]):
    stop_dict[init_station].travel_time = 0
    unvisited = []
    visited = {init_station: stop_dict[init_station]}

    current_stop = init_station

    while current_stop != final_station:
        for key, value in stop_dict[current_stop].neighbours.items():
            if key not in visited:
                if key not in unvisited:
                    min_row = None
                    min_minutes = 1023
                    for row in value:
                        if row.departure_time >= add_minutes_to_time(departure_time,
                                                                     stop_dict[current_stop].travel_time):
                            if time_difference(departure_time, row.arrival_time) < min_minutes:
                                min_row = row
                                min_minutes = time_difference(departure_time, row.arrival_time)

                    if min_row is not None:
                        unvisited.append(key)
                        stop_dict[key].travel_time = min_minutes
                        stop_dict[key].from_stop = current_stop
                        stop_dict[key].from_line = min_row.line

                else:
                    min_row = None
                    min_minutes = stop_dict[key].travel_time
                    for row in value:
                        if row.departure_time >= add_minutes_to_time(departure_time,
                                                                     stop_dict[current_stop].travel_time):
                            if time_difference(departure_time, row.arrival_time) < min_minutes:
                                min_row = row
                                min_minutes = time_difference(departure_time, row.arrival_time)

                    if min_row is not None:
                        stop_dict[key].travel_time = min_minutes
                        stop_dict[key].from_stop = current_stop
                        stop_dict[key].from_line = min_row.line

        # choosing next current_stop
        min_time_stop = None
        min_time = 1023
        for elem in unvisited:
            if stop_dict[elem].travel_time + heuristic_t(stop_dict[final_station], stop_dict[elem]) < min_time:
                min_time_stop = elem
                min_time = stop_dict[elem].travel_time

        unvisited.remove(min_time_stop)
        visited[min_time_stop] = True
        current_stop = min_time_stop

    station_backwards = current_stop
    changes = 0

    while station_backwards != init_station:
        s_b_travel_time = stop_dict[station_backwards].travel_time
        s_b_from_line = stop_dict[station_backwards].from_line

        print(f'{station_backwards} {s_b_travel_time} {s_b_from_line}')

        station_backwards = stop_dict[station_backwards].from_stop

        if stop_dict[station_backwards].from_line != s_b_from_line \
                and stop_dict[station_backwards].from_line is not None:
            changes += 1

    return f"Shortest travel from {init_station} to {final_station} at " \
           f"{departure_time}: {stop_dict[current_stop].travel_time} minutes with {changes} changes"


def a_star_p(init_station, final_station, departure_time, stop_dict: dict[str, Stop]):
    stop_dict[init_station].travel_time = 0
    unvisited = []
    visited = {init_station: stop_dict[init_station]}

    current_stop = init_station

    while current_stop != final_station:
        for key, value in stop_dict[current_stop].neighbours.items():
            if key not in visited:
                if key not in unvisited:
                    min_row = None
                    min_minutes = 1023
                    for row in value:
                        if row.departure_time >= add_minutes_to_time(departure_time,
                                                                     stop_dict[current_stop].travel_time):
                            if time_difference(departure_time, row.arrival_time) + \
                                    heuristic_p_line(stop_dict[current_stop], row.line) < min_minutes:
                                min_row = row
                                min_minutes = time_difference(departure_time, row.arrival_time)

                    if min_row is not None:
                        unvisited.append(key)
                        stop_dict[key].travel_time = min_minutes
                        stop_dict[key].from_stop = current_stop
                        stop_dict[key].from_line = min_row.line

                else:
                    min_row = None
                    min_minutes = stop_dict[key].travel_time
                    for row in value:
                        if row.departure_time >= add_minutes_to_time(departure_time,
                                                                     stop_dict[current_stop].travel_time):
                            if time_difference(departure_time, row.arrival_time) + \
                                    heuristic_p_line(stop_dict[current_stop], row.line) < min_minutes:
                                min_row = row
                                min_minutes = time_difference(departure_time, row.arrival_time)

                    if min_row is not None:
                        stop_dict[key].travel_time = min_minutes
                        stop_dict[key].from_stop = current_stop
                        stop_dict[key].from_line = min_row.line

        # choosing next current_stop
        min_time_stop = None
        min_time = 1023
        for elem in unvisited:
            if stop_dict[elem].travel_time + heuristic_p_stop(stop_dict[current_stop], stop_dict[elem]) < min_time:
                min_time_stop = elem
                min_time = stop_dict[elem].travel_time

        unvisited.remove(min_time_stop)
        visited[min_time_stop] = True
        current_stop = min_time_stop

    station_backwards = current_stop
    changes = 0

    while station_backwards != init_station:
        s_b_travel_time = stop_dict[station_backwards].travel_time
        s_b_from_line = stop_dict[station_backwards].from_line

        print(f'{station_backwards} {s_b_travel_time} {s_b_from_line}')

        station_backwards = stop_dict[station_backwards].from_stop

        if stop_dict[station_backwards].from_line != s_b_from_line \
                and stop_dict[station_backwards].from_line is not None:
            changes += 1

    return f"Shortest travel from {init_station} to {final_station} at " \
           f"{departure_time}: {stop_dict[current_stop].travel_time} minutes with {changes} changes"


def a_star_t_optimized(init_station, final_station, departure_time, stop_dict: dict[str, Stop]):
    stop_dict[init_station].travel_time = 0
    unvisited = []
    visited = {init_station: stop_dict[init_station]}

    current_stop = init_station

    while current_stop != final_station:
        for key, value in stop_dict[current_stop].neighbours.items():
            if key not in visited:
                if key not in unvisited:
                    min_row = None
                    min_minutes = 1023
                    for row in value:
                        if row.departure_time >= add_minutes_to_time(departure_time,
                                                                     stop_dict[current_stop].travel_time):
                            if time_difference(departure_time, row.arrival_time) < min_minutes:
                                min_row = row
                                min_minutes = time_difference(departure_time, row.arrival_time)

                    if min_row is not None:
                        unvisited.append(key)
                        stop_dict[key].travel_time = min_minutes
                        stop_dict[key].from_stop = current_stop
                        stop_dict[key].from_line = min_row.line

                else:
                    min_row = None
                    min_minutes = stop_dict[key].travel_time
                    for row in value:
                        if row.departure_time >= add_minutes_to_time(departure_time,
                                                                     stop_dict[current_stop].travel_time):
                            if time_difference(departure_time, row.arrival_time) < min_minutes:
                                min_row = row
                                min_minutes = time_difference(departure_time, row.arrival_time)

                    if min_row is not None:
                        stop_dict[key].travel_time = min_minutes
                        stop_dict[key].from_stop = current_stop
                        stop_dict[key].from_line = min_row.line

        # choosing next current_stop
        min_time_stop = None
        min_time = 1023
        for elem in unvisited:
            if stop_dict[elem].travel_time + heuristic_t(stop_dict[final_station], stop_dict[elem]) < min_time:
                min_time_stop = elem
                min_time = stop_dict[elem].travel_time

        unvisited.remove(min_time_stop)
        visited[min_time_stop] = True
        current_stop = min_time_stop

    station_backwards = current_stop
    changes = 0

    while station_backwards != init_station:
        s_b_travel_time = stop_dict[station_backwards].travel_time
        s_b_from_line = stop_dict[station_backwards].from_line

        print(f'{station_backwards} {s_b_travel_time} {s_b_from_line}')

        station_backwards = stop_dict[station_backwards].from_stop

        if stop_dict[station_backwards].from_line != s_b_from_line \
                and stop_dict[station_backwards].from_line is not None:
            changes += 1

    return f"Shortest travel from {init_station} to {final_station} at " \
           f"{departure_time}: {stop_dict[current_stop].travel_time} minutes with {changes} changes"
