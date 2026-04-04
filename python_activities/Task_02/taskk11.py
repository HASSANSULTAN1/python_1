

import random

def flip():
    return random.randint(0, 1)



heads_count = 0
tails_count = 0


print("COIN TOSS SIMULATION")


for i in range(1, 101):
    result = flip()
    
    if result == 1:
        heads_count += 1
        outcome = "Heads"
    else:
        tails_count += 1
        outcome = "Tails"
    
    print("Toss " + str(i) + ": " + outcome)


print("FINAL RESULTS")
print("Total Tosses : 100")
print("Heads        : " + str(heads_count) + " times")
print("Tails        : " + str(tails_count) + " times")
print("Heads %      : " + str(round(heads_count, 2)) + "%")
print("Tails %      : " + str(round(tails_count, 2)) + "%")
