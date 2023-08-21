# Entry point.

import time

import system
import config

inet_failed_tries = 0

def step():
    global inet_failed_tries

    if system.inet_connected():
        inet_failed_tries = 0
    else:
        inet_failed_tries += 1

    if inet_failed_tries >= config.INET_RETRIES:
        system.turn_airplane_mode(True)
        time.sleep(config.AIRPLANE_THRESHOLD)
        system.turn_airplane_mode(False, config.RELAUNCH_HOTSPOT)

        inet_failed_tries = 0



while True:
    step()
    time.sleep(config.INET_PERIOD)
