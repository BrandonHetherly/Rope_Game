import time
import random

blue_score = 0
red_score = 0

temp_blue_score = 0
temp_red_score = 0

miss = {'points': 0}
blue = {'color': 'blue', 'points': 1}
green = {'color': 'green', 'points': 2}
yellow = {'color': 'green', 'points': 3}

flag = True
while flag:

    temp_blue_score = 0
    temp_red_score = 0

    for throw in range(3):

        chance = random.randint(0, 100)
        if chance <= 20:
            temp_blue_score = temp_blue_score + blue['points']
        elif 50 >= chance > 20:
            temp_blue_score = temp_blue_score + green['points']
        elif 70 >= chance > 50:
            temp_blue_score = temp_blue_score + yellow['points']
        #else:
            #blue_score = blue_score + miss['points']
            #temp_blue_score.append(blue_score)

    for throw in range(3):

        chance = random.randint(0, 100)
        if chance <= 20:
            temp_red_score = temp_red_score + blue['points']
        elif 50 >= chance > 20:
            temp_red_score = temp_red_score + green['points']
        elif 70 >= chance > 50:
            temp_red_score = temp_red_score + yellow['points']
        #else:
            #red_score = red_score + miss['points']
            #temp_red_score.append(red_score)


    diff = 0

    if temp_red_score > temp_blue_score:
        diff = temp_red_score - temp_blue_score
        red_score = red_score + diff
    elif temp_blue_score > temp_red_score:
        diff = temp_blue_score - temp_red_score
        blue_score = blue_score + diff

    print("------")
    print(f"Blue: {blue_score}")
    print(f"Red: {red_score}")
    time.sleep(1)

    if blue_score >= 21 or red_score >= 21:
        flag = False
        print("==== Game Over ====")


print(f"Blue: {blue_score}")
print(f"Red: {red_score}")
