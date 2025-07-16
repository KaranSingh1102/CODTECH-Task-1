
import os
import hashlib
import json
import time

MONITOR_FOLDER =  r"C:\Users\Arjun Singh\Desktop\sample folder"

HASH_FILE = "file_hashes.json"
CHECK_INTERVAL = 10  # in seconds

def calculate_hash(filepath):
    sha256 = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
    except FileNotFoundError:
        return None
    return sha256.hexdigest()

def scan_folder(folder):
    file_hashes = {}
    for root, dirs, files in os.walk(folder):
        for file in files:
            filepath = os.path.join(root, file)
            file_hash = calculate_hash(filepath)
            if file_hash:
                file_hashes[filepath] = file_hash
    return file_hashes

def load_baseline():
    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, "r") as f:
            return json.load(f)
    return {}

def save_baseline(baseline):
    with open(HASH_FILE, "w") as f:
        json.dump(baseline, f, indent=2)

def monitor():
    baseline = load_baseline()
    print("Initial baseline loaded.")

    while True:
        current_hashes = scan_folder(MONITOR_FOLDER)

        changes_detected = False

        # Detect new or modified files
        for filepath, filehash in current_hashes.items():
            if filepath not in baseline:
                print(f"[NEW FILE] {filepath}")
                changes_detected = True
            elif baseline[filepath] != filehash:
                print(f"[MODIFIED] {filepath}")
                changes_detected = True

        # Detect deleted files
        for filepath in baseline:
            if filepath not in current_hashes:
                print(f"[DELETED] {filepath}")
                changes_detected = True

        # If any changes, update baseline
        if changes_detected:
            print("Changes detected. Updating baseline...")
            save_baseline(current_hashes)
            baseline = current_hashes.copy()
        else:
            print("No changes detected.")

        print("Scan completed. Sleeping...\n")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    print(f"Monitoring {MONITOR_FOLDER} for changes...")
    monitor()
