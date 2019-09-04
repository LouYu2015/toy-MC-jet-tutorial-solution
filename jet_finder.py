import numpy as np
import math
import copy
import generator


def transverse(p: np.ndarray):
    return np.linalg.norm(p[0:2])


def angular_distance(p1: np.ndarray, p2: np.ndarray):
    return math.atan2(np.linalg.norm(np.cross(p1, p2)), np.dot(p1, p2))


def jet_distance(p1: np.ndarray, p2: np.ndarray, n: int, r: int):
    return math.pow(min(transverse(p1),
                        transverse(p2)),
                    2 * n) * angular_distance(p1, p2) / r


def beam_distance(p: np.ndarray, n: int):
    return math.pow(transverse(p), 2 * n)


def find_jets_to_merge(jets: [np.ndarray], n, r, cache):
    assert(len(jets) >= 2)
    min_i = 0
    min_j = 1
    min_d = float('inf')
    for i in range(len(jets)):
        for j in range(i + 1, len(jets)):
            index = (tuple(jets[i]), tuple(jets[j]))
            if index in cache:
                d = cache[index]
            else:
                d = jet_distance(jets[i], jets[j], n, r)
                cache[index] = d
            if d < min_d:
                min_i = i
                min_j = j
                min_d = d
    return min_i, min_j, min_d


def find_jet_to_remove(jets: [np.ndarray], n, cache):
    min_i = 0
    min_d = float('inf')
    for i in range(len(jets)):
        index = tuple(jets[i])
        if index in cache:
            d = cache[index]
        else:
            d = beam_distance(jets[i], n)
            cache[index] = d
        if d < min_d:
            min_i = i
            min_d = d
    return min_i, min_d


def cluster_jets(jets: [np.ndarray], n: float, r: float, exclusive: bool):
    result = []
    jets = copy.copy(jets)
    # jets = [np.array(x, dtype=np.float32) for x in jets]
    cache_merge = {}
    cache_promote = {}
    while len(jets) > (2 if exclusive else 1):
        min_merge_i, min_merge_j, min_merge_d = find_jets_to_merge(jets, n, r, cache_merge)
        min_i, min_d = find_jet_to_remove(jets, n, cache_promote)
        if min_merge_d < min_d or exclusive:
            jet1 = jets[min_merge_i]
            jet2 = jets[min_merge_j]
            del jets[min_merge_j]
            del jets[min_merge_i]
            jets.append(jet1 + jet2)
            print("merging %d %d" % (min_merge_i, min_merge_j))
        else:
            result.append(jets[min_i])
            del jets[min_i]
            print("promoting %d" % min_i)
    return result + jets


def main():
    j = generator.initial_jet()
    print(cluster_jets(generator.generate_event(j, 0.05), 1, 1, exclusive=False))
    print(j)


if __name__ == "__main__":
    main()
