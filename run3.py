name = input("What is your name? ")
print("Welcome", name, "to your travel adventure")

answer = input("You have the option to travel by air, sea, or campervan. Which do you choose? (plane/boat/campervan) ").lower()

if answer == "plane":
    print("You were involved in a catastrophic plane crash. You made the wrong choice.")
    
elif answer == "boat":
    answer = input("You chose to travel by boat. Which one will you take? (speedboat/yacht/fishing boat) ").lower()
    
    if answer == "speedboat":
        print("You're racing through the waves and having a blast! Your fuel tank wasn't euipt for such a long journey")
    elif answer == "yacht":
        print("I'm sorry, whales have been targeting yachts, and unfortunately, one has damaged your boat.")
    elif answer == "fishing boat":
        answer = input("Great choice! The fisherman is a skilled seaman. Where do you want to go? (nearest coastal town/island) ").lower()
        
        if answer == "nearest coastal town":
            print("You arrive safely at the coastal town and enjoy the local seafood.")
        elif answer == "island":
            answer = input ("You embark on a remote island adventure. What do you want to explore? (natives/wildlife/herbs)").lower()
                
            if answer == "natives":
                print("You get eaten, the tribe have always been cannibals")

            elif answer == "wildlife":
                print()
                
            elif answer == "herbs":
                print()

            else:
                print("Invalid choice. Game Over!")
    else:
        print("Invalid choice. Game Over!")
            
elif answer == "campervan":
    answer = input("You have so much choice in your campervan. Where do you want to explore first? (Africa/Eastern Europe) ").lower()
    
    if answer == "africa":
        print("You're off on a safari adventure through the African savannah!")
    elif answer == "eastern europe":
        answer = input ("You'll explore the rich history and culture of Eastern Europe. Where do you want to go first? (Poland/Slovenia)")
        if answer == "Poland":
            print()
        elif answer == "Slovenia":
            print()

        else:
            print("Invalid choice. Game Over!")
    else:
        print("Invalid choice. Game Over!")

else:
    print("Invalid choice for your mode of travel.")
