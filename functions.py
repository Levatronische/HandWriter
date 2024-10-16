import mouse
import keyboard
import pickle


def read_char():
    list_of_pos = []
    recent = (0, 0)
    while True:
        if mouse.is_pressed():
            now = mouse.get_position()
            list_of_pos.append((now[0] - recent[0], now[1] - recent[1]))
            print((now[0] - recent[0], now[1] - recent[1]))
            recent = now
        if keyboard.is_pressed("q"):
            break
    list_of_pos[0] = (0, 0)
    return list_of_pos


def save_char_list(char_list, char):
    with open(f"data/{char}", "wb") as fp:
        pickle.dump(char_list, fp)


def get_char_list(char):
    with open(f"data/{char}", "rb") as fp:
        return pickle.load(fp)