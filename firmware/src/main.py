import json
from modules import wifi
from system import setup

with open("config.json") as c:
    data = json.load(c)

ssid = data["SSID"]
password = data["PASSWORD"]
device_id = data["ID"]

if not wifi.connect(ssid=ssid, password=password):
    setup.deploy_server(device_id)