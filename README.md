# _RemoteCommander_

# End User License Agreement
By using the software provided you automatically agree to the following EULA:
1. I (KablammoMan) am not responsible for any trouble that you get in (legal, institutional, etc...) for using the software provided, however, if I am caught using it I will accept responsibility for my actions and take whatever punishment is deemed appropriate.
2. The software is provided as is and I make no guarantees of the software working on all computers at all points in time.

# Description

This is a project that allows you to run pre-determined commands on someone elses computer - if you are on the same network.

# Requirements
1. Python (added to PATH - can set this at installation)
2. Pyinstaller (cmd: "pip install pyinstaller")
3. Both computers are on the same network

# Files: "slave.py" vs "slavemanual.py"
The difference between these two are that "slave.py" will autmotacially move itself to the startup folder, allowing it to run on startup (some antiviruses will flag this as malware). However, the "slavemanual.py" will be required to be run manually everytime you want to connect to the desired computer OR you can manually place it into the startup folder.

# Instructions

To Setup:
1. Download "master.py" onto your computer
2. (Optional) Open Command Prompt to the directory of "master.py"
3. (Optional) Type "pyinstaller --onefile master.py" and press enter
4. (Optional) Use the created "master.exe" file if you want to (in "dist" folder)
5. Download either "slave.py" OR "slavemanual.py" depending on what your intent is
6. Change the "S20364-PC" to your computers hostname -> can be found using "print(socket.gethostname())" (requires "import socket")
7. Open Command Prompt to the directory of "slave.py" or "slavemanual.py"
8. Type "pyinstaller --onefile --noconsole slave.py" OR "pyinstaller --onefile --noconsole slavemanual.py" depending on downloaded file
9. Run the created "slave.exe" OR "slavemanual.exe" (located in "dist" folder) on the desired computer

To Use:
1. Run "slave.exe" OR "slavemanual.exe" on desired computer (if not done already)
2. Run "master.exe" on your computer
3. Wait until it says "IP is connected to server"
4. Use one of the commands below

# Current Commands

1. cmd(_string_, _iterations_) -> runs the desired command (_string_) _iterations_ times
2. explorer() -> opens file explorer
3. shutdown() -> shuts down the target computer
4. delete(_string_) -> deletes the desired file or folder (_string_)
