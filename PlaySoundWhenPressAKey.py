from playsound import playsound
import keyboard


def sound():
    playsound('Napalm_Death-You_Suffer.mp3')


exit = True

while (exit):

    if(keyboard.is_pressed('space')):
        sound()

    exit = not (keyboard.is_pressed('esc'))
