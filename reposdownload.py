###############################################################################
# The purpose of this script is to download the offline repository of zSpace
# applications automatically. The path names in function paths() will all have
# to be changed when implementing on the final computer.
###############################################################################
import shutil
import os
import time

#This function declares the paths to all of the necessary file locations/destinations.
def paths():
    signfix_path = r'C:\OfflineRepo\Download_Materials\DIRECT_6.1.0.130_DS_3.2.9\deploy\offline-signfix.py' #path to offline-signfix.py
    signfix_path = signfix_path.replace('\\','/')

    json_path = r'C:\OfflineRepo\Download_Materials\ops.app-manager-offline-release-folder-config\Released.json' #path to the ga2019.json file
    json_path = json_path.replace('\\','/')

    USB_path = r'D:\OFFLINE_REPO' #path to the desired USB drive for the newest repository download storage
    USB_path = USB_path.replace('\\','/')

    backup_path = r'C:\OfflineRepo\Backup_Repository' #path to the desired location for the backup copy to be stored
    backup_path = backup_path.replace('\\','/')

    source = r'C:\OfflineRepo' #parent branch of where the download and backup are stored
    source = source.replace('\\','/')

    return(signfix_path,json_path,USB_path,backup_path,source)


#This function backs up the repository by moving the now outdated version to a new
#folder, while deleting any older copies.
def backup_repos(backup_path,source):
    #determining the backup path and if it already exists
    backupexist = os.path.isdir(backup_path)

    #determining the repository download path and if it already exists
    download_folder = '/Released' #this is the filename of the newest downloaded repository
    source = source + download_folder
    sourceexist = os.path.isdir(source)

    #if both paths exist, will delete old backup and rename the now old version
    #else, if only source exists, will rename old source to new backup
    #otherwise do nothing. No action necessary if only contain old backup or neither exist
    if ((backupexist==1) and (sourceexist==1)):
        shutil.rmtree(backup_path)
        os.rename(source,backup_path)
    elif (sourceexist==1):
        os.rename(source,backup_path)

    return(source)


#This function downloads the repository
def download(sign,json):
    os.system(f"python.exe {sign} --config={json}")

    return


#This function copies the newest repository download onto the desired USB drive location.
#It checks if the necessary folders exist before moving/deleting items to prevent errors
def USBcopy(USB_path,newest_repos):
    newest_repos_exist = os.path.isdir(newest_repos)

    if (newest_repos_exist==1):
        USB_exist = os.path.isdir('D:') #checks if D drive exists on machine
        if (USB_exist==1):
            USB_repo_exist = os.path.isdir(USB_path)
            if(USB_repo_exist==1):
                shutil.rmtree(USB_path)
                shutil.copytree(newest_repos,USB_path)
            else:
                shutil.copytree(newest_repos,USB_path)
        else:
            print('There was an error with the USB copy. USB D: drive not detected.')
    else:
        print('There was an error with the USB copy. The newest repository download could not be found.')

    return



def main():
    sign,json,USB,backup,source = paths()
    newest_repos = backup_repos(backup,source)
    download(sign,json)
    USBcopy(USB,newest_repos)


main()
