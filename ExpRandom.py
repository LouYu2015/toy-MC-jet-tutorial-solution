import math
import random


class ExpRandom:
    @staticmethod
    def pdf(x: float):
        return math.exp(-x)

    @staticmethod
    def cdf(x: float):
        return -math.exp(-x)

    @staticmethod
    def inverse_cdf(x: float):
        return -math.log(-x)

    @staticmethod
    def generate(start: float, end: float) -> float:
        a = ExpRandom.cdf(start)
        b = ExpRandom.cdf(end)
        return ExpRandom.inverse_cdf(random.random()*(b - a) + a)
