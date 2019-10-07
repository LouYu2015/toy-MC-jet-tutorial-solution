import ExpRandom
import matplotlib.pyplot as plt

if __name__ == "__main__":
    r = [ExpRandom.ExpRandom.generate(0, 5)
         for _ in range(100000)]
    plt.title("Exponent Function")
    plt.xlabel("Value")
    plt.ylabel("Number of samples")
    plt.hist(r, bins=100)
    plt.show()