import os
import shutil
from config import *

pwd = os.getcwd()

bkpfld_path = os.path.join(pwd, bkpdir)
sunjray_path = os.path.join(pwd, sunjraydir)

sunjray_realtime_path = os.path.join(sunjray_path, rtdir)
sunjray_delayed_path = os.path.join(sunjray_path, dlydir)


# Create BKPDIR,SUNJRAY folders in the present working directory(pwd) for functionality of the program.
def create_dirs_pwd():
    isdir1 = os.path.isdir(bkpdir)
    if isdir1 == 0:
        os.mkdir(bkpfld_path)
        print(bkpdir+" directory created")
    else:
        print(bkpdir+" directory is already exists.")

    isdir3 = os.path.isdir(sunjraydir)
    if isdir3 == 0:
        os.mkdir(sunjray_path)
        print(sunjraydir+" directory created")
    else:
        print(sunjraydir+" directory is already exists.")


# Create directories Realtime and Delayed in SUNJRAY.
def create_dirs_sunjray():
    sf1 = os.path.isdir(sunjray_realtime_path)
    if sf1 == 0:
        os.mkdir(sunjray_realtime_path)
        print(rtdir+" sub-directory created in "+sunjraydir)
    else:
        print(rtdir+" sub-directory already exists in "+sunjraydir)

    sf2 = os.path.isdir(sunjray_delayed_path)
    if sf2 == 0:
        os.mkdir(sunjray_delayed_path)
        print(dlydir+" sub-directory created in "+sunjraydir)
    else:
        print(dlydir+" sub-directory already exists in "+sunjraydir)





if __name__ == "__main__":
    create_dirs_pwd()
    create_dirs_sunjray()
