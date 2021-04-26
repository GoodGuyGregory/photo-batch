#! python3
# selectiveCopy - a program designed to allow for a specified selection file type
#  to be copied and added to a new folder

import os
import re
import shutil


def selectivecopy():
    # Creates a Directory for Photo-Session
    name = input('enter a name for the session: ')
    os.mkdir(name)
    currentPath = os.getcwd()
    FolderInPath = os.path.join(currentPath, name)
    
    # Moves the Folder to the desired location
    outputLoc = input('where do you store your photos?: ')
    

    # Walks Directory for photos with the most recent date
    for folderName, subFolderNames, filenames in os.walk(os.getcwd()):
        #  dont search Found-Images
        if folderName == FolderInPath:
            break
        else:
            # determine 
            for filename in filenames:
                # determine condition for file date
                if :
                    print("adding image file: %s" % filename)
                    shutil.copy(filename, name)
            print('')


def main():

    selectivecopy()


main()
