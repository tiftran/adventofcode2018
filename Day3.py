import util
from collections import defaultdict


def solve(input):
    bounding_boxes = format_data(input)
    result, overlaps = get_overlaps(bounding_boxes)
    return result


def format_data(input):
    bounding_boxes = []
    for entry in input:
        bounding_boxes.append(get_box(entry))
    return bounding_boxes


def get_overlaps(bounding_boxes):
    result = 0
    overlaps = defaultdict(int)
    for _id, x, w, y, h in bounding_boxes:
        # walking through every coordinate pair within the bounding box
        for i in range(w):
            for j in range(h):
                overlaps[(i + x, j + y)] += 1
                # if result is 2, implies co-ordinate has overlapped for the first time
                if overlaps[(i + x, j + y)] == 2:
                    result += 1

    return result, overlaps


def solve_2(input):
    bounding_boxes = format_data(input)
    result, overlaps = get_overlaps(bounding_boxes)

    for _id, x, w, y, h in bounding_boxes:
        found = True
        for i in range(w):
            for j in range(h):
                if overlaps[(i + x, j + y)] != 1:
                    found = False
                    break
            if not found:
                break
        if found:
            return _id


def get_box(entry):
    # 1 @ 53,238: 26x24
    data = entry.split(" ")
    _id = data[0]
    x, y = int(data[2].split(",")[0]), int(data[2].split(",")[1].strip(":"))
    w, h = int(data[3].split("x")[0]), int(data[3].split("x")[1])
    return _id, x, w, y, h


input = util.get_input("./Input/Day3Input")

print(solve(input))
print(solve_2(input))
