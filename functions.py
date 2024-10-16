import mouse
import keyboard
import pickle
import random


def wait_until(char):
    while True:
        if keyboard.is_pressed(char):
            break


def read_char_pos():
    list_of_pos = []
    recent = (0, 0)

    while True:
        if mouse.is_pressed():
            now = mouse.get_position()
            list_of_pos.append((now[0] - recent[0], now[1] - recent[1]))
            recent = now
            print((now[0] - recent[0], now[1] - recent[1]))
        if keyboard.is_pressed(" "):
            break
    return list_of_pos


def put_char(char_list):
    rand_int = random.randint(1, char_list[0])
    list_of_pos = char_list[rand_int]
    print(rand_int)
    for pos in list_of_pos:
        mouse.move(pos[0], pos[1], absolute=False, duration=0)


def save_char_list(char_list, char):
    with open(f"data/{char}", "wb") as fp:
        pickle.dump(char_list, fp)


def get_char_list(char):
    with open(f"data/{char}", "rb") as fp:
        return pickle.load(fp)