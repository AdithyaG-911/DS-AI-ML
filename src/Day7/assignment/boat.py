# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 10:03:38 2026

@author: adith
"""

import random

print("=== 🚤 RoboController 2.1 ===")

# ---- User Inputs ----
boat_name = input("Enter Boat Name: ")
distance_to_target = float(input("Enter distance to target (in meters): "))

start_point = "Harbor A"
end_point = "Harbor B"

checkpoints = [f"Start at {start_point}"]
distance_travelled = 0
speed = 10   # default speed (meters per move)


# ---- Movement Simulation ----
while distance_travelled < distance_to_target:

    # Random obstacle appearance
    obstacle_chance = random.choice(["none", "human", "object", "none"])

    if obstacle_chance == "human":
        print("\n🚶 Human detected ahead!")
        print("Boat stopping for safety...")
        speed = 0
        checkpoints.append(f"Stopped at {distance_travelled:.0f}m (Human crossing)")

    elif obstacle_chance == "object":
        print("\n📦 Object detected in water!")
        print("Reversing to avoid collision...")
        checkpoints.append(f"Reversed at {distance_travelled:.0f}m (Object detected)")

        turn_direction = random.choice(["Left", "Right"])
        print(f"Turning {turn_direction}...")
        checkpoints.append(f"Turned {turn_direction} at {distance_travelled:.0f}m")

        speed = 8  # slower after avoidance

    else:
        speed = random.randint(8, 15)

    # Move only if speed > 0
    if speed > 0:
        distance_travelled += speed

        # Prevent overshooting
        if distance_travelled > distance_to_target:
            distance_travelled = distance_to_target

        print(f"Moving at speed {speed} m/s → Total: {distance_travelled:.2f}m")
        checkpoints.append(f"Moved to {distance_travelled:.0f}m (Speed {speed})")


# ---- Ending ----
checkpoints.append(f"Reached {end_point}")


# ---- Trip Summary ----
print("\n=== 🚀 Trip Summary ===")
print(f"Boat Name: {boat_name}")
print(f"Starting Point: {start_point}")
print(f"Ending Point: {end_point}")
print(f"Target Distance: {distance_to_target} meters")
print(f"Final Distance Travelled: {distance_travelled:.2f} meters")
print("\nJourney Log:")

for cp in checkpoints:
    print("-", cp)

print("\nMission Completed Successfully ✅")