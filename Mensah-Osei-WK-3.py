'''
Osei mensah's solution 

'''

''' IMPORT STANDARD LIBRARIES '''
import os       # File System Methods
import sys      # System Methods
import time     # Time Conversion Methods
import hashlib  # Python standard library hashlib


''' IMPORT 3RD PARTY LIBRARIES '''
from prettytable import PrettyTable # pip install prettytable

''' DEFINE PSEUDO CONSTANTS '''
#Change to directory as required


''' LOCAL FUNCTIONS '''

def GetFileMetaData(fileName):
    ''' 
        obtain filesystem metadata
        from the specified file
        specifically, fileSize and MAC Times
        
        return True, None, fileSize and MacTimeList
    '''
    try:
        metaData         = os.stat(fileName)       # Use the stat method to obtain meta data
        fileSize         = metaData.st_size         # Extract fileSize and MAC Times
        timeLastAccess   = metaData.st_atime
        timeLastModified = metaData.st_mtime
        timeCreated      = metaData.st_ctime
        
        macTimeList = [timeLastModified, timeLastAccess, timeCreated] # Group the MAC Times in a List
        return True, None, fileSize, macTimeList
    
    except Exception as err:
        return False, str(err), None, None

''' LOCAL CLASSES '''
# NONE

''' MAIN ENTRY POINT '''

if __name__ == '__main__':
    DIR = input("Please Enter Starting Directory: ")
    if not os.path.isdir(DIR):
        print("invalid directory...please enter a valid directory path") 
        
    tb1 = PrettyTable(['Path','Status','FileSize','LastModified','LastAccess','Created', 'SHA-256 HASH', 'Error Info'])
    print("Walking: ", DIR, "\n")         
    try:
        # Perform the os.walk, starting at the target directory
        # TODO: Change this from a pseudo-constant to a user-specified directory using input()
        for root, dirs, fileList in os.walk(DIR):
            
            
            # For each of the files in the file list, do the following:
            for nextFile in fileList:
                try:
                    
                    # Get the absolute path of the file--to be used for reporting and getting the file hash
                    path = os.path.join(root, nextFile)
                    absPath = os.path.abspath(path)
                    # Call the GetFileMetadata function (from week 2 solution)
                    success, errInfo, fileSize, macList = GetFileMetaData(absPath)
                    
                    # Open each file in read binary mode
                    with open(absPath, 'rb') as targetFile:
                        # Read the contents of the file and get the file hash
                        fileContents = targetFile.read()
                        sha256Obj = hashlib.sha256()
                        sha256Obj.update(fileContents)
                        hexDigest = sha256Obj.hexdigest()
                        tb1.add_row([ absPath, 'OK', fileSize,
                                      time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(macList[0])),
                                      time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(macList[1])),
                                      time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(macList[2])),
                                      hexDigest, ''])
                        
                except Exception as err:
                    # add exception to pretty table here
                    tb1.add_row( [nextFile, 'ERR', 0, 'ERR', 'ERR', 'ERR', 'ERR', str(err)] )
        
       
    except Exception as err:
       
        print("\n\nScript Aborted     ", "Exception =     ", err)        
    tb1.align = "l"
    print(tb1.get_formatted_string())
    print("Script end")