import math
import random


class ReciprocalRandom:
    @staticmethod
    def pdf(x: float):
        return 1.0/x

    @staticmethod
    def cdf(x: float):
        return math.log(x)

    @staticmethod
    def inverse_cdf(x: float):
        return math.pow(math.e, x)

    @staticmethod
    def generate(start: float, end: float) -> float:
        a = ReciprocalRandom.cdf(start)
        b = ReciprocalRandom.cdf(end)
        return ReciprocalRandom.inverse_cdf(random.random()*(b - a) + a)
