import pywifi
from pywifi import const
import time
connected=False
def scan_available_networks():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # Assuming you have only one Wi-Fi interface. You can loop through available interfaces if needed.

    iface.scan()
    scan_results = iface.scan_results()

    if not scan_results:
        print("No WiFi networks found.")
    else:
        print("Available WiFi networks:")
        for result in scan_results:
            print(f"SSID: {result.ssid}, Signal Strength: {result.signal}, BSSID: {result.bssid}")

def connect_to_wifi(ssid, password):
    global connected
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # Assuming you have only one Wi-Fi interface. You can loop through available interfaces if needed.

    iface.scan()
    scan_results = iface.scan_results()

    target_network = None

    for result in scan_results:
        if result.ssid == ssid:
            target_network = result
            break

    if target_network is None:
        print(f"Network '{ssid}' not found.")
        return

    profile = pywifi.Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = password

    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)
    iface.connect(tmp_profile)

    time.sleep(5)

    if iface.status() == const.IFACE_CONNECTED:
        print(f"Connected to '{ssid}' successfully.")
        connected=True
    else:
        print(f"Failed to connect to '{ssid}'.")

# To scan and list available networks:
scan_available_networks()
# while not connected:
#     # To connect to a specific network, replace 'Your_WiFi_SSID' and 'Your_WiFi_Password' with your actual SSID and password:
#     connect_to_wifi("AASAN YT", "8209634753")
#     #connect_to_wifi("ak", "1234554321")
#     connect_to_wifi("vivo Y200 5G", "armankathat")
#     connect_to_wifi("Arman", "salinabano")
connect_to_wifi("ak", "1234554321")
