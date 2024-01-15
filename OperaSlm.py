import time

import pyautogui

pg = pyautogui

# Abrindo o prompt
pg.hotkey('winleft', 'r', interval=0)
time.sleep(1)
pg.typewrite(['cmd', 'enter'],0)

# Escrevendo no Prompt
time.sleep(1)
pg.typewrite(['s', 't', 'a', 'r', 't', 'space', 'O', 'p', 'e', 'r', 'a', 'enter'], 0.01)
pg.typewrite(['e', 'x', 'i', 't', 'enter'], 0)

# Escrevendo no Google


time.sleep(3)
pg.typewrite('facebook', 0.01)
pg.typewrite(['enter'])
