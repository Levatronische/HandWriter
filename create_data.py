from functions import read_char_pos, save_char_list, get_char_list
import time
col = 1
char = input()

char_list = [col]

for i in range(col):
    char_list.append(read_char_pos())
    print(f"{i + 1} - Ready")
    time.sleep(0.1)

save_char_list(char_list, char)
