from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
#from future_builtins import *

import sys # we import sys module becoz we want to access e command-line arguments it holds in the sys.argv list
import time

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


app = QApplication(sys.argv)

try:
    due = QTime.currentTime()
    print(due)
    message = "Alert!"
    print(sys.argv)
    print(len(sys.argv))
    if len(sys.argv) < 2:
        raise ValueError
    hours, mins = sys.argv[1].split(":")
    due = QTime(int(hours), int(mins))
    print(due)
    if not due.isValid():
        raise ValueError
    if len(sys.argv) > 2:
        message = " ".join(sys.argv[2:])# if time is valid we set e message to b e space-separated concatenation of e othercommand-lin arguments if any
except ValueError:
    message = "Usage: alert.pyw HH:MM [optional message]" # 24hr clock
due = QTime.currentTime()
while QTime.currentTime() < due:
    time.sleep(20) # 20 seconds

label = QLabel("<font color=red size=72><b>{0}</b></font>"
               .format(message))
label.setWindowFlags(Qt.SplashScreen)
label.show()#show() only schedules a 'paint event'.it adds a new event to e QApplication object event queue
QTimer.singleShot(60000, app.quit) # 1 minute
app.exec_() #starts event loop

