import numpy as np
import math
import copy


def transverse(p: np.ndarray):
    return np.linalg.norm(p[0:2])


def angular_distance(p1: np.ndarray, p2: np.ndarray):
    return math.acos(
        np.dot(p1, p2) /
        (np.linalg.norm(p1) * np.linalg.norm(p2))
    )


def jet_distance(p1: np.ndarray, p2: np.ndarray, n: int, r: int):
    return math.pow(min(transverse(p1),
                        transverse(p2)),
                    2 * n) * angular_distance(p1, p2) / r


def beam_distance(p: np.ndarray, n: int):
    return math.pow(transverse(p), 2 * n)


def find_jets_to_merge(jets: [np.ndarray], n, r):
    assert(len(jets) >= 2)
    min_i = 0
    min_j = 1
    min_d = float('inf')
    for i in range(len(jets)):
        for j in range(i + 1, len(jets)):
            d = jet_distance(jets[i], jets[j], n, r)
            if d < min_d:
                min_i = i
                min_j = j
                min_d = d
    return min_i, min_j, min_d


def find_jet_to_remove(jets: [np.ndarray], n):
    min_i = 0
    min_d = float('inf')
    for i in range(len(jets)):
        d = beam_distance(jets[i], n)
        if d < min_d:
            min_i = i
            min_d = d
    return min_i, min_d


def cluster_jets(jets: [np.ndarray], n: int, r: int):
    result = []
    jets = copy.copy(jets)
    while len(jets) >= 2:
        min_merge_i, min_merge_j, min_merge_d = find_jets_to_merge(jets, n, r)
        min_i, min_d = find_jet_to_remove(jets, n)
        if min_merge_d < min_d:
            jet1 = jets[min_merge_i]
            jet2 = jets[min_merge_j]
            del jets[min_merge_j]
            del jets[min_merge_i]
            jets.append(jet1 + jet2)
        else:
            result.append(jets[min_i])
            del jets[min_i]
    return result + jets