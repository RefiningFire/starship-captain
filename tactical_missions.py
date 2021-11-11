def duel_target_ship(target_name, target_hull, target_armor, target_shields, target_power, target_systems):
    print("Target Name: " + target_name)
    print("Target Hull: " + str(target_hull))
    print("Target Armor: " + str(target_armor))
    print("Target Shields: " + str(target_shields))
    print("Target Power: " + str(target_power))
    print("Target Systems: " + str(target_systems))
    locked_in_combat = True
    while locked_in_combat == True:
        if target_hull > 0 and hull > 0:
            print("Both Hull and Target Hull > 0")
