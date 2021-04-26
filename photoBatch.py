#! python3
# selectiveCopy - a program designed to allow for a specified selection file type
#  to be copied and added to a new folder

import os
import time
import datetime
import re
import shutil


def selectivecopy():
    # Creates a Directory for Photo-Session
    name = input('enter a name for the session: ')
    os.mkdir(name)
    dateOfSession = input('when was the photo session? (MM-DD-YYYY): ')
    #  datetime object for comparison
    listOfChars = ['-', '/']
    dateOfSession = "".join(i for i in dateOfSession if i not in listOfChars)
    searchRange = datetime.datetime(
        int(dateOfSession[4:]), int(dateOfSession[:2]), int(dateOfSession[2:4]))
    print(searchRange)
    currentPath = os.getcwd()
    FolderInPath = os.path.join(currentPath, name)
    #  TODO:
    # GET THIS ELEMENT INTO A DATETIME OBJECT FOR COMPARISON
    print('current time: ' + str(time.ctime(time.time())))

    # Moves the Folder to the desired location
    # outputLoc = input('where do you store your photos?: ')

    # Walks Directory for photos with the most recent date
    for folderName, subFolderNames, filenames in os.walk(os.getcwd()):
        #  dont search Found-Images
        if folderName == FolderInPath:
            break
        else:
            # determine
            for filename in filenames:
                # determine condition for file date
                fileCreationDate = str(datetime.datetime.fromtimestamp(
                    os.stat(currentPath + '/' + filename).st_birthtime))
                # TODO: USE THE DATETIME COMPARISON FOR THE CURRENTTIME.DAY, CURRENTTIME.MONTH
                if datetime.time(creationTime) == searchRange:
                    # TODO: APPEND TO THE DIRECTORY FOR ARCHIVING
                    #     print(filename + str(os.stat(filename).st_mtime))
                    # if :
                    #     print("adding image file: %s" % filename)
                    #     shutil.copy(filename, name)
            print('')


def main():

    selectivecopy()


main()
