#!/usr/bin/python
import eyed3
import re
import os
import sys
import logging
logging.basicConfig()
logger = logging.getLogger('logger')
# logger.warning('The system may break down')

if (len(sys.argv)<3):
    print "Usage:"
    print sys.argv[0] + " [MUSIC DIRECTORY] [PATTERNS]..."
    print "Example: " + sys.argv[0] + " " + "\"/mnt/music.s/jukebox\" \"vocal\" \"flute\""
    sys.exit("To few arguments")

print "Patterns:"
for i in range(len(sys.argv)):
    if (i>1):
        # For each pattern
        pattern = sys.argv[i]
        print pattern

# sys.exit("DEBUG")
        
def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            print "Directory: " + fullPath
            getListOfFiles(fullPath)
        else:
            if fullPath.endswith((".mp3", ".flac")):
                # Init
                allfound = False
                found = False
                if entry.startswith(("+")):
                    print "Incorrect name: fullPath"
                try:
                    audiofile = eyed3.load(unicode(fullPath,"utf-8"))
                    allFound = False
                    if audiofile:
                        allfound = True
                        for i in range(len(sys.argv)):
                            if (i>1):
                                # For each pattern
                                pattern = sys.argv[i]
                                found = False
                                for comment in audiofile.tag.comments:
                                    comment_txt = comment.text
                                    match = re.search(pattern, comment_txt)
                                    if match:
                                        # print "Match: " + pattern
                                        found = True
                                        # print "-------------------------"
                                        # print comment_txt
                                        # print "-------------------------"
                                if not found:
                                    allfound = False
                except:
                    allfound = False
                    print ("No tag for: " + fullPath)
                if allfound:
                    os.system ("clementine -a \"" + fullPath + "\"")
                    print "clementine - a \"" + fullPath + "\""

dirName = sys.argv[1]
print "Analysing " + sys.argv[1]
getListOfFiles(dirName)
