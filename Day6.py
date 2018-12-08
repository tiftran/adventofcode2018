import util
import collections

MAX_DISTANCE = 10000


def get_input(name):
    return [line.strip() for line in open(name)]


def convert_to_tuple(input):
    result = []
    for line in input:
        x, y = line.split(",")
        result.append((int(x),int(y)))
    return result


def get_edge_dim(input):
    min_x = min(x for x,y in input)
    max_x = max(x for x,y in input)
    min_y = min(y for x,y in input)
    max_y = max(y for x,y in input)

    return (min_x, max_x), (min_y, max_y)


def find_dist(pt1, pt2):
    return abs(pt1[0]-pt2[0]) + abs(pt2[1] - pt1[1])


def find_area(x_range, y_range, input):
    areas = collections.defaultdict(int)
    for x in range(x_range[0], x_range[1]):
        for y in range(y_range[0], y_range[1]):
            tup = find_min_dist(x, y, input)
            if tup:
                areas[tup] += 1

    return areas


def find_min_dist(x, y, input):
    list_dist = []

    for pt in input:
        dist = find_dist((x, y), pt)
        list_dist.append((dist, pt))
    list_dist.sort()
    if list_dist[0][0] == list_dist[1][0]:
        return None

    else:
        return list_dist[0][1]


def find_max_area(areas, areas2):
    max_area = 0

    for key in areas:
        if areas[key] == areas2[key] and areas[key] > max_area:
            max_area = areas[key]

    return max_area


def solve1(input):
    x_range, y_range = get_edge_dim(input)
    dict_of_areas = find_area(x_range, y_range, input)

    # to rule out the edge cases, if area is by the edge
    x_range = (x_range[0]-5,x_range[1]+5)
    y_range = (y_range[0] - 5, y_range[1] + 5)
    dict_of_bigger_area = find_area(x_range, y_range, input)

    return find_max_area(dict_of_areas, dict_of_bigger_area)


def solve2(input):
    x_range, y_range = get_edge_dim(input)
    return find_region(x_range,y_range,input)


def find_region(x_range, y_range, input):
    counter = 0
    for i in range(x_range[0], x_range[1]):
        for j in range(y_range[0], y_range[1]):
            total_dist = find_sum_of_dist(i,j,input)
            if total_dist < MAX_DISTANCE:
                counter +=1

    return counter


def find_sum_of_dist(x, y, input):
    total_dist = 0
    for entry in input:
        total_dist += find_dist((x,y), entry)

    return total_dist


input = util.get_input("./Input/Day6Input")
input = convert_to_tuple(input)
print(solve1(input))
solve2(input)