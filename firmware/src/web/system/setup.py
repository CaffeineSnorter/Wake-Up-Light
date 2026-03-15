import os
import network
import setup_net

def config_available(path: str):
    try:
        os.stat(path)
        return True
    except OSError:
        return False
    
def set_id():
    wlan = network.WLAN(network.STA_IF)
    mac = wlan.config('mac')
    return ''.join('{:02x}'.format(b) for b in mac[-3:])

def deploy_server(id: str):
    web_page = setup_net.get_web_page()
    setup_net.set_ap()
    setup_net.get_socket(web_page)
    