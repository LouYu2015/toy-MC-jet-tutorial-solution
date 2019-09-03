import ReciprocalRandom
import matplotlib.pyplot as plt

if __name__ == "__main__":
    r = [ReciprocalRandom.ReciprocalRandom.generate(1, 5)
         for _ in range(10000)]
    plt.hist(r)
    plt.show()