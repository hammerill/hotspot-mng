# File for managing low-level OS commands.

import subprocess

import config

# Turn Airplane mode on or off. Also manage WiFi hotspot.
def turn_airplane_mode(on=True, hotspot=True):
    subprocess.run(f"sudo settings put global airplane_mode_on {1 if on else 0}", shell=True) # Set Airplane parameter
    subprocess.run("sudo -E am broadcast -a android.intent.action.AIRPLANE_MODE", shell=True) # Invoke intent to apply parameter
    
    if (not on) and hotspot:
        subprocess.run("sudo service call tethering 4 null s16 random", shell=True) # Turn on WiFi hotspot (somehow)

# Check connection by pinging some address.
def inet_connected():
    p = subprocess.Popen(["ping", "-c1", config.HOST_TO_CHECK])
    try:
        res = p.wait(config.HOST_CHECK_TIMEOUT)
        if res == 0:
            return True
    except Exception:
        p.kill()
    
    return False
