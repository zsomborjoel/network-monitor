from .logs import add_to_log


def get_unexpected_devices(log, known_devices):
    """
    :param log: incoming log data
    :param known_devices: list of devices which currently working on network
    :return: list of unknown devices
    """

    add_to_log("In unexpected devices")
    unexpected_devices = []
    for elem in log:
        if "DHCPACK(br0)" in elem:
            device = elem.split("DHCPACK(br0)")[1].strip()
            device_name = device.split(" ")[2]
            if device_name not in known_devices and device not in unexpected_devices:
                unexpected_devices.append(device)

    return unexpected_devices
