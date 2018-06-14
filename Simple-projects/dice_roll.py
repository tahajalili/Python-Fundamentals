#If you like, please follow my gihub repo at http://github.com/tahajalili
import random , time

q = int(input("How many times do you want to roll a dice?: "))


def roll(q):
    for i in range(0,q):
        n = random.randint(1,6)
        print("==> ",n)
        time.sleep(0.5)
try:
    roll(q)
except IndexError:
    print("Error accured in number of rolls.")