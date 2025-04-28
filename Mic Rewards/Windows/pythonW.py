import pyautogui
import time
import random
import subprocess
import requests

timeWa1 = random.uniform(8, 11)
timeWa2 = random.uniform(3, 7)

# Function: get a random word from the API
def ranWord():
    try:
        response = requests.get("https://random-word-api.vercel.app/api?words=1")
        if response.status_code == 200:
            return response.json()[0]  # Returns the generated word
    except Exception as e:
        print(f"Error getting the word: {e}")
    return "fallback"  # Default word if API fails

print("Starting the script...")

# Function to search
def start():
    print(f"Running interaction {i+1}...")
        
    pyautogui.hotkey("ctrl", "t")  # Open new tab
    time.sleep(1)
    pyautogui.hotkey("ctrl", "e")  # Execute shortkey 'Ctrl + E'
    time.sleep(0.5)
    palavra = ranWord()  # Execute function 'ranWord'
    pyautogui.typewrite(palavra)  # Write word
    time.sleep(timeWa2)
    pyautogui.press("enter")  # Press 'Enter'
    time.sleep(timeWa1)

# Open Microsoft Edge
subprocess.Popen(r"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
print("Microsoft Edge opened!")

# Wait Edge opens
time.sleep(5)

# Execute 'start' function 30 times
for i in range(30):
     start()

# Close all tabs
print("Finishing... Closing tabs...")
for _ in range(30):
    pyautogui.hotkey("ctrl", "w")
    time.sleep(0.1)

print("Script completed successfully!")

input("Press Enter to close...")
