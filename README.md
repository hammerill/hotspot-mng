# Hotspot Manager
A little script designed to be launched from Termux in a rooted Android device.

It will verify if Internet is connected; if not, it will reconnect it
(I wrote it on my vacation because there's no reliable WiFi).

## Configure
Install Python3, git and sudo:
```bash
pkg install python3 git tsu
```
Clone repo:
```bash
git clone https://github.com/Hammerill/hotspot-mng
cd hotspot-mng
```

## Launch
```bash
python3 main.py &> /dev/null
```
