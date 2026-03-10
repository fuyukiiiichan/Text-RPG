# ΣΕΝΑΡΙΟ:
# Ο παίκτης φτιάχνει έναν χαρακτήρα (Hero) με δικά του stats.
# Το παιχνίδι δημιουργεί έναν εχθρό (Enemy) με ΤΥΧΑΙΑ stats.
# Μετά γίνεται μια “μάχη” 1 γύρου (ένα attack ο Hero και ένα attack ο Enemy)
# και βγαίνει αποτέλεσμα ανάλογα με τα stats.
# ΕΠΙΤΡΕΠΕΤΑΙ:
# - input(), print(), μεταβλητές, strings
# - int(), float()
# - πράξεις: +, -, *, /, //, %, **
# - random (randint)
# - if 
# ΔΕΝ ΧΡΕΙΑΖΕΤΑΙ:
# - loops
# - λίστες
# ------------------------------------------------------------
# 1) HERO: ΖΗΤΑ ΑΠΟ ΤΟΝ ΧΡΗΣΤΗ
# - hero_name (string)
# - hero_class (string) (Warrior/Mage/Rogue ή ό,τι θέλει)
# - strength (int)  1-20
# - crit (int)   1-20
# - intelligence (int) 1-20
# ------------------------------------------------------------
# 2) ENEMY:  ΤΥΧΑΙΑ
# - enemy_name:  "Goblin", "Skeleton", "Dark Mage", "Wolf"
# - enemy_strength = random.randint(5, 18)
# - enemy_agility  = random.randint(5, 18)
# - enemy_intelligence = random.randint(5, 18)
# ------------------------------------------------------------
from random import randint
from time import sleep
classesdict = {
    "warrior":{
        "Strenght": 8,
        "Critical": 3,
        "Intelligence": 1,
        "Agillity": 2
    },
    "mage":{
        "Strenght":3,
        "Critical":4,
        "Intelligence": 8,
        "Agillity":3
    },
    "rogue":{
        "Strenght":2,
        "Critical":6,
        "Intelligence":7,
        "Agillity":6
    }
}
Enemydict = {
    "Grass Fields":{
        "Baby Wolf":{
            "HP":randint(14,19),
            "Strenght":randint(10,20),
            "XP":randint(5,15),
            "Coins":randint(5,10)
        },
        "Weak Goblin":{
            "HP":randint(15,20),
            "Strenght":randint(10,22),
            "XP":randint(10,20),
            "Coins":randint(5,15)
        },
        "Wolf":{
            "HP":randint(17,25),
            "Strenght":randint(10,20),
            "XP":randint(10,25),
            "Coins":randint(10,20)
        }
    },
    "Village":{
        "Villager":{
            "HP":randint(15,20),
            "Strenght":randint(15,24),
            "XP":randint(15,30),
            "Coins":randint(10,30)
        },
        "Goblin":{
            "HP":randint(20,25),
            "Strenght":randint(20,25),
            "XP":randint(15,30),
            "Coins":randint(20,35)
        }
    },
    "Cave":{
        "Skeleton":{
            "HP":randint(23,30),
            "Strenght":randint(23,40),
            "XP":randint(30,50),
            "Coins":randint(35,50)
        },
        "Dark Mage":{
            "HP":randint(30,40),
            "Strenght":randint(35,50),
            "XP":randint(40,60),
            "Coins":randint(45,70)
        }
    },
    "Gladiator Arena":{
        "Lion":{
        "HP":randint(45,70),
        "Strenght":randint(50,75),
        "XP":randint(50,75),
        "Coins":randint(50,75)
        },
        "Gladiator":{
            "HP":randint(55,90),
            "Strenght":randint(55,95),
            "XP":randint(60,80),
            "Coins":randint(65,90)
        },
    },
    "Kings Castle":{
        "Lower Guards":{
            "HP":randint(100,120),
            "Strenght":randint(55,95),
            "XP":randint(65,85),
            "Coins":randint(80,100)
        },
        "Upper Guards":{
            "HP":randint(75,100),
            "Strenght":randint(70,150),
            "XP":randint(70,90),
            "Coins":randint(80,110)
        },
        "King":{
            "HP":randint(150,210),
            "Strenght":randint(150,210),
            "XP":randint(75,95),
            "Coins":randint(90,115)
        }
    },
    "Zeus":{
        "Zeus":{
            "HP":randint(300,550),
            "Strenght":randint(200,450),
            "XP":randint(150,200),
            "Coins":randint(200,300)
        }
    },
    "Daemon":{
        "Daemon":{
            "HP":randint(700,1000),
            "Strenght":randint(400,850),
            "XP":randint(450,500),
            "Coins":randint(500,700)
        }
    }
}
XP = 0
maxhp = 100
HP = maxhp
coins = 0
Arenas = ["Grass Fields","Village","Cave","Gladiator Arena","Kings Castle","Olympus","Peak Olympus"]
def shop(HP, Strenght, Agillity, Intelligence, Critical, coins, maxhp):
    print("Welcome to the shop!")
    print("1) Basic Strenght Potion: +5 Strenght | 150 Coins ")
    print("2) Basic Health Potion: +30 Health | 150 Coins ")
    print("3) Basic Intelligence Potion: +5 Intelligence | 150 Coins ")
    print("4) Rare Strenght Potion: +15 Strenght | 300 Coins ")
    print("5) Rare Health Potion: +50 Health | 300 Coins ")
    print("6) Rare Intelligence Potion: +15 Intelligence | 300 Coins ")
    print("7) Elite Strenght Potion: +30 Strenght | 750 Coins ")
    print("8) Elite Health Potion: +100 Health | 750 Coins ")
    print("9) Elite Intelligence Potion: +30 Intelligence | 750  Coins ")
    while True:
        try:
            choice = int(input(""))
            break
        except ValueError:
            print("Error! Choose a number")
    if choice == 1:
        if coins >= 150:
            coins -= 150
            Strenght +=5
        else:
            print("Not enough coins!")
    elif choice == 2:
        if coins >=150:
            coins-=150
            maxhp += 30
        else:
            print("Not enough coins!")
    elif choice == 3:
        if coins >=150:
            coins-=150
            Intelligence += 5
        else:
            print("Not enough coins!")
    elif choice == 4:
        if coins >= 300:
            coins-=300
            Strenght += 13
        else:
            print("Not enough coins!")
    elif choice == 5:
        if coins >= 300:
            coins -= 300
            maxhp += 50
        else:
            print("Not enough coins!")
    elif choice == 6:
        if coins >= 300:
            coins-=300
            Intelligence += 13
        else:
            print("Not enough coins!")
    elif choice == 7:
        if coins >=750:
            coins-=750
            Strenght += 35
        else:
            print("Not enough coins!")
    elif choice == 8:
        if coins >= 750:
            coins -= 750
            maxhp += 100
        else:
            print("Not enough coins!")
    elif choice == 9:
        if coins >=750:
            coins-=750
            Intelligence += 45
        else:
            print("Not enough coins!")
    else:
        print("Invalid choice!")
    return (HP, Strenght, Agillity, Intelligence, Critical, coins,maxhp)
def arena(XP):
    multi = 1
    for i in range(len(Arenas)):
        if i == 0:
            pass
        else:
            if XP >= i*100*multi:
                pass
            else:
                return i+1
        print(f"{i+1}){Arenas[i]}")
        multi += i*1.5
def Grass_Fields(XP, HP, Strenght, Agillity, Intelligence, Critical, coins):
    print("You just spawned at Grass Fields")
    print("1) Fight")
    print("2) Exit")
    while True:
        try:
            choice = int(input(""))
            break
        except ValueError:
            print("Error! Enter a number")

    if choice == 1:
        spawnorder = ["Baby Wolf", "Weak Goblin", "Wolf"]
        for enemies in spawnorder:
            enemy_strenght = Enemydict["Grass Fields"][enemies]["Strenght"]
            enemy_hp = Enemydict["Grass Fields"][enemies]["HP"]
            enemy_coins = Enemydict["Grass Fields"][enemies]["Coins"]
            enemy_xp = Enemydict["Grass Fields"][enemies]["XP"]
            print(f"A Wild {enemies} Has Appeared!")
            print(f"You're fighting {enemies}")
            print(f"Hero HP: {HP}")
            print(f"{enemies} HP: {enemy_hp}")
            print(f"{enemies} Attack: {enemy_strenght}")
            print("1) Attack")
            print("2) Run Away")
            while True:
                try:
                    choice = int(input(""))
                    break
                except ValueError:
                    print("Error! Choose a number")
            if choice == 1:
                heroattack = randint(Strenght - 1, Strenght + 10)
                critical_chance = randint(Critical, 100)
                if critical_chance == 100:
                    heroattack += heroattack * 0.2
                    is_critical = True
                else:
                    is_critical = False
                attackorder = randint(1, 2)
                if attackorder == 1:
                    print(f"{name} attacks first!")
                    sleep(0.5)
                    enemy_hp -= heroattack
                    if is_critical:
                        print(f"Critical! {name} Dealt {heroattack} to {enemies}")
                    else:
                        print(f"{name} Dealt {heroattack} to {enemies}")
                    sleep(0.5)
                    if enemy_hp > 0:
                        print(f"{enemies} Attacks!")
                        sleep(0.5)
                        HP -= enemy_strenght
                        print(f"{enemies} Dealt {enemy_strenght} to {name}")
                        sleep(0.5)
                else:
                    print(f"{enemies} attacks first!")
                    sleep(0.5)
                    HP -= enemy_strenght
                    print(f"{enemies} Dealt {enemy_strenght} to {name}")
                    sleep(0.5)
                    if HP > 0:
                        print(f"{name} Attacks!")
                        sleep(0.5)
                        enemy_hp -= heroattack
                        if is_critical:
                            print(f"Critical! {name} Dealt {heroattack} to {enemies}")
                        else:
                            print(f"{name} Dealt {heroattack} to {enemies}")
                        sleep(0.5)
                if HP <= 0:
                    print("You've Died!")
                    sleep(0.5)
                    return (XP, HP, Strenght, Agillity, Intelligence, Critical, coins)
                if enemy_hp <= 0:
                    earned_xp = enemy_xp + Intelligence * 0.1
                    earned_coins = enemy_coins + Intelligence * 0.1
                    print(f"You beat {enemies}")
                    print(f"{earned_xp} XP Gained")
                    print(f"{earned_coins} Coins Earned")
                    XP += enemy_xp + Intelligence * 0.1
                    coins += enemy_coins + Intelligence * 0.1
                    sleep(0.5)
            elif choice == 2:
                print("You ran away safely!")
                sleep(0.5)
                return (XP, HP, Strenght, Agillity, Intelligence, Critical, coins)
            else:
                print("Invalid choice!")
                return (XP, HP, Strenght, Agillity, Intelligence, Critical, coins)
    return (XP, HP, Strenght, Agillity, Intelligence, Critical, coins)
def Village(XP, HP, Strenght, Agillity, Intelligence, Critical, coins):
    print("You just spawned at Village")
    print("1) Fight")
    print("2) Exit")
    while True:
        try:
            choice = int(input(""))
            break
        except ValueError:
            print("Error! Enter a number")

    if choice == 1:
        spawnorder = ["Villager", "Goblin"]
        for enemies in spawnorder:
            enemy_strenght = Enemydict["Village"][enemies]["Strenght"]
            enemy_hp = Enemydict["Village"][enemies]["HP"]
            enemy_coins = Enemydict["Village"][enemies]["Coins"]
            enemy_xp = Enemydict["Village"][enemies]["XP"]
            print(f"A Wild {enemies} Has Appeared!")
            print(f"You're fighting {enemies}")
            print(f"Hero HP: {HP}")
            print(f"{enemies} HP: {enemy_hp}")
            print(f"{enemies} Attack: {enemy_strenght}")
            print("1) Attack")
            print("2) Run Away")
            while True:
                try:
                    choice = int(input(""))
                    break
                except ValueError:
                    print("Error! Choose a number")
            if choice == 1:
                heroattack = randint(Strenght - 1, Strenght + 10)
                critical_chance = randint(Critical, 100)
                if critical_chance == 100:
                    heroattack += heroattack * 0.2
                    is_critical = True
                else:
                    is_critical = False
                attackorder = randint(1, 2)
                if attackorder == 1:
                    print(f"{name} attacks first!")
                    sleep(0.5)
                    enemy_hp -= heroattack
                    if is_critical:
                        print(f"Critical! {name} Dealt {heroattack} to {enemies}")
                    else:
                        print(f"{name} Dealt {heroattack} to {enemies}")
                    sleep(0.5)
                    if enemy_hp > 0:
                        print(f"{enemies} Attacks!")
                        sleep(0.5)
                        HP -= enemy_strenght
                        print(f"{enemies} Dealt {enemy_strenght} to {name}")
                        sleep(0.5)
                else:
                    print(f"{enemies} attacks first!")
                    sleep(0.5)
                    HP -= enemy_strenght
                    print(f"{enemies} Dealt {enemy_strenght} to {name}")
                    sleep(0.5)
                    if HP > 0:
                        print(f"{name} Attacks!")
                        sleep(0.5)
                        enemy_hp -= heroattack
                        if is_critical:
                            print(f"Critical! {name} Dealt {heroattack} to {enemies}")
                        else:
                            print(f"{name} Dealt {heroattack} to {enemies}")
                        sleep(0.5)
                if HP <= 0:
                    print("You've Died!")
                    sleep(0.5)
                    return (XP, HP, Strenght, Agillity, Intelligence, Critical, coins)
                if enemy_hp <= 0:
                    earned_xp = enemy_xp + Intelligence * 0.1
                    earned_coins = enemy_coins + Intelligence * 0.1
                    print(f"You beat {enemies}")
                    print(f"{earned_xp} XP Gained")
                    print(f"{earned_coins} Coins Earned")
                    XP += enemy_xp + Intelligence * 0.1
                    coins += enemy_coins + Intelligence * 0.1
                    sleep(0.5)
            elif choice == 2:
                print("You ran away safely!")
                sleep(0.5)
                return (XP, HP, Strenght, Agillity, Intelligence, Critical, coins)
            else:
                print("Invalid choice!")
                return (XP, HP, Strenght, Agillity, Intelligence, Critical, coins)
    return (XP, HP, Strenght, Agillity, Intelligence, Critical, coins)
def Cave(XP, HP, Strenght, Agillity, Intelligence, Critical, coins):
    print("You just spawned at Cave")
    print("1) Fight")
    print("2) Exit")
    while True:
        try:
            choice = int(input(""))
            break
        except ValueError:
            print("Error! Enter a number")

    if choice == 1:
        spawnorder = ["Skeleton", "Dark Mage"]
        for enemies in spawnorder:
            enemy_strenght = Enemydict["Cave"][enemies]["Strenght"]
            enemy_hp = Enemydict["Cave"][enemies]["HP"]
            enemy_coins = Enemydict["Cave"][enemies]["Coins"]
            enemy_xp = Enemydict["Cave"][enemies]["XP"]
            print(f"A Wild {enemies} Has Appeared!")
            print(f"You're fighting {enemies}")
            print(f"Hero HP: {HP}")
            print(f"{enemies} HP: {enemy_hp}")
            print(f"{enemies} Attack: {enemy_strenght}")
            print("1) Attack")
            print("2) Run Away")
            while True:
                try:
                    choice = int(input(""))
                    break
                except ValueError:
                    print("Error! Choose a number")
            if choice == 1:
                heroattack = randint(Strenght - 1, Strenght + 10)
                critical_chance = randint(Critical, 100)
                if critical_chance == 100:
                    heroattack += heroattack * 0.2
                    is_critical = True
                else:
                    is_critical = False
                attackorder = randint(1, 2)
                if attackorder == 1:
                    print(f"{name} attacks first!")
                    sleep(0.5)
                    enemy_hp -= heroattack
                    if is_critical:
                        print(f"Critical! {name} Dealt {heroattack} to {enemies}")
                    else:
                        print(f"{name} Dealt {heroattack} to {enemies}")
                    sleep(0.5)
                    if enemy_hp > 0:
                        print(f"{enemies} Attacks!")
                        sleep(0.5)
                        HP -= enemy_strenght
                        print(f"{enemies} Dealt {enemy_strenght} to {name}")
                        sleep(0.5)
                else:
                    print(f"{enemies} attacks first!")
                    sleep(0.5)
                    HP -= enemy_strenght
                    print(f"{enemies} Dealt {enemy_strenght} to {name}")
                    sleep(0.5)
                    if HP > 0:
                        print(f"{name} Attacks!")
                        sleep(0.5)
                        enemy_hp -= heroattack
                        if is_critical:
                            print(f"Critical! {name} Dealt {heroattack} to {enemies}")
                        else:
                            print(f"{name} Dealt {heroattack} to {enemies}")
                        sleep(0.5)
                if HP <= 0:
                    print("You've Died!")
                    sleep(0.5)
                    return (XP, HP, Strenght, Agillity, Intelligence, Critical, coins)
                if enemy_hp <= 0:
                    earned_xp = enemy_xp + Intelligence * 0.1
                    earned_coins = enemy_coins + Intelligence * 0.1
                    print(f"You beat {enemies}")
                    print(f"{earned_xp} XP Gained")
                    print(f"{earned_coins} Coins Earned")
                    XP += enemy_xp + Intelligence * 0.1
                    coins += enemy_coins + Intelligence * 0.1
                    sleep(0.5)
            elif choice == 2:
                print("You ran away safely!")
                sleep(0.5)
                return (XP, HP, Strenght, Agillity, Intelligence, Critical, coins)
            else:
                print("Invalid choice!")
                return (XP, HP, Strenght, Agillity, Intelligence, Critical, coins)
    return (XP, HP, Strenght, Agillity, Intelligence, Critical, coins)
def Gladiator_Arena(XP, HP, Strenght, Agillity, Intelligence, Critical, coins):
    print("You just spawned at Gladiator Arena")
    print("1) Fight")
    print("2) Exit")
    while True:
        try:
            choice = int(input(""))
            break
        except ValueError:
            print("Error! Enter a number")
    if choice == 1:
        spawnorder = ["Lion","Gladiator"]
        for enemies in spawnorder:
            enemy_strenght = Enemydict["Gladiator Arena"][enemies]["Strenght"]
            enemy_hp = Enemydict["Gladiator Arena"][enemies]["HP"]
            enemy_coins = Enemydict["Gladiator Arena"][enemies]["Coins"]
            enemy_xp = Enemydict["Gladiator Arena"][enemies]["XP"]
            print(f"A Wild {enemies} Has Appeared!")
            print(f"You're fighting {enemies}")
            print(f"Hero HP: {HP}")
            print(f"{enemies} HP: {enemy_hp}")
            print(f"{enemies} Attack: {enemy_strenght}")
            print("1) Attack")
            print("2) Run Away")
            while True:
                try:
                    choice = int(input(""))
                    break
                except ValueError:
                    print("Error! Choose a number")
            if choice == 1:
                heroattack = randint(Strenght - 1, Strenght + 10)
                critical_chance = randint(Critical, 100)
                if critical_chance == 100:
                    heroattack += heroattack * 0.2
                    is_critical = True
                else:
                    is_critical = False
                attackorder = randint(1, 2)
                if attackorder == 1:
                    print(f"{name} attacks first!")
                    sleep(0.5)
                    enemy_hp -= heroattack
                    if is_critical:
                        print(f"Critical! {name} Dealt {heroattack} to {enemies}")
                    else:
                        print(f"{name} Dealt {heroattack} to {enemies}")
                    sleep(0.5)
                    if enemy_hp > 0:
                        print(f"{enemies} Attacks!")
                        sleep(0.5)
                        HP -= enemy_strenght
                        print(f"{enemies} Dealt {enemy_strenght} to {name}")
                        sleep(0.5)
                else:
                    print(f"{enemies} attacks first!")
                    sleep(0.5)
                    HP -= enemy_strenght
                    print(f"{enemies} Dealt {enemy_strenght} to {name}")
                    sleep(0.5)
                    if HP > 0:
                        print(f"{name} Attacks!")
                        sleep(0.5)
                        enemy_hp -= heroattack
                        if is_critical:
                            print(f"Critical! {name} Dealt {heroattack} to {enemies}")
                        else:
                            print(f"{name} Dealt {heroattack} to {enemies}")
                        sleep(0.5)
                if HP <= 0:
                    print("You've Died!")
                    sleep(0.5)
                    return (XP, HP, Strenght, Agillity, Intelligence, Critical, coins)
                if enemy_hp <= 0:
                    earned_xp = enemy_xp + Intelligence * 0.1
                    earned_coins = enemy_coins + Intelligence * 0.1
                    print(f"You beat {enemies}")
                    print(f"{earned_xp} XP Gained")
                    print(f"{earned_coins} Coins Earned")
                    XP += enemy_xp + Intelligence * 0.1
                    coins += enemy_coins + Intelligence * 0.1
                    sleep(0.5)
            elif choice == 2:
                print("You ran away safely!")
                sleep(0.5)
                return (XP, HP, Strenght, Agillity, Intelligence, Critical, coins)
            else:
                print("Invalid choice!")
                return (XP, HP, Strenght, Agillity, Intelligence, Critical, coins)
    return (XP, HP, Strenght, Agillity, Intelligence, Critical, coins)
def Kings_Castle(XP, HP, Strenght, Agillity, Intelligence, Critical, coins):
    print("You just spawned at Kings Castle")
    print("1) Fight")
    print("2) Exit")
    while True:
        try:
            choice = int(input(""))
            break
        except ValueError:
            print("Error! Enter a number")

    if choice == 1:
        spawnorder = ["Lower Guards", "Upper Guards","King"]
        for enemies in spawnorder:
            enemy_strenght = Enemydict["Kings Castle"][enemies]["Strenght"]
            enemy_hp = Enemydict["Kings Castle"][enemies]["HP"]
            enemy_coins = Enemydict["Kings Castle"][enemies]["Coins"]
            enemy_xp = Enemydict["Kings Castle"][enemies]["XP"]
            print(f"A Wild {enemies} Has Appeared!")
            print(f"You're fighting {enemies}")
            print(f"Hero HP: {HP}")
            print(f"{enemies} HP: {enemy_hp}")
            print(f"{enemies} Attack: {enemy_strenght}")
            print("1) Attack")
            print("2) Run Away")
            while True:
                try:
                    choice = int(input(""))
                    break
                except ValueError:
                    print("Error! Choose a number")
            if choice == 1:
                heroattack = randint(Strenght - 1, Strenght + 10)
                critical_chance = randint(Critical, 100)
                if critical_chance == 100:
                    heroattack += heroattack * 0.2
                    is_critical = True
                else:
                    is_critical = False
                attackorder = randint(1, 2)
                if attackorder == 1:
                    print(f"{name} attacks first!")
                    sleep(0.5)
                    enemy_hp -= heroattack
                    if is_critical:
                        print(f"Critical! {name} Dealt {heroattack} to {enemies}")
                    else:
                        print(f"{name} Dealt {heroattack} to {enemies}")
                    sleep(0.5)
                    if enemy_hp > 0:
                        print(f"{enemies} Attacks!")
                        sleep(0.5)
                        HP -= enemy_strenght
                        print(f"{enemies} Dealt {enemy_strenght} to {name}")
                        sleep(0.5)
                else:
                    print(f"{enemies} attacks first!")
                    sleep(0.5)
                    HP -= enemy_strenght
                    print(f"{enemies} Dealt {enemy_strenght} to {name}")
                    sleep(0.5)
                    if HP > 0:
                        print(f"{name} Attacks!")
                        sleep(0.5)
                        enemy_hp -= heroattack
                        if is_critical:
                            print(f"Critical! {name} Dealt {heroattack} to {enemies}")
                        else:
                            print(f"{name} Dealt {heroattack} to {enemies}")
                        sleep(0.5)
                if HP <= 0:
                    print("You've Died!")
                    sleep(0.5)
                    return (XP, HP, Strenght, Agillity, Intelligence, Critical, coins)
                if enemy_hp <= 0:
                    earned_xp = enemy_xp + Intelligence * 0.1
                    earned_coins = enemy_coins + Intelligence * 0.1
                    print(f"You beat {enemies}")
                    print(f"{earned_xp} XP Gained")
                    print(f"{earned_coins} Coins Earned")
                    XP += enemy_xp + Intelligence * 0.1
                    coins += enemy_coins + Intelligence * 0.1
                    sleep(0.5)
            elif choice == 2:
                print("You ran away safely!")
                sleep(0.5)
                return (XP, HP, Strenght, Agillity, Intelligence, Critical, coins)
            else:
                print("Invalid choice!")
                return (XP, HP, Strenght, Agillity, Intelligence, Critical, coins)
    return (XP, HP, Strenght, Agillity, Intelligence, Critical, coins)
def Zeus(XP, HP, Strenght, Agillity, Intelligence, Critical, coins):
    print("You just spawned at Olympus")
    print("1) Fight")
    print("2) Exit")
    while True:
        try:
            choice = int(input(""))
            break
        except ValueError:
            print("Error! Enter a number")

    if choice == 1:
        spawnorder = ["Zeus"]
        for enemies in spawnorder:
            enemy_strenght = Enemydict["Zeus"][enemies]["Strenght"]
            enemy_hp = Enemydict["Zeus"][enemies]["HP"]
            enemy_coins = Enemydict["Zeus"][enemies]["Coins"]
            enemy_xp = Enemydict["Zeus"][enemies]["XP"]
            print(f"A Wild {enemies} Has Appeared!")
            print(f"You're fighting {enemies}")
            print(f"Hero HP: {HP}")
            print(f"{enemies} HP: {enemy_hp}")
            print(f"{enemies} Attack: {enemy_strenght}")
            print("1) Attack")
            print("2) Run Away")
            while True:
                try:
                    choice = int(input(""))
                    break
                except ValueError:
                    print("Error! Choose a number")
            if choice == 1:
                heroattack = randint(Strenght - 1, Strenght + 10)
                critical_chance = randint(Critical, 100)
                if critical_chance == 100:
                    heroattack += heroattack * 0.2
                    is_critical = True
                else:
                    is_critical = False
                attackorder = randint(1, 2)
                if attackorder == 1:
                    print(f"{name} attacks first!")
                    sleep(0.5)
                    enemy_hp -= heroattack
                    if is_critical:
                        print(f"Critical! {name} Dealt {heroattack} to {enemies}")
                    else:
                        print(f"{name} Dealt {heroattack} to {enemies}")
                    sleep(0.5)
                    if enemy_hp > 0:
                        print(f"{enemies} Attacks!")
                        sleep(0.5)
                        HP -= enemy_strenght
                        print(f"{enemies} Dealt {enemy_strenght} to {name}")
                        sleep(0.5)
                else:
                    print(f"{enemies} attacks first!")
                    sleep(0.5)
                    HP -= enemy_strenght
                    print(f"{enemies} Dealt {enemy_strenght} to {name}")
                    sleep(0.5)
                    if HP > 0:
                        print(f"{name} Attacks!")
                        sleep(0.5)
                        enemy_hp -= heroattack
                        if is_critical:
                            print(f"Critical! {name} Dealt {heroattack} to {enemies}")
                        else:
                            print(f"{name} Dealt {heroattack} to {enemies}")
                        sleep(0.5)
                if HP <= 0:
                    print("You've Died!")
                    sleep(0.5)
                    return (XP, HP, Strenght, Agillity, Intelligence, Critical, coins)
                if enemy_hp <= 0:
                    earned_xp = enemy_xp + Intelligence * 0.1
                    earned_coins = enemy_coins + Intelligence * 0.1
                    print(f"You beat {enemies}")
                    print(f"{earned_xp} XP Gained")
                    print(f"{earned_coins} Coins Earned")
                    XP += enemy_xp + Intelligence * 0.1
                    coins += enemy_coins + Intelligence * 0.1
                    sleep(0.5)
            elif choice == 2:
                print("You ran away safely!")
                sleep(0.5)
                return (XP, HP, Strenght, Agillity, Intelligence, Critical, coins)
            else:
                print("Invalid choice!")
                return (XP, HP, Strenght, Agillity, Intelligence, Critical, coins)
    return (XP, HP, Strenght, Agillity, Intelligence, Critical, coins)
def Daemon(XP, HP, Strenght, Agillity, Intelligence, Critical, coins):
    print("You just spawned at Peak Olympus")
    print("1) Fight")
    print("2) Exit")
    while True:
        try:
            choice = int(input(""))
            break
        except ValueError:
            print("Error! Enter a number")

    if choice == 1:
        spawnorder = ["Daemon"]
        for enemies in spawnorder:
            enemy_strenght = Enemydict["Daemon"][enemies]["Strenght"]
            enemy_hp = Enemydict["Daemon"][enemies]["HP"]
            enemy_coins = Enemydict["Daemon"][enemies]["Coins"]
            enemy_xp = Enemydict["Daemon"][enemies]["XP"]
            print(f"A Wild {enemies} Has Appeared!")
            print(f"You're fighting {enemies}")
            print(f"Hero HP: {HP}")
            print(f"{enemies} HP: {enemy_hp}")
            print(f"{enemies} Attack: {enemy_strenght}")
            print("1) Attack")
            print("2) Run Away")
            while True:
                try:
                    choice = int(input(""))
                    break
                except ValueError:
                    print("Error! Choose a number")
            if choice == 1:
                heroattack = randint(Strenght - 1, Strenght + 10)
                critical_chance = randint(Critical, 100)
                if critical_chance == 100:
                    heroattack += heroattack * 0.2
                    is_critical = True
                else:
                    is_critical = False
                attackorder = randint(1, 2)
                if attackorder == 1:
                    print(f"{name} attacks first!")
                    sleep(0.5)
                    enemy_hp -= heroattack
                    if is_critical:
                        print(f"Critical! {name} Dealt {heroattack} to {enemies}")
                    else:
                        print(f"{name} Dealt {heroattack} to {enemies}")
                    sleep(0.5)
                    if enemy_hp > 0:
                        print(f"{enemies} Attacks!")
                        sleep(0.5)
                        HP -= enemy_strenght
                        print(f"{enemies} Dealt {enemy_strenght} to {name}")
                        sleep(0.5)
                else:
                    print(f"{enemies} attacks first!")
                    sleep(0.5)
                    HP -= enemy_strenght
                    print(f"{enemies} Dealt {enemy_strenght} to {name}")
                    sleep(0.5)
                    if HP > 0:
                        print(f"{name} Attacks!")
                        sleep(0.5)
                        enemy_hp -= heroattack
                        if is_critical:
                            print(f"Critical! {name} Dealt {heroattack} to {enemies}")
                        else:
                            print(f"{name} Dealt {heroattack} to {enemies}")
                        sleep(0.5)
                if HP <= 0:
                    print("You've Died!")
                    sleep(0.5)
                    return (XP, HP, Strenght, Agillity, Intelligence, Critical, coins)
                if enemy_hp <= 0:
                    earned_xp = enemy_xp + Intelligence * 0.1
                    earned_coins = enemy_coins + Intelligence * 0.1
                    print(f"You beat {enemies}")
                    print(f"{earned_xp} XP Gained")
                    print(f"{earned_coins} Coins Earned")
                    XP += enemy_xp + Intelligence * 0.1
                    coins += enemy_coins + Intelligence * 0.1
                    sleep(0.5)
            elif choice == 2:
                print("You ran away safely!")
                sleep(0.5)
                return (XP, HP, Strenght, Agillity, Intelligence, Critical, coins)
            else:
                print("Invalid choice!")
                return (XP, HP, Strenght, Agillity, Intelligence, Critical, coins)
    return (XP, HP, Strenght, Agillity, Intelligence, Critical, coins)
def play(XP,HP, Strenght, Agillity, Intelligence,Critical, coins):
    arena(XP)
    while True:
        try:
            choice = int(input(""))
            break
        except ValueError:
            print("Error! Choose a number")
    if choice == 1 and XP>=0:
        return Grass_Fields(XP,HP, Strenght, Agillity, Intelligence,Critical,coins)
    elif choice == 2 and XP>100:
        return Village(XP,HP,Strenght,Agillity,Intelligence,Critical,coins)
    elif choice == 3 and XP>500:
        return Cave(XP,HP,Strenght,Agillity,Intelligence,Critical,coins)
    elif choice == 4 and XP>1650:
        return Gladiator_Arena(XP,HP,Strenght,Agillity,Intelligence,Critical,coins)
    elif choice == 5 and XP>4000:
        return Kings_Castle(XP,HP,Strenght,Agillity,Intelligence,Critical,coins)
    elif choice == 6 and XP>8000:
        return Zeus(XP,HP,Strenght,Agillity,Intelligence,Critical,coins)
    elif choice == 7 and XP>14100:
        return Daemon(XP,HP,Strenght,Agillity,Intelligence,Critical,coins)
    else:
        return (XP, HP, Strenght, Agillity, Intelligence, Critical, coins)
    
def stats(name,XP,HP, Strenght, Agillity, Intelligence,Critical,coins,maxhp):
    print(f"Hero: {name} Class: {Heroclass.capitalize()}")
    print("Base stats: ")
    print(f"Strenght:{Strenght}")
    print(f"Critical:{Critical}")
    print(f"Intelligence:{Intelligence}")
    print(f"Health:{HP}")
    print(f"XP:{XP}")
    print(f"Coins:{coins}")
print("Choose a name: ")
name = input("")
while True:
    print("Choose a class:")
    print("Warrior/Mage/Rogue")
    Heroclass = input("").lower()
    if Heroclass in classesdict:
        Strenght = classesdict[Heroclass]["Strenght"]
        Critical = classesdict[Heroclass]["Critical"]
        Intelligence = classesdict[Heroclass]["Intelligence"]
        Agillity = classesdict[Heroclass]["Agillity"]
        break
    else:
        print("Not a class, Try Again!")
print("Allocate Skill Points") 
SP = 5
while True:
    if SP == 0:
        break
    print(f"Skill Points left: {SP}")
    print(f"1) Strenght:{Strenght}")
    print(f"2) Critical:{Critical}")
    print(f"3) Intelligence:{Intelligence}")
    while True:
        try:
            choice = int(input(""))
            break
        except ValueError:
            print("Not valid!")
    if choice == 1:
        Strenght+=1
        SP-=1
    elif choice ==2:
        Critical+=1
        SP-=1
    elif choice ==3:
        Intelligence+=1
        SP-=1
    else:
        print("Error! Choose a valid option")
print(f"Hero: {name} Class: {Heroclass.capitalize()}")
print("Base stats: ")
print(f"Strenght:{Strenght}")
print(f"Critical:{Critical}")
print(f"Intelligence:{Intelligence}")
print(f"Health:{HP}")
print(f"XP:{XP}")
while True:
    print("1) Play")
    print("2) Shops")
    print("3) Stats")
    print("4) Exit")
    while True:
        try:
            choice = int(input(""))
            break
        except ValueError:
            print("Choose A Number")
    if choice == 1:
        XP,HP, Strenght, Agillity, Intelligence,Critical, coins = play(XP,HP, Strenght, Agillity, Intelligence,Critical, coins)
    elif choice == 2:
        HP, Strenght, Agillity, Intelligence,Critical, coins, maxhp = shop(HP, Strenght, Agillity, Intelligence,Critical, coins, maxhp)
    elif choice == 3:
        stats(name,XP,HP, Strenght, Agillity, Intelligence,Critical,coins,maxhp)
    elif choice == 4:
        print("Exiting")
        break
    else:
        print("Please choose a valid option!")

#balancing update
