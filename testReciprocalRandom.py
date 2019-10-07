import ReciprocalRandom
import matplotlib.pyplot as plt

if __name__ == "__main__":
    r = [ReciprocalRandom.ReciprocalRandom.generate(1, 5)
         for _ in range(100000)]
    plt.title("Reciprocal Function")
    plt.xlabel("Value")
    plt.ylabel("Number of samples")
    plt.hist(r, bins=100)
    plt.show()