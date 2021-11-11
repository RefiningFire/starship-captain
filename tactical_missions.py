def duel_target_ship(player_hull, player_armor, player_shields, player_power, player_systems, target_name, target_hull, target_armor, target_shields, target_power, target_systems):
    print("Player Hull: " + str(player_hull))
    print("Player Armor: " + str(player_armor))
    print("Player Shields: " + str(player_shields))
    print("Player Power: " + str(player_power))
    print("Player Systems: " + str(player_systems))
    print("Target Name: " + target_name)
    print("Target Hull: " + str(target_hull))
    print("Target Armor: " + str(target_armor))
    print("Target Shields: " + str(target_shields))
    print("Target Power: " + str(target_power))
    print("Target Systems: " + str(target_systems))
    locked_in_combat = True
    while locked_in_combat == True:
        if target_hull > 0 and player_hull > 0:
            print("Both Hull and Target Hull > 0")
