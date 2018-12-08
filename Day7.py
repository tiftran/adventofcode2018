import util
from collections import defaultdict


def solve(input):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z"]
    input = trim_input(input)
    prereq = build_prereqs(input)
    consumed = set()
    result = ""
    while True:
        if len(consumed) == len(alphabet):
            break

        for letter in alphabet:
            if letter not in consumed and contains_all(prereq[letter], consumed):
                consumed.add(letter)
                result += letter
                break
    return result


def contains_all(set1, set2):
    for element in set1:
        if element not in set2:
            return False
    return True


def build_prereqs(input):
    prereq = defaultdict(set)
    for tup in input:
        prereq[tup[0]].add(tup[1])

    return prereq


def trim_input(input):
    result = []
    for line in input:
        x, y = line.split("must")
        x = x.split("Step ")[1].strip()
        y = y.split("step ")[1].split(" can")[0]
        result.append((y, x))

    return result


def solve2(input):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z"]
    jobs = [None] * 5
    duration_of_job = [None] * 5
    done = set()

    input = trim_input(input)
    prereq = build_prereqs(input)
    time = -1

    while True:
        time += 1
        for i in range(len(jobs)):
            if jobs[i] is not None:
                duration_of_job[i] -= 1
                if duration_of_job[i] == 0:
                    done.add(jobs[i])
                    jobs[i] = None

        for i in range(len(jobs)):
            if jobs[i] is None:
                for letter in alphabet:
                    if letter not in done and letter not in jobs and contains_all(prereq[letter], done):
                        jobs[i] = letter
                        duration_of_job[i] = 60 + ord(letter) - ord('A') + 1
                        break
        if len(done) == len(alphabet):
            break

    return time


input = util.get_input("./Input/Day7Input")

print(solve(input))
print(solve2(input))
