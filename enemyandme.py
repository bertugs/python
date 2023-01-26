import random

print("Set veriable!\n")
playerHealt = int(input("Set player healt: "))
enemyHealt = int(input("Set enemy healt: "))
ammoDamage = int(input("Set ammo damage: "))
ammoCount = int(input("Set ammo count: "))
print("\n")
rounds = 1
playerLifeInt = playerHealt

print("GAME STARTED!\n")
print("1. Round started")
while enemyHealt > 0:
    fire = int(input("How many bullets will you shoot: "))
    if fire <= ammoCount and fire > 0:
        enemyDamage = random.randint(0,playerLifeInt)
        ammoCount -= fire
        getDamage = fire * ammoDamage
        enemyHealt -= getDamage
        playerHealt -= enemyDamage
        print("Enemy healt: " + str(enemyHealt))
        print("Ammo count: " + str(ammoCount))
        print("Your healt: " + str(playerHealt)+"\n")
        if ammoCount == 0 or playerHealt <= 0:
            break
        else:
            rounds += 1
            print(str(rounds) + ". Round started")
    else:
        print("Not enouh bullets!\n")

if playerHealt > 0:
    print("YOU WIN!")
    skore = print("Your skore:" + str(10 * rounds))
    
else:
    print("YOU LOSE!")