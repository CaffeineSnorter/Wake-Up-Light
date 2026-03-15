import gc
import sys
import esp
from system import setup

gc.collect()
esp.osdebug(None)

if "/modules" not in sys.path:
    sys.path.append("/modules")


device_id = setup.set_id()

config_file = "config.json"

if not setup.config_available(config_file):
    setup.deploy_server(device_id)
else:
    import main