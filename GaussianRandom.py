import math
import random
import scipy.special


class GaussianRandom:
    @staticmethod
    def pdf(x: float, a: float, sigma: float):
        return 1.0/math.sqrt(2 * math.pi * sigma**2) * math.exp(-(x - a)**2/2/sigma**2)

    @staticmethod
    def cdf(x: float, a: float, sigma: float):
        return 0.5 * (1 + math.erf((x - a) / sigma / math.sqrt(2)))

    @staticmethod
    def inverse_cdf(x: float, a: float, sigma: float):
        return math.sqrt(2) * sigma * scipy.special.erfinv(2 * x - 1) + a

    @staticmethod
    def generate(start: float, end: float, center: float, sigma: float) -> float:
        a = GaussianRandom.cdf(start, center, sigma)
        b = GaussianRandom.cdf(end, center, sigma)
        return GaussianRandom.inverse_cdf(random.random()*(b - a) + a, center, sigma)
