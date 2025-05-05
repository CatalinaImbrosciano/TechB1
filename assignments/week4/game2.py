# SAVE THE ASADO - Refactored Version
# A typical Argentine family lunch, asado, is thrown off by your cousin Mariano's mistake. Your goal is to make sure the asado happens no matter what.

import time
import sys

DEBUG = False  # Remember to set your DEBUG flag to false when you hand in your assignment


LOSING_MESSAGE = "\nGAME OVER\n    😖\n\n\n Do you want to try again?"
WINNING_MESSAGE = ", YOU SAVED THE ASADO 👏🏼👏🏼👏🏼"

def intro():
    name = input("Hello! Please enter your name: ")
    name = name.upper()
    print("\nGood morning", name, "☀️")
    time.sleep(1)
    print("\n🕚It's Sunday 11am in Buenos Aires, Argentina.")
    time.sleep(2)
    print(
        "  It is a beautiful sunny day. Your family is starting to arrive for a typical Argentine family lunch: Asado 🇦🇷 \n  Do you know what an Asado is?")
    time.sleep(6)
    print(
        "🥩 ASADO: It's a tradition. A special cut of meat is grilled over an open flame, usually joined by other cuts, bread, fries, a variety of salads and wine.")
    time.sleep(6)
    print("   Your grandma insists on having the whole family seated and the food served at exactly 2 p.m, and...")
    time.sleep(8) #
    return name
#Game context + input name

def scene1():
    print("\n                    It's your alarm!!")
    print("                       ⏰🎶⏰🎶⏰ ")
    time.sleep(3)

    print("\nOutside your room you can already hear some voices, laughter, and the clink of wine glasses 🍷✨\nDo you...\n🔇 Turn off the alarm and join the others as they arrive? \n🛌 Hit snooze and catch a few more minutes of sleep? ")
    time.sleep(3)
    answer1 = input("\nWhat do you do... a. [Stop]  b. [Snooze]?")
    if answer1 == "a":
        print("Let's go then 🎉")
    if answer1 == "b":
        print("Okey...5 more minutes 😴")
        time.sleep(2)
        print("\nYour alarm rings again ⏰🙄")
        answer1 = input("What do you do... a. [Stop]  b. [Snooze]?")
        if answer1 == "a":
            print("Alright, let's go! 🎉")
        if answer1 == "b":
            print("Again? Okey...💤")
            time.sleep(2)
            while True:
                answer1 = input("a. [Stop]  b. [Snooze]? ⏰🙄")
                time.sleep(1)
                if answer1 == "a":
                    break
            print("Finally! Let's go 🎉")
#scene 1: Alarm - getting up

def scene2(name):
    time.sleep(2)
    print("\nIn the backyard, your dad and uncle are turning on the fire. 🌳🔥 You’re about to join them.\nThey’re chatting with the neighbor, who’s also making asado next door. They’re probably talking about football...⚽")
    time.sleep(8)
    print("\nWait! The doorbell rings.\n 🚪")
    time.sleep(2)
    print("\nDo you open the door?")
    answer = input("a. Open\nb. Join your father and uncle?")

    if answer == "b":
        print("\nYes, they are indeed talking about football⚽️")
        time.sleep(2)
        print("Your mom approaches, looking upset...")
        time.sleep(2)
        print("- Mariano just arrived... and he forgot the meat...🤦🏽‍♀️")
        time.sleep(2)
        print("- What?! I'm going to kill my son.")
        time.sleep(3)
        print("- No meat, no asado.🥩❌")
        time.sleep(2)
        print (LOSING_MESSAGE)
        again = input("  yes / no?")
        if again == "no":
            sys.exit()
        if again == "yes":
            main()
        return again

    if answer == "a":
        print("\nIt's Mariano, your cousin ")
        time.sleep(2)
        print("- I need your help...😓")
        time.sleep(2)
        print("  I forgot the meat, they are going to kill me!")
        time.sleep(2)
        print("\n😵")
        time.sleep(2)
        print("Take a deep breath", name, "...")
        time.sleep(2)
        print("And go get some meat before anyone notices!")
        time.sleep(1)
        print("\n  SAVE")
        time.sleep(1)
        print("  THE")
        time.sleep(1)
        print(" ASADO\n 🥩🔥⏳")
        time.sleep(3)
#scene 2: Doorbell rings.

def scene3():
    print("\nYou have no time to go to Mariano’s place unless you take the car. But your dad never lends you the car...")
    time.sleep(3)

    option = input("\na. Take your dad's keys 🔑️\nb. Run to the butcher🏃🏽‍♀️‍➡️️\nc. Steal your neighbor’s meat 🥩\n")
    return option
#scene 3: 3 options to solve the problem

def sc3_option_a(option):
    if option == "a":
        print("\nThe keys are where they always are... on the table by the front door. Take them without anyone noticing 👀")
        time.sleep(3)
    return option
#option a: car keys

def sc3_option_b(option):
    if option == "b":
        time.sleep(1)
        print("Let's go!🏃🏽‍♀️‍➡️")
    return option
#option b: butcher

def sc3_option_c(option):
    if option == "c":
        print("\n- I have a plan... I’m a great talker. I’ll distract the neighbor and keep him away from the house. You sneak into the kitchen, grab the meat, and put it in your fridge.")
        time.sleep(5)
        print("\nIt feels unfair that you have to do the dirty work, but your cousin has a point... You're not exactly the best talker 🫢")
        time.sleep(2)
        answer = input("Do you agree to this plan? Yes or no? 🤔")
        if answer == "yes":
            print("Let's hurry then!")
        if answer == "no":
            print("- Okay, then… Got any better ideas?")
            time.sleep(2)
            option = input("a. Take your dad’s keys 🔑️\nb. Run to the butcher 🏃‍♂️")
            if option == "a":
                sc3_option_a(option)
            if option == "b":
                time.sleep(2)
                sc3_option_b(option)
            return option
    return option
#option 3: stealing the neighbor

def scene4():
    time.sleep(3)
    print("\nOh no...Tia Marta...🙄")
    time.sleep(2)
    print("- Hello, hello! How are my angels? Where are you going? ✨")
    time.sleep(3)
    print("- Nowhere...")
    time.sleep(2)
    print("- Nowhere? No one ever goes nowhere. Anyway, say hello to your aunty, just back from the Mendoza vineyards 🍇 ⛰️\n  and brought something for you two...")
    time.sleep(7)
    print("- Aunty Marta, we really have to go.")
    time.sleep(3)
    print("- Mariano, come on, just answer this...")
    time.sleep(2)
    print("  I had 2 bottles of wine. I had one glass and saw double. I had another glass, and another, and another.🍷")
    while True:
        number = input("  How many bottles of wine do I have now, from 0 to 10? ")
        number = int(number)
        if 0 < number < 10:
            print("\n- 🚫Mmm, no darling, try again...")
        elif number > 10:
            print("\n- 🛑You’re distracted! Listen carefully, I said from 0 to 10...")
        elif number == 0:
            break

    print("\n- 🌟Hahaha, exactly! Because I 'haaad' haha, I drank them all! You’re so smart, my angels!")
    time.sleep(3)
    print("   Here’s a bottle for you two to share... because I don’t share my wine! Haha!🍷😜")
    time.sleep(4)
    print("\n- Phew! Tía Marta almost caught us 😬. She didn’t, but she slowed us down. Remember, grandma wants everything ready by 2 PM. We have to hurry!")
#Before continuing with option a/b/c: Tia Marta's riddle. (It doesn't depend on the chosen option)

#Chosen option continues

def sc3_option_a2(name,option):
    if option == "a":
        time.sleep(3)
        print("\n🚘")
        print("You’re driving and Mariano is your co-pilot.")
        time.sleep(2)
        print("- Speed up! We’re never going to make it like this!!")
        time.sleep(3)
        print("\nSPEED LIMIT 60KM")
        time.sleep(1)
        print("You speed up...🚗💨")
        time.sleep(2)
        print("\n‼️Watch out! Speed camera!")
        time.sleep(2)
        print("Did you slow down? What's your speed?")
        time.sleep(2)
        number = input("Speed (in km/h):")
        number = int(number)
        if number <= 60:
            print("\nGood, you didn’t get a fine! But now you won’t make it to the asado on time ⏰")
            time.sleep(4)
            print("\nNow, everyone is eating salad 🥗😞💔")
            time.sleep(2)
            print(name, LOSING_MESSAGE)
            again = input("  yes / no?")
            if again == "no":
                sys.exit()
            if again == "yes":
                main()

        elif number > 60:
            print("Okay, your dad’s gonna kill you for the fine...💰 but at least you'll make it to the asado on time!")
            time.sleep(3)
            print("\n- You’re the best driver ever 🫶🏼")
            time.sleep(1)
            print("  Wait here, I’m going to get the meat and we’re off!")
            time.sleep(3)
            print("\n- Okay, let’s go!")
            print("  🚘")
            print("\nYour cousin puts on some Argentine music to relax a bit 🎶")
            time.sleep(2)
            print("-", name, "What do you want to listen to?")
            time.sleep(2)
            music = input("Cumbia or Rock?️")
            if music == "cumbia":
                print("click this link ▶️: https://open.spotify.com/playlist/37i9dQZF1DWUyLwMSMFLA4?si=a88cf4fc20884ed5")
            elif music == "rock":
                print("click this link ▶️: https://open.spotify.com/playlist/3nKM1H45FbpC0FgEHflkG1?si=8a5659d712c34a62")
            time.sleep(3)
            print("\nYou finally get home in time to deliver the meat!!")
            print("         ✨🎊✨🎊✨🎊✨🎊✨🎊✨🎊✨🎊✨")
            time.sleep(2)
            print("\nBut... your dad is furious about the car.🤬😤")
            time.sleep(2)
            print("\n- Sorry Uncle, it was my fault, not", name + "’s. I forgot the meat. And I’ll pay the fine.💰")
            time.sleep(3)
            print("- Fine?!😡")
            time.sleep(2)
            print("\nRemember... you have 1 bottle of a really special wine 👀")
            time.sleep(2)
            decision = input("Do you gift it to your father? 🎁")
            if decision == "yes":
                print("\nYou are forgiven. And you all have asado together 💖🎉")
                time.sleep(4)
                print(name, WINNING_MESSAGE)
                time.sleep(2)
                print("\n    🥩 🥩      🥩 🥩")
                time.sleep(0.5)
                print("   🥩    🥩   🥩    🥩")
                time.sleep(0.5)
                print("  🥩      🥩 🥩      🥩")
                time.sleep(0.5)
                print("  🥩        🥩       🥩")
                time.sleep(0.5)
                print("   🥩       🥩      🥩")
                time.sleep(0.5)
                print("    🥩              🥩")
                time.sleep(0.5)
                print("     🥩            🥩")
                time.sleep(0.5)
                print("      🥩          🥩")
                time.sleep(0.5)
                print("       🥩        🥩")
                time.sleep(0.5)
                print("         🥩     🥩")
                time.sleep(0.5)
                print("          🥩   🥩")
                time.sleep(0.5)
                print("           🥩 🥩")
                time.sleep(0.5)
                print("             🥩")
                sys.exit()

            elif decision == "no":
                print("\nYour dad is angry.")
                time.sleep(2)
                print("He made the asado, but his bad mood ruined it...😡")
                time.sleep(3)
                print("You made it on time ⏰, but now... nobody is enjoying the asado...")
                time.sleep(3)
                print(LOSING_MESSAGE)
                again = input("  yes / no?")
                if again == "no":
                    sys.exit()
                if again == "yes":
                    main()
#option: car keys

def sc3_option_c2(name,option):
    print("\n- Okay", name,"The mission begins. I'll distract the neighbor and our parents in the garden 🤡\n  Good luck!🍀🤞🏽")
    time.sleep(4)
    print("\nYou sneak into the house quietly.👣🥷🏽\nEverything is going well. You approach the fridge and suddenly... you freeze!🥶")
    time.sleep(5)
    print("Mariano and you didn’t anticipate...")
    time.sleep(2)
    print("  🐩")
    time.sleep(1)
    print("Lola, the dog...")
    time.sleep(2)
    print("Lola starts barking at you like crazy! You don’t know what to do...")
    time.sleep(2)
    print("\n🌳Meanwhile, in the garden...")
    time.sleep(4)
    print("- Weird, why is my dog barking so much... I’ll go see what's happening 🧐")
    time.sleep(3)
    print("\nYou hear your cousin trying to stop your neighbor from coming in🫸🏼")
    time.sleep(3)
    print("You remember you have a bottle of wine...")
    time.sleep(2)
    decision3 = input("\na. Give the dog some wine to make her sleep 🐩💤\nb. Try petting her 🫳🏼")
    if decision3 == "a":
        print("\nIt worked! The dog fell asleep thanks to the wine.🍷💤")
        time.sleep(3)
        print("\nYou listen to the conversation in the garden to check if you're safe now.. 👁️")
        time.sleep(3)
        print("- But Mariano, let me go see, just for a second. She was barking a lot and suddenly stopped...")
        time.sleep(3)
        print("\nOh no! First he was worried that Lola was barking, and now because she’s not?!😱")
        time.sleep(3)
        decision4 = input("\na. You start barking 🗣️ b. You run away 🏃🏽‍♀️")
        if decision4 == "a":
            time.sleep(1)
            print("🗣🗣🗣")
            time.sleep(2)
            print("\nThe neighbor calmed down and won’t enter the house. Well done! 😌 ")
            time.sleep(3)
            print("Grab the meat and get out of there!🫳🥩")
            time.sleep(4)
            print("\nGood job! You made it!")
            print("✨🎊✨🎊✨🎊✨🎊✨🎊✨")
            time.sleep(2)
            print(name, WINNING_MESSAGE)
            time.sleep(2)
            print("\n    🥩 🥩      🥩 🥩")
            time.sleep(0.5)
            print("   🥩    🥩   🥩    🥩")
            time.sleep(0.5)
            print("  🥩      🥩 🥩      🥩")
            time.sleep(0.5)
            print("  🥩        🥩       🥩")
            time.sleep(0.5)
            print("   🥩       🥩      🥩")
            time.sleep(0.5)
            print("    🥩              🥩")
            time.sleep(0.5)
            print("     🥩            🥩")
            time.sleep(0.5)
            print("      🥩          🥩")
            time.sleep(0.5)
            print("       🥩        🥩")
            time.sleep(0.5)
            print("         🥩     🥩")
            time.sleep(0.5)
            print("          🥩   🥩")
            time.sleep(0.5)
            print("           🥩 🥩")
            time.sleep(0.5)
            print("             🥩")
            sys.exit()
        if decision4 == "b":
            time.sleep(1)
            print("\nRun as fast as you can!!")
            time.sleep(2)
            print("- Hey!", name, "What are you doing with my meat?! Come here right now!🤬")
            time.sleep(3)
            print("\nNow, everyone is eating salad 🥗😞💔")
            time.sleep(2)
            print(LOSING_MESSAGE)
            again = input("  yes / no?")
            if again == "no":
                sys.exit()
            if again == "yes":
                main()
    if decision3 == "b":
        time.sleep(1)
        print("\nThe dog won’t let you pet her")
        time.sleep(2)
        print("The neighbor enters and sees you with the meat in hand trying to pet the dog 😳")
        time.sleep(4)
        print("- What is this?!")
        time.sleep(2)
        print("\nNow, everyone is eating salad 🥗😞💔")
        time.sleep(2)
        print(LOSING_MESSAGE)
        again = input("  yes / no?")
        if again == "no":
            sys.exit()
        if again == "yes":
            main()
#option: stealing the neighbor

def sc3_option_b2(name,option):
    if option == "b":
        time.sleep(2)
        print("\nYou are about to arrive, just need to turn the corner and that's it 🤸🏽‍♀️")
        time.sleep(3)
        print("\n- Oh no,", name, "It's closed!❌")
        time.sleep(2)
        print("  What should we do now? There's no time to go to my place.")
        decision2 = input("\na.Go back empty-handed 🤲🏽 b. Steal your neighbor’s meat 🥩")
        if decision2 == "a":
            print("\nNow, everyone is eating salad 🥗😞💔")
            time.sleep(2)
            print(LOSING_MESSAGE)
            again = input("  yes / no?")
            if again == "no":
                sys.exit()
            if again == "yes":
                main()

        elif decision2 == "b":
            print("\nCome on, let's go!")
            time.sleep(2)
            print("\nYou are back at your house 🏡")
            time.sleep(2)
            sc3_option_c2
#option: butcher


def restart_from_sc1 (name, again):
    if again == yes:
        scene1()
        scene2(name)
        option = scene3()
        sc3_option_a(option)
        sc3_option_b(option)
        sc3_option_c(option)
        scene4()
        sc3_option_a_c2a(name, option)
        sc3_option_b_c2b(name, option)
        sc3_option_c6(name, option) #
#I couldn't do this :( When lose, restart from previous scene, not from the beginning.

def main():
    name = intro()
    scene1()
    scene2(name)
    option = scene3()
    sc3_option_a(option)
    sc3_option_b(option)
    option = sc3_option_c(option)
    scene4()
    sc3_option_a2 (name, option)
    sc3_option_b2 (name, option)
    sc3_option_c2(name,option)



if __name__ == "__main__":
    main()
