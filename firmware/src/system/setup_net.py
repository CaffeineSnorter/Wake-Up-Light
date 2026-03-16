import network
import socket
import json

def get_ssid_list():
    station = network.WLAN(network.STA_IF)
    station.active(True)
    networks = station.scan()
    return [i[0] for i in networks]

def get_web_page():
    options = get_ssid_list()

    string=""
    for ssid in options:
        string += f"""<option value="{ssid}">{ssid}</option>"""

    html = """
    <html>
    <body>
    <h2>Wake Up Lamp wifi setup</h2>
    <form method="POST">
    <label for="ssid">SSID</label>
    <select name="ssid" id="ssid">
    """+ string + """</select>
    Password:<br>
        <input name="password"><br>
    <input type="submit" value="Save"/>
    </form>"""
    return html

def set_ap(id: str):
    SSID = f"WakeUpLamp-{id}"
    PASSWORD = "0123456789"

    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid=SSID, key=PASSWORD)

    while ap.active()==False:
        pass

    print("Connection succesful")
    print(ap.ifconfig())

def parser(info):

    data = {}
    pairs = info.split("&")

    for pair in pairs:
        key, value = pair.split("=")
        data[key] = value

    return data

def save_config(data):
    config = {
        "SSID": data["ssid"],
        "PASSWORD": data["password"]
    }

    with open("config.json","w") as f:
        json.dump(config,f)

def get_socket(html: str):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('',80))
    s.listen(5)

    while True:
        conn, addr = s.accept()

        request = conn.recv(1024).decode()

        if "POST" in request:

            body = request.split("\r\n\r\n")[1]
            data = parser(body)
            save_config(data)
            response = "<h1>Saved. Reboot device.</h1>"

        else:
            
            response = get_web_page()

        conn.send("HTTP/1.1 200 OK\r\n")
        conn.send("Content-Type: text/html\r\n\r\n")
        conn.send(response)

        conn.close()