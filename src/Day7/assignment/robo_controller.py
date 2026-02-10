#object detector bot.
#input:bot name from user
#output:distance traveled by the bot
#condition:bot should be able to move forward and backward and turn left and right.
#if bot detect human, then it will wait for human to move away, or else, it will move in random direction, such as reverse, left or right.
#bot will detect object or human from 50meters distance.

#problem statement: RoboController 1.0

#Simulate a robot's movement, take user inputs, make decisions using if statements, manage checkpoints with lists, and show a trip summary.
#1.The program should take inputs such as the robot's name, the distance to the target, and whether there is an obstacle ahead.
#2.Based on this information, it should decide the robot's speed and movement using if elif-else and nested if conditions.
#3.The robot should record its journey by storing checkpoints in a list, allow updates such as adding or removing checkpoints, and use the random module to simulate unexpected direction changes.
#4.Finally, it should display a complete trip summary using f-strings, showing the robot's name, total distance travelled, obstacle status, and final checkpoint list

import random
bot_name=input("Enter the robot's name: ")
distance=int(input("Enter the distance to the target (in meters): "))
obstacle=input("Is there an obstacle ahead? (yes/no): ").lower()
obstacles = ["Human", "Wall", "Object"]
#obstacle_name=random.choice(["Human", "Wall","Object"])   <- This is advanced code.
obstacle_name = obstacles[random.randint(0, len(obstacles)-1)]  # This is basic code to select a random obstacle from the list.
checkpoints = []

print("========================================================")
print(f"Bot's Name                     :{bot_name}")
print(f"Toatal distance traveelled     :{distance} meters")
print(f"Obstacle status                 :{obstacle}")
print(f"Obstacle detected               :{obstacle_name}")