import os
import time
import random
import requests
import subprocess

timeWa1 = random.uniform(8, 11)

# Function checks if a device is connected
def veriDevi():
    retorno = subprocess.getoutput("adb devices")
    return "device" in retorno

# Function answer if an device is connected
if not veriDevi():
    print("No Android device identified. Make sure ADB is set up, the device is connected, and supports 'USB Debugging'.")
    exit()

# Function to execute ADB commands
def adb_command(command):
    """Execute ADB commands"""
    try:
        result = subprocess.run(f"adb {command}", shell=True, text=True, capture_output=True)
        if result.returncode != 0:
            print(f"Error executing the command: {result.stderr}")
        else:
            print(f"Command executed: {result.stdout}")
    except Exception as e:
        print(f"Error on execute the adb_command: {e}")

# Function to get a random word from the API
def ranWord():
    try:
        response = requests.get("https://random-word-api.vercel.app/api?words=1")
        if response.status_code == 200:
            return response.json()[0]
    except Exception as e:
        print(f"Error getting the word: {e}")
    return "fallback"

# Function open Bing
def openBing():
    adb_command("shell pm clear com.microsoft.bing")  # Clean data
    time.sleep(2)
    adb_command("shell am start -n com.microsoft.bing/com.microsoft.sapphire.app.main.SapphireMainActivity")  # Open Bing on Android
    time.sleep(20)
    adb_command("shell input tap 350 1340")  # Click on Introduction
    time.sleep(5)

# Function to search
def doSearch():
    adb_command("shell input tap 220 718")  # Tap on the first search bar
    time.sleep(2)
    adb_command("shell input tap 200 100")  # Tap on the second search bar
    time.sleep(2)
    palavra = ranWord()
    adb_command(f"shell input text {palavra}")
    time.sleep(2)
    adb_command("shell input keyevent 66")  # Press 'Enter'
    time.sleep(timeWa1)
    adb_command("shell input tap 630 1455")  # Back to start
    time.sleep(3)

# Function News Scroll
def scrollNews():
    time.sleep(2)
    adb_command("shell input tap 350 870") # Tap on new
    time.sleep(8)
    adb_command("shell input keyevent 4") # Back
    time.sleep(2)
    adb_command("shell input touchscreen draganddrop 650 1380 650 400 700") # Scroll

# Close tabs
def cloTabs():
    adb_command("shell input tap 512 1457")  # Tap on 'Guides' icon
    time.sleep(2)
    adb_command("shell input tap 664 123")   # Tap on 'Three dots'
    time.sleep(2)
    adb_command("shell input tap 176 1157")  # Tap on 'Clear all tabs'
    time.sleep(2)
    adb_command("shell input tap 630 1455")  # Tap on 'House'
    time.sleep(2)

# Comandos finais
def finalComm():
     adb_command("shell am force-stop com.microsoft.bing")  # Stop Bing
     time.sleep(1)
     adb_command("shell am kill com.microsoft.bing")  # Kill Bing
     time.sleep(1)

     # Simule 'Navegation bar' to close in second plan
     adb_command("shell input keyevent KEYCODE_APP_SWITCH")  # Tap 'Overview'
     time.sleep(1)
     adb_command("shell input keyevent KEYCODE_MOVE_END")  # Select Bing
     time.sleep(1)
     adb_command("shell input keyevent KEYCODE_DEL")  # Move Bing
     time.sleep(1)
     adb_command("shell input keyevent 26")  # Tap 'Home'
     time.sleep(1)

# --Start process--

openBing()

adb_command("shell am force-stop com.microsoft.bing")  # Stop Bing
time.sleep(1)
adb_command("shell am kill com.microsoft.bing")  # Kill Bing
time.sleep(1)
adb_command("shell input keyevent KEYCODE_APP_SWITCH")  # Tap 'Overview'
time.sleep(1)
adb_command("shell input keyevent KEYCODE_MOVE_END")  # Select Bing
time.sleep(1)
adb_command("shell input keyevent KEYCODE_DEL")  # Move Bing
time.sleep(1)

openBing()

adb_command("shell input tap 643 1056")  # Tap on close message
time.sleep(2)

# Execute 'doSearch' 45 times
for i in range(45):
    doSearch()

# Prepare to scroll news
adb_command("shell input touchscreen draganddrop 650 1380 650 85 700")  # Max scroll
time.sleep(2)
adb_command("shell input touchscreen draganddrop 650 1380 650 800 700")  # Adjust scroll

# Execute 'scrollNews' 35 times
for i in range(35):
    scrollNews()

cloTabs()

finalComm()

print("Script completed successfully!")

input("Press Enter to close...")
