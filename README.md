# ops.app-manager-offline-releases-folder-weekly-update-script

# PURPOSE:
# The purpose of the materials in this repository is to automatically download the latest version of the offline repository to a user designated location.
# The script will download the latest version of the offline repo, save a prior version as a backup, and copy the latest download to a D: drive 
# storage location (assuming one is connected).

# REQUIRED MATERIALS:
# Python 3.x or above (code written using version 3.8.5)
# Python "shutil" module
# Python "os" module
# Python "time" module
# DIRECT_6.1.0.130_DS_3.2.9-v2 archive
# .NET 5.0
# Latest config .json (named Released.json)

# HOW TO USE:
# The reposdownload.py script is what initiates the repository download. To do so, the user must modify the file locations listed in the script under
# the "paths" function. "signfix_path" must be changed to the path to the offline-signfix.py file and "json_path" must be changed to the location where the Released.json
# file is stored. 
# "USB_path", "backup_path", and "source" are all custom to where the user desires each item to be stored. "USB_path" is the desired location where
# the user would like to store the repo on a USB. !NOTE! If not storing to a D drive, user must also change line 66 in "USBcopy" funtion to reflect the desired
# drive letter. "backup_path" specifies where the backup will be stored and under what name, and "source" is the parent branch where the newest download and backup
# versions will be stored.

# It is important to note that the python script itself does not automate the download with respect to time. The program needs to be called in order to run.
# This code has been implemented with the use of windows task scheduler to automatically download the repo on saturdays at 6pm. A custom task is scheduled that
# runs the program, which is how it automates with respect to time. A .bat with the command line to run the program is also included in the repo
# which can manually run the script.

# In short, to run the program the user must first make sure all of the necessary files/modules/applications listed in the requirements are downloaded. They must then
# change each of the file paths in "paths" to the desired/necessary locations as described. Finally, they then call the script manually in
# a command window, manually with the .bat, or automatically by setting up a windows task schedule. 
