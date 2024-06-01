from time import sleep
from threading import *

from sunjrayru import *
from sunjraydu import *


# Generate one zip file for every minute
class GMZIPFILE(Thread):
    def run(self):
        print("Program Started")
        create_dirs_pwd()
        create_dirs_sunjray()
        while True:
            try:
                zfgen_main()
            except:
                pass


class SUNJRAYUpload(Thread):
    def run(self):
        print("SUNJRAY Upload Thread Starts")
        while True:
            try:
                sunjrayrumain()
            except:
                print("Exception in SUNJRAY Realtime upload")
            try:
                sunjraydumain()
            except:
                print("Exception in SUNJRAY Delayed upload")


if __name__  == "__main__":
    t1 = GMZIPFILE()
    t1.start()
    sleep(5)


    t2 = SUNJRAYUpload()
    t2.start()
    sleep(5)


