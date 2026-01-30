import random

def guess_logic(target, attempts_left, count=1):
    if attempts_left == 0:
        print(f"Out of moves! Number was {target}")
        return
    try:
        if (guess := int(input(f"guess ({attempts_left} left): "))) == target:
            print(f"You won in {count} attempts!")
            return
        print("Too High" if guess> target else "Too Low")
        guess_logic(target, attempts_left-1, count+1)
    except ValueError:
        print("Invailid input!")
        guess_logic(target,attempts_left,count)
        
print("1. Easy (100) | 2. Medium (10) | 3. Hard (5)")
levels = {"1":100, "2":10, "3":5}
limit = levels.get(input("Level: "), 10)

guess_logic(random.randint(1,100), limit)