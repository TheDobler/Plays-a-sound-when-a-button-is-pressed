from playsound import playsound
import keyboard


def sound():
    playsound('') #add a mp3 file in here to play when you press the buton.


exit = True

while (exit):

    if(keyboard.is_pressed('space')): #Change here for which button you want to play the mp3 file.
        sound()

    exit = not (keyboard.is_pressed('esc'))
