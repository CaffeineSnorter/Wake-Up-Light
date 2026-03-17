import network
from time import sleep

def connect(ssid: str, password: str, timeout: int):

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.config(reconnects=4)

    if wlan.isconnected():
        return True
    
    print(f"Connecting to {ssid}...")
    wlan.connect(ssid, password)

    timeout_ = timeout
    while not wlan.isconnected() and timeout_ > 0:
        sleep(1)
        timeout_ -= 1
    if wlan.isconnected():
        print(wlan.ipconfig('addr4'))
        return True
    print("Connection failed...")
    return False
