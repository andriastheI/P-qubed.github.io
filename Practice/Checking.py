word = 10


def numberWord(val):
    num_str = str(val)
    length = 0

    if num_str == "1000":
        return 11
    if len(num_str) == 3:
        length += 10

    for i in range(len(num_str)):
        numb = int(num_str[i])

        check2 = int(num_str[-2:])
        if numberHelper(check2) == 0 and i == 1:
            numb *= 10
        elif numberHelper(check2) != 0 and i == 1:
            length += numberHelper(check2)
            return length

        value = numberHelper(numb)
        length += value

    return length


def numberHelper(num):
    if num in [1, 2, 6, 10]:
        return 3
    elif num in [4, 5, 9]:
        return 4
    elif num in [3, 7, 8, 40, 50, 60]:
        return 5
    elif num in [11, 12, 20, 30, 80, 90]:
        return 6
    elif num in [15, 16, 70]:
        return 7
    elif num in [13, 14, 18, 19]:
        return 8
    elif num in [17]:
        return 9
    else:
        return 0


check = numberWord(word)
print(check)