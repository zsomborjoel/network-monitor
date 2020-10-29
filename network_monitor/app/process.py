from .logs import add_to_log
from .emails import send_mail
from .config import get_config
from .network import connect, run_command
from .logics import get_unexpected_devices
import sys
import time

# Params
email_password = sys.argv[1]
router_username = sys.argv[2]
router_password = sys.argv[3]

router_host = get_config("host")
router_port = get_config("port")

from_address = get_config("from_address")
to_address = get_config("to_address")

known_devices = get_config("devices")
subject = "Network monitor alert"

last_unexpected_devices = []


def process(ssh):
    global last_unexpected_devices
    router_output = run_command(ssh, "cat /var/log/messages")
    unexpected_devices = get_unexpected_devices(router_output, known_devices)
    if unexpected_devices != last_unexpected_devices and len(unexpected_devices) > 0:
        print(unexpected_devices)
        send_mail(from_address, to_address, subject, email_password, str(unexpected_devices))
        last_unexpected_devices = unexpected_devices
    else:
        add_to_log("In sleep mode")
        time.sleep(1 * 60 * 60)


def main():
    add_to_log('Process started')
    print('started')
    try:
        ssh = connect(router_host, router_port, router_username, router_password)
        while True:
            process(ssh)
            time.sleep(5)
    except Exception as e:
        add_to_log(str(e))
        print(e)


if __name__ == '__main__':
    main()
