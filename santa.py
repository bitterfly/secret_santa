import itertools
import numpy as np

def get_santas(people, couples):
    while True:
        permutation = list(np.random.permutation(people))
        hamilton_permutation = [permutation[-1]] + permutation[:-1]
        if valid(zip(hamilton_permutation, permutation), couples):
            return {key: value for (key, value) in zip(permutation, hamilton_permutation)}


def valid(people, couples):
    for person, santa in people:
        if person == santa or ''.join(sorted(person+santa)) in couples:
            return False
    return True