import subprocess
import os
import winreg
import sys

# Ensure the script is running in the correct directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def run(command):
    """Execute an command on cmd"""
    subprocess.run(command, shell=True, check=True)

def add_to_path(new_path):
    """Adds a directory to the user's PATH permanently."""
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment", 0, winreg.KEY_ALL_ACCESS) as key:
            current_path = winreg.QueryValueEx(key, "Path")[0]
            if new_path not in current_path:
                print(f"Adding {new_path} to PATH...")
                winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, current_path + ";" + new_path)
                print(f"{new_path} added to PATH.")
            else:
                print(f"{new_path} is alredy on PATH.")
    except Exception as e:
        print(f"Error in adding to PATH: {e}")

# Update pip
print("Updating pip...")
run("python -m pip install --upgrade pip")

# Install python libraries
print("Installing the necessary libraries...")
run("pip install pyautogui pytesseract opencv-python pillow requests")

# Install Tesseract OCR
print("Installing Tesseract OCR...")
# try use Winget to install
try:
    run("winget install -e --id UB-Mannheim.TesseractOCR")
except subprocess.CalledProcessError:
    print("Failed to install Tesseract OCR with winget. Trying another approach...")

# Add Tesseract to PATH
tesseract_path = r"C:\Program Files\Tesseract-OCR"
add_to_path(tesseract_path)

# ADB Configuration
script_dir = os.path.dirname(os.path.abspath(__file__))  # Script directory
adb_path = os.path.join(script_dir, "..", "Android", "platform-tools")  # Relative path to platform-tools folder

# Ensure ADB path is correct
adb_path = os.path.abspath(adb_path)

if not os.path.exists(os.path.join(adb_path, "adb.exe")):
    print(f"ADB not found in {adb_path}. Make sure that the 'platform-tools' folder exists.")
    exit(1)

# Add ADB in PATH
print("Adding ADB to PATH...")
add_to_path(adb_path)

# Force PATH update in current session
print("Updating PATH for current session...")
os.environ["PATH"] += f";{adb_path}"

# Verify ADB installation
print("Verifying ADB installation...")
run(f'"{adb_path}\\adb.exe" version')

# Try running ADB to see if it's working
run(f"adb version")

print("Setup complete! If ADB doesn't work, restart the terminal.")

input("Press Enter to close...")
