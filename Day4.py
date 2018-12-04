import util
import operator
from collections import defaultdict


def aggregate_data(input):
    input.sort()
    time_keeper = defaultdict(int)
    total_time_keeper = defaultdict(int)
    start_sleep = None

    for time_entry in input:
        if "begins shift" in time_entry:
            guard = get_guard(time_entry)

        elif "falls asleep" in time_entry:
            start_sleep = int( get_minute(time_entry))

        elif "wakes up" in time_entry:
            end_sleep = int(get_minute(time_entry))

            total_time_keeper[guard] += (end_sleep - start_sleep)

            for i in range(start_sleep, end_sleep):
                time_keeper[(guard, i)] +=1
            start_sleep = None
    return time_keeper, total_time_keeper


def solve1(agg_data1, agg_data2):
    guard, total_min = max(agg_data2.items(), key=operator.itemgetter(1))

    best_min = None
    min_frequency = 0
    for tup, value in agg_data1.items():
        if tup[0] == guard and value > min_frequency:
            best_min = tup[1]
            min_frequency = value

    return guard, best_min


def solve2(agg_data):

    return max(agg_data.items(), key=operator.itemgetter(1))


def get_minute(time_entry):

    #:XX] ...
    temp = time_entry.split(":")[1]
    return temp.split("]")[0]


def get_guard(entry):
    # #XXX begins shift
    temp = entry.split("#")[1]
    return temp.split(" ")[0]


input = util.get_input("./Input/Day4Input")
agg_data1, agg_data2 = aggregate_data(input)
print(solve1(agg_data1, agg_data2))
print(solve2(agg_data1))