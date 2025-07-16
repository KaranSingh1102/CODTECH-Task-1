# CODTECH-Task-1
# 🔐 File Integrity Checker

**File Integrity Checker** is a lightweight Python script that monitors a specified folder for any changes in files, such as creation, modification, or deletion. It uses SHA-256 hashing to ensure accurate file integrity verification and runs on a simple loop with a customizable scan interval. The script automatically maintains a JSON file (`file_hashes.json`) to store and compare file hashes during each scan. It's easy to configure—just set your folder path in the code and run the script. Ideal for basic file monitoring, version tracking, or detecting unauthorized changes. Requires only Python 3.6+ and no external libraries.


![image alt](https://github.com/KaranSingh1102/CODTECH-Task-1/blob/8cc1963640da5ea93adf259301264b12e78cd403/screenshot1.png)


### 🧪 Sample Output: After File Changes Detected

Below is an example of what the terminal will display when changes are detected in the monitored folder:

