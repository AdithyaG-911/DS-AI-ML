# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 11:13:08 2026

@author: adith
"""

import random

print("=== 🤖 RoboController 2.1 ===")

# ---- User Inputs ----
bot_name = input("Enter Bot Name: ")
distance_to_target = float(input("Enter distance to target (in meters): "))
obstacle_ahead = input("Is there an obstacle ahead? (yes/no): ").lower()

start_point = "Base Station"
end_point = "Target Zone"

checkpoints = [f"Start at {start_point}"]
distance_travelled = 0
speed = 10  # default speed


# ---- Initial Speed Decision (if-elif + nested if) ----
if obstacle_ahead == "yes":
    if distance_to_target > 100:
        speed = 6
    else:
        speed = 8
else:
    if distance_to_target > 100:
        speed = 15
    elif distance_to_target > 50:
        speed = 12
    else:
        speed = 9

checkpoints.append(f"Initial speed set to {speed} m/s")


# ---- Movement Simulation ----
while distance_travelled < distance_to_target:

    detected_distance = random.randint(10, 60)

    if detected_distance <= 50:
        obstacle_type = random.choice(["human", "object"])

        if obstacle_type == "human":
            print("\n🚶 Human detected within 50m!")
            print("Bot stopping for safety...")
            checkpoints.append(f"Stopped at {distance_travelled:.0f}m (Human detected)")
            continue

        elif obstacle_type == "object":
            print("\n📦 Object detected within 50m!")
            print("Reversing to avoid collision...")

            reverse_step = random.randint(5, 10)
            distance_travelled = max(0, distance_travelled - reverse_step)
            checkpoints.append(f"Reversed to {distance_travelled:.0f}m")

            turn_direction = random.choice(["Left", "Right"])
            print(f"Turning {turn_direction}...")
            checkpoints.append(f"Turned {turn_direction} at {distance_travelled:.0f}m")

            speed = random.randint(6, 10)  # slower after avoidance

    else:
        speed = random.randint(8, 15)

    # ---- Move Forward ----
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
print(f"Bot Name: {bot_name}")
print(f"Starting Point: {start_point}")
print(f"Ending Point: {end_point}")
print(f"Target Distance: {distance_to_target} meters")
print(f"Final Distance Travelled: {distance_travelled:.2f} meters")
print("\nJourney Log:")

for cp in checkpoints:
    print("-", cp)

print("\nMission Completed Successfully ✅")
