import random
class Creature():
    def __init__(self,HP,name):
        self.hp = HP
        self.name = name

    def attack(self):
        attcak_value = random.randint(0,50)
        return attcak_value

    def not_dead(self):
        if self.hp<=0:
            return False
        else:
            return True

    def being_attack(self,attack_value):
        self.hp = self.hp-attack_value

    def show_status(self):
        print('{}\'s hp is {}.'.format(self.name,self.hp))

player = Creature(100,'lcf')
enemy = Creature(100,'enemy')

while player.not_dead() and enemy.not_dead():
    user_input = input('Attack or Defence(A/D):')
    player.show_status()
    enemy.show_status()
    if user_input == 'A':
        player_attack_value = player.attack()
        enemy_attack_value = enemy.attack()
        enemy.being_attack(enemy_attack_value)
        player.being_attack(player_attack_value)
    elif user_input == 'D':
        enemy_attack_value = enemy.attack()*0.1
        player.being_attack(enemy_attack_value)

if player.not_dead():
    print('You win!')
else:
    print('You lose!')