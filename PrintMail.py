import platform

# Windows print imports
import tempfile
import win32api
import win32print

# Linux print imports
import subprocess

def printmail(subject, body):
    print("Printing \"" + subject + "\"...")
    printcontent = subject + "\n\n\n" + body
    if platform.system() is 'Windows':
        # Print mail on windows
        filename = tempfile.mktemp(".txt")
        open (filename, "w").write (printcontent)
        win32api.ShellExecute (
        0,
        "print",
        filename,
        '/d:"%s"' % win32print.GetDefaultPrinter(),
        ".",
        0
        )
    elif platform.system() is 'Linux':
        # Print mail on Linux
        lpr = subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
        lpr.stdin.write(printcontent)
