import mouse
import keyboard
from functions import read_char, save_char_list, get_char_list


list_of_pos = read_char()

char_list = [list_of_pos]

save_char_list(char_list, "a")

char_list = []

list_of_pos = get_char_list("a")[0]

mouse.press()
for pos in list_of_pos:
    mouse.move(pos[0], pos[1], absolute=False, duration=0)
    if keyboard.is_pressed("w"):
        break
mouse.release()
