import numpy as np
import math
import random
from ReciprocalRandom import ReciprocalRandom
from ExpRandom import ExpRandom


def vector_length(x: np.ndarray) -> float:
    return np.sqrt(x.dot(x))


def rotate_x(p: np.ndarray, theta: float) -> np.ndarray:
    rotation_matrix = np.array([[1, 0, 0],
                                [0, math.cos(theta), -math.sin(theta)],
                                [0, math.sin(theta), math.cos(theta)]])
    return np.dot(rotation_matrix, np.transpose(p))


def rotate_y(p: np.ndarray, theta: float) -> np.ndarray:
    rotation_matrix = np.array([[math.cos(theta), 0, math.sin(theta)],
                                [0, 1, 0],
                                [-math.sin(theta), 0, math.cos(theta)]])
    return np.dot(rotation_matrix, np.transpose(p))


def rotate_z(p: np.ndarray, theta: float) -> np.ndarray:
    rotation_matrix = np.array([[math.cos(theta), -math.sin(theta), 0],
                                [math.sin(theta), math.cos(theta), 0],
                                [0, 0, 1]])
    return np.dot(rotation_matrix, np.transpose(p))


def split(p: np.ndarray) -> (np.ndarray, np.ndarray):
    # Total energy
    energy = vector_length(p)

    # Energy for one branch
    e1 = energy * (ReciprocalRandom.generate(0.1, 1.1) - 0.1)

    # Angle of divergence
    theta = ReciprocalRandom.generate(0.1, math.pi/2 + 0.1) - 0.1

    # Get new branches
    r1 = np.array([e1*math.cos(theta),
                   e1*math.sin(theta),
                   0])
    r2 = np.array([energy - e1,
                   -r1[1],
                   0])

    # Apply azimuthal angle
    roll = random.random() * math.pi
    r1 = rotate_x(r1, roll)
    r2 = rotate_x(r2, roll)

    # Align with source
    pitch = -math.atan2(p[2], vector_length(np.array([p[0], p[1]])))
    r1 = rotate_y(r1, pitch)
    r2 = rotate_y(r2, pitch)

    yaw = math.atan2(p[1], p[0])
    r1 = rotate_z(r1, yaw)
    r2 = rotate_z(r2, yaw)

    return r1, r2


def generate_tree_helper(origin: np.ndarray, p: np.ndarray, cutoff: float) \
        -> [np.ndarray]:
    if vector_length(p) <= cutoff:
        return [p]
    r1, r2 = split(p)

    r1_end = origin + r1
    r2_end = origin + r2

    print("%f, %f, %f, %f, %f, %f" % (origin[0], origin[1], origin[2],
                                      r1_end[0], r1_end[1], r1_end[2]))
    print("%f, %f, %f, %f, %f, %f" % (origin[0], origin[1], origin[2],
                                      r2_end[0], r2_end[1], r2_end[2]))

    return generate_tree_helper(origin + r1, r1, cutoff) + \
        generate_tree_helper(origin + r2, r2, cutoff)


def generate_tree(p: np.ndarray, cutoff: float):
    return generate_tree_helper(np.array([0, 0, 0]), p, cutoff)


def generate_event(cutoff):
    energy = ExpRandom.generate(0, 1000)
    phi = random.random() * math.pi * 2
    theta = random.random() * math.pi
    p1 = np.array([0, 0, energy])
    p1 = rotate_y(p1, theta)
    p1 = rotate_z(p1, phi)
    return generate_tree(p1, cutoff) + generate_tree(-p1, cutoff)


if __name__ == "__main__":
    generate_event(0.05)
