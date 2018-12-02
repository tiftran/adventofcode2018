import util


def part_1(input):
    input = map(lambda x: int(x), input)
    return sum(input)


def part_2(input):
    result = 0
    seen_so_far = {}

    while True:
        for num in input:
            result+= int(num)
            if result in seen_so_far:
                return result
            else:
                seen_so_far[result] = True

input = util.get_input("./Input/Day1Input")

print(part_1(input))
print(part_2(input))
