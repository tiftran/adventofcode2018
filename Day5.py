import util
import string

def solve1(input):
    stack = []
    for element in input:
        try:
            top_of_stack = stack[-1]
            if same_letter(top_of_stack, element) and is_opposite_case(top_of_stack, element):
                stack.pop()
            else:
                stack.append(element)
        except IndexError as e:
            stack.append(element)

    return len(stack)


def is_opposite_case(element1, element2):
    return (element1.islower() and element2.isupper()) or (element1.isupper() and element2.islower())


def same_letter(element1, element2):
    return element1.lower() == element2.lower()


def solve2(input):

    current_len = len(input)
    current_letter = None

    for letter in string.ascii_lowercase:
        new_input = input.replace(letter, "")
        new_input = new_input.replace(letter.upper(), "")

        new_length = solve1(new_input)
        if new_length < current_len:
            current_len = new_length
            current_letter = letter

    return current_letter, current_len

input = util.get_input("./Input/Day5Input")
input = "".join(input)
print(solve1(input))
print(solve2(input))
