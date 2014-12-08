import sys
import time
from datetime import datetime

def currentpeopleconnectedtointernet():
        ts = time.time()
        tsnow = int(ts*1000)
#       tsnow = 1420066799000 #endof2014testvalue
        ts2014 = 1388530800000
        tssince = tsnow-ts2014
        ppms = 0.0067492106651900 
        return int(2710380995.17892 + (ppms*tssince))

while 1:
        sys.stdout.write('\rPeople connected to Internet right now (according to ITU): {0:10d} '.format(currentpeopleconnectedtointernet()))
        sys.stdout.flush()
        time.sleep(0.05)
