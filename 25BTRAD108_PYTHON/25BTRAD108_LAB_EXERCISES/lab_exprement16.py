import random
from collections import Counter

class DiceSimulator:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self, n=1):
        return [random.randint(1, self.sides) for _ in range(n)]

    def run_experiment(self, n=2, rolls=1000):
        res = [sum(self.roll_dice(n)) for _ in range(rolls)]
        freq = Counter(res)
        print(f"\nSimulating {rolls} rolls of {n} x {self.sides}-sided dice:\n" + "-" * 45)
        for s in range(n, n * self.sides + 1):
            c = freq[s]
            pct = (c / rolls) * 100
            print(f"Sum {s:2d} | {c:4d} ({pct:5.2f}%) | {'#' * int(pct * 2)}")

if __name__ == "__main__":
    random.seed(42)
    sim = DiceSimulator()
    print("Sample Roll:", (r := sim.roll_dice(2)), f"Sum = {sum(r)}")
    sim.run_experiment()
