import util


def solve(input):
    two = 0
    three = 0
    for word in input:
        temp_2 = False
        temp_3 = False
        for letter in word:
            val = word.count(letter)

            if val == 2 and temp_2 is False:
                two += 1
                temp_2 = True

            if val == 3 and temp_3 is False:
                three += 1
                temp_3 = True

    return two * three


def solve2(input):

    for i in range(len(input)):
        for j in range(i+1, len(input)):
            if len(input[i]) == len(input[j]):
                items, bool = one_diff(input[i], input[j])
                if bool:
                   return"".join(items)


def one_diff(input1, input2):
    counter = 0
    same = []
    for i in range(len(input1)):
        if input1[i]!= input2[i]:
            counter +=1

        else:
            same.append(input1[i])

        if counter > 1:
            return None, False
    return same, True


input = util.get_input("./Input/Day2Input")
print(solve(input))
print(solve2(input))