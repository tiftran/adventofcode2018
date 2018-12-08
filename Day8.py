import util


def solve1(input):
    children, data = input[:2]
    input = input[2:]
    total_sum = 0

    # base case when there are no children
    if children is 0:
        total_sum += sum(input[:data])
        return total_sum, input[data:]

    else:
        for i in range(children):
            total, input = solve1(input)
            total_sum += total
        total_sum += sum(input[:data])

        return total_sum,  input[data:]



def solve2(input):
    children, data = input[:2]
    input = input[2:]
    total_sum = 0
    references = []

    # base case when there are no children
    if children is 0:
        total_sum += sum(input[:data])
        return total_sum, input[data:]

    else:
        for i in range(children):
            total, input = solve2(input)
            references.append(total)

        for entry in input[:data]:
            if entry -1 <len(references):
                total_sum += references[entry-1]

        return total_sum,  input[data:]


input = util.get_input("./Input/Day8Input")
input = input[0].split(" ")
input = [int(i) for i in input]



print(solve1(input))
print(solve2(input))