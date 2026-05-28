#Francis
#therace
import random
finish_line = 50  #Finish Line
tortoise_pos = 0  #Starting Position
hare_pos = 0		 #Starting Position
is_hare_asleep = False #Hare starts Awake

# The Simulation Loop
while tortoise_pos < finish_line and hare_pos < finish_line:
# Tortoise always moves a short distance between 1 - 3 meters at random
    tortoise_move = random.randint(1,3)
    tortoise_pos += tortoise_move
# Hare has a 30% chance of falling a sleep for a turn
    if random.random() < 0.3:
        is_hare_asleep = True
    else:
        is_hare_asleep = False
# If Hare is awake, it will move 1 - 10 meters at random
    if not is_hare_asleep:
        hare_move = random.randint(1,10)
        hare_pos += hare_move
# Print the positions of the Hare and Tortoise after each round
# Determine the winner
if tortoise_pos >= finish_line:
    print("🐢 The Tortoise wins!")
else:
    print("🐇 The Hare wins!")
