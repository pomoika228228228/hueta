# Сделать, чтобы игрок мог выбирать сторону, куда повернуть
# С помощью int(input())

import random
from time import sleep
hp = 100
distance = 400
speed = 0

yetti = 3
tree = 2
rock = 1

while True:
    print('')
    chanceEnemy = random.randint(0,6)
    if chanceEnemy == rock:
        print('Вы столкнулись с камнем')
        hp -= 5
        print(f'У вас осталось {hp} жизней')
        sleep(1)
    elif chanceEnemy == yetti:
        print('Вас пожрал Йети')
        hp -= 10
        print(f'У вас осталось {hp} жизней')
        sleep(1)
    elif chanceEnemy == tree:
        print('Вы влетели в дерево')
        hp -= 8
        print(f'У вас осталось {hp} жизней')
        sleep(1)
        
    speed += 1 #speed = speed + 1.
    distance -= speed #distance = distance - speed
    print(f'Вы летите со скорость {speed} км/c')
    print(f'Осталось проехать {distance} километров')
    
    if (distance <= 0):
        print('УРА! Победа!')
        break
    if (hp <= 0):
        print('Вас сожрали')
        break

    sleep(0.6)
