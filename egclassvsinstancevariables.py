# A class variable is associated with a class and is shared across all instances
# An instance variable is associated with instance only

class Shooting:
    remainingBullets = 100 # class variable

    def __init__(self, playerName):
        self.playerName = playerName
        self.remainingBullets = 10 # instance variable
        Shooting.remainingBullets -= 10

    def shoot(self):
        if(Shooting.remainingBullets == 0):
            print("Can not shoot. No more bullets")
        else:
            self.remainingBullets -= 1


shooting_alice = Shooting("Alice")
print("\nGame created for Alice")
print(f"Remaining bullets [Total] - {Shooting.remainingBullets}")
print(f"Remaining bullets [Alice] - {shooting_alice.remainingBullets}")

shooting_bob = Shooting("Bob")
print("n\Game created for Bob")
print(f"Remaining bullets [Total] - {Shooting.remainingBullets}")#remaingBullets(100)-shooting.remaingBullets(10)= 90
print(f"Remaining bullets [Bob] - {shooting_bob.remainingBullets}")#bczo its a instance o e class wil take into account the instance variable(self.remaining = 10) only

print("\nAlice fired a shot")
print(f"Remaining bullets [Total] - {Shooting.remainingBullets}")
print(f"Remaining bullets [Alice] - {shooting_alice.remainingBullets}")

shooting_bob.shoot()
print("\nBob fired a shot")
print(f"Remaining bullets [Total] - {Shooting.remainingBullets}")
print(f"Remaining bullets [Bob] - {shooting_bob.remainingBullets}")

shooting_chris = Shooting("Chris")
print("\nGame created for Chris")
print(f"Remaining bullets [Total] - {Shooting.remainingBullets}")
print(f"Remaining bullets [Chris] - {shooting_bob.remainingBullets}")

for i in range(0,5):
	shooting_chris.shoot()
print("\nChris fired 5 shots")
print(f"Remaining bullets [Total] - {Shooting.remainingBullets}")
print(f"Remaining bullets [Chris] - {shooting_chris.remainingBullets}")
