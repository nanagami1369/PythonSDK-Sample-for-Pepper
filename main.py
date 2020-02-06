import sys

import qi
import where_is_do

import os

pepper_ip = os.environ.get("PEPPER_IP")
pepper_port_row = os.environ.get("PEPPER_PORT")
pepper_port = int(pepper_port_row)
try:
    # Initialize qi framework.
    connection_url = "tcp://" + pepper_ip + ":" + str(pepper_port)
    app = qi.Application(["What_is_do", "--qi-url=" + connection_url])
except RuntimeError:
    error_message = "Pepperに接続できませんでした\n ip={}\n port={}\n"
    error_message.format(pepper_ip, pepper_port)
    sys.exit(1)

Pepper = where_is_do.Pepper(app, pepper_ip, pepper_port)
Pepper.run()
