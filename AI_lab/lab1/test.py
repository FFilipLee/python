from Time import Time
from functions import time_difference, extract_hour_minute, add_minutes_to_time
from Row import Row
import csv

if __name__ == '__main__':

    a = Time(15, 55)
    b = Time(15, 56)
    c = Time(1, 40)
    d = Time(12, 7)
    print(add_minutes_to_time(a, 40))
    print(add_minutes_to_time(a, 0))
    print(add_minutes_to_time(a, 92))

    print(Time(*extract_hour_minute("00:23:32")))

    with open('connection_graph.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)

        next(reader)

        for row in range(1):
            print(Row(*next(reader)))

