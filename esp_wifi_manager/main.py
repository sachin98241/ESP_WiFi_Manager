"""
ESP32 WiFi Config - Main entry point
Run this on your ESP32 to start the WiFi manager
"""

from esp32_config import ESP32WiFiConfig

# Initialize WiFi Config Manager
wifi = ESP32WiFiConfig(
    ap_name="ESP32_Config",      # WiFi AP name (change if desired)
    ap_pass="12345678"           # WiFi AP password (change if desired)
)

# Start the manager
# - First attempts to connect to saved WiFi
# - If fails, starts Access Point with web server
print("Starting ESP32 WiFi Config Manager...")
wifi.start()
