import usb.core
import usb.util


def find_bluetooth_dongle():
    # Find all USB devices
    devices = usb.core.find(find_all=True)

    for device in devices:
        # Check if the device is a Bluetooth adapter
        if device.bDeviceClass == 224:  # Wireless Controller
            return device
    
    return None

dongle = find_bluetooth_dongle()

if dongle:
    print(f"Bluetooth dongle found:")
    print(f"  Manufacturer: {usb.util.get_string(dongle, dongle.iManufacturer)}")
    print(f"  Product: {usb.util.get_string(dongle, dongle.iProduct)}")
    print(f"  Serial Number: {usb.util.get_string(dongle, dongle.iSerialNumber)}")
    print(f"  Device Class: {dongle.bDeviceClass}")
    print(f"  VID:PID: {dongle.idVendor:04x}:{dongle.idProduct:04x}")
else:
    print("No Bluetooth dongle found.")
