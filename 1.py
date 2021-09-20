sight1, sight2, sight3 = 1, 2, 5


def ner(sight1, sight2, sight3):
    if (sight1 + sight2 > sight3) and (sight1 + sight3 > sight2) and (sight2 + sight3 > sight1):
        p = (sight1 + sight2 + sight3) / 2
        return (p * (p - sight1) * (p - sight2) * (p - sight3)) ** (1/2)
    return 0

print(ner(sight1,sight2, sight3))