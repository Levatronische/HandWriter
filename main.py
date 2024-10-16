import mouse
import keyboard
from functions import read_char_pos, save_char_list, get_char_list, put_char

char_list = get_char_list("а")

alfabet = {
    "а": get_char_list("а"),
}

while True:
    while True:
        if keyboard.is_pressed("a"):
            break

    mouse.press()
    put_char(alfabet["а"])