import winreg

def get_bluetooth_devices():
    devices = []
    try:
        bluetooth = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\BTHPORT\Parameters\Devices")
    except WindowsError:
        return devices

    for i in range(winreg.QueryInfoKey(bluetooth)[0]):
        try:
            device_addr = winreg.EnumKey(bluetooth, i)
            device_key = winreg.OpenKey(bluetooth, device_addr)
            device_name = winreg.QueryValueEx(device_key, "Name")[0]
            devices.append((device_addr, device_name))
        except WindowsError:
            pass

    return devices

bluetooth_devices = get_bluetooth_devices()

if bluetooth_devices:
    print("Bluetooth devices found:")
    for addr, name in bluetooth_devices:
        print(f"  Address: {addr}, Name: {name}")
else:
    print("No Bluetooth devices found.")
