import network

def get_ssid_list():
    station = network.WLAN(mode=network.WLAN.STA)
    networks = station.scan()
    return [i[1] for i in networks]

def get_web_page():
    pass

def set_ap():
    pass

def get_socket(html: str):
    pass