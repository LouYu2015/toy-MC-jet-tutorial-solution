import GaussianRandom
import matplotlib.pyplot as plt

if __name__ == "__main__":
    r = [GaussianRandom.GaussianRandom.generate(0, 10, 5, 2)
         for _ in range(100000)]
    plt.title("Gaussian Function")
    plt.xlabel("Value")
    plt.ylabel("Number of samples")
    plt.hist(r, bins=100)
    plt.show()