import time
import random

print("The duck fashion show.")
time.sleep(1)

m_row = input("How many rows of ducks are modeling from 1 to 3 or random ")
list_m_row = [1, 2, 3, "random"]
if m_row == "random":
    m_row = random.choice(list_m_row[0:3])
    print(f"Randomly chosen: {m_row}")
else:
    m_row = int(m_row)

d_row = input("\nHow many ducks per row? 1, 2 3 or random? ")
list_d_row = [1, 2, 3, "random"]
if d_row == "random":
    d_row = random.choice(list_d_row[0:3])
    print(f"Randomly chosen: {d_row}")
else:
    d_row = int(d_row)

print("\nGet them ready")
list_outfits = ['hat', 'glasses', 'non', "random"]
for row in list_outfits:
    print(row)
chosen_outfit = input(f"Choose an outfit for the ducks:")

if chosen_outfit == "random":
    chosen_outfit2 = random.choice(list_outfits[0:3])
    print(f"Randomly chosen: {chosen_outfit2}")
else:
    chosen_outfit2 = chosen_outfit
    print(f"You chose: {chosen_outfit2}")


for x in range(m_row):
    for y in range(d_row):
        if chosen_outfit2 == "hat":
            print("         ∆__      ", end="")
        if chosen_outfit2 == "non":
            print("              ", end="")

    print()

    for y in range(d_row):
        if chosen_outfit2 == "glasses":
            print ("      ___(-Ω)<   ", end="")
        else:
            print("      ___( •)<   ", end="")

    print()

    for y in range(d_row):
        print("     <_…__…_)    ", end="")
    print()

    for y in range(d_row):
        print("˜˜˜˜˜          ", end="")
    print()

    print()