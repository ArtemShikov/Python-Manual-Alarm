

import time
import datetime
import pygame


def run_alarm(alarm_time):
     print(f"Clock's arranged to {alarm_time}")
     sound = r"ClockSong.mp3"
     is_running = True


     while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M")
        #print(current_time)

        if current_time == alarm_time:
            print("AWAKE BRO")

            pygame.mixer.init()
            pygame.mixer.music.load(sound)
            pygame.mixer.music.play()


            while pygame.mixer.music.get_busy():
                time.sleep(30)

                is_running = False

    #  time.sleep(1)       

run_alarm("20:38")

