import subprocess
import csv
import re
import os
import sys
import importlib.util

# Taken from here
# http://www.py2exe.org/index.cgi/HowToDetermineIfRunningFromExe
def isRunningAsExe():
    # Modern replacement for imp.is_frozen
    is_frozen = getattr(sys, "frozen", False)
    return (hasattr(sys, "frozen") or  # new py2exe
            hasattr(sys, "importers") or  # old py2exe
            is_frozen)  # tools/freeze replacement

def getExecDirectory():
    return os.path.dirname(sys.argv[0])

def tryKillAdbExe(sysManager):
    try:
        sysManager.executeAndWait('taskkill /f /IM adb.exe')
    except:
        pass

def doesProcessExist(pattern):
    p_tasklist = subprocess.Popen('tasklist.exe /fo csv', stdout=subprocess.PIPE, universal_newlines=True)

    for p in csv.DictReader(p_tasklist.stdout):
        if re.match(pattern, p['Image Name']):
            return True

    return False
