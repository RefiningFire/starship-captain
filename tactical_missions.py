def duel_target_ship(player_hull, target_hull):
    print("Player Hull: " + str(player_hull))
    print("Target Hull: " + str(target_hull))
    locked_in_combat = True
    if locked_in_combat == True:
        if target_hull > 0 and player_hull > 0:
            print("What is your Command, sir?")
            print("Fire - 1 | Evade - 2 | Shields Up - 3")
            chosen_action = int(input("Command: "))
        elif target_hull <= 0 and player_hull >0:
            print("You Win!")
            locked_in_combat = False
        elif target_hull > 0 and player_hull <= 0:
            print("You Lose...")
            locked_in_combat = False
