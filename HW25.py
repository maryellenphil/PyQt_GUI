# Mary-Ellen Phillips

from PyQt5.QtCore import QDate, QTime, QDateTime, Qt, QTimeZone 
now = QDate.currentDate()
#print(now)
print(now.toString(Qt.ISODate))
print(now.toString(Qt.DefaultLocaleLongDate))
print('')

dateTime = QDateTime.currentDateTime()
print(dateTime.toString())
print('')

print('Print the time:')
time = QTime.currentTime()
print(time.toString(Qt.DefaultLocaleLongDate))
print('')

print('Print the month:')
getTimeStr = dateTime.toString()
print(getTimeStr[4:7])
print('')

# days in month/year
d = QDate(1945,5,7)
print("Days in month: %s" % d.daysInMonth())
print("Days in year: %s" % d.daysInYear())
print('')

# difference in days 
xmas1 = QDate(2019,12,24)
xmas2 = QDate(2018,12,24)

now = QDate.currentDate()
daysPassed = xmas2.daysTo(now)
print('%s days passed since last Xmas' % daysPassed)
print('')

# datetime aritmetic 
now = QDateTime.currentDateTime()
print('Today: %s' % now.toString(Qt.ISODate))
print('Adding 12 days: %s' % now.addDays(12).toString(Qt.ISODate))
print('Subtracting 22 days: %s' % now.addDays(-22).toString(Qt.ISODate))
print('Adding 55 seconds: %s' % now.addSecs(55).toString(Qt.ISODate))
print('Adding 3 months: %s' % now.addMonths(3).toString(Qt.ISODate))
print('Adding 12 years: %s' % now.addYears(12).toString(Qt.ISODate))
print('')

# daylight saving time (DST)
now = QDateTime.currentDateTime()
print('Time Zone: %s' % now.timeZoneAbbreviation())

if now.isDaylightTime():
    print('The current date falls into DST')
else:
    print('The current date does not fall into DST')

print('')

# a simple window 
import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox, QDesktopWidget
from PyQt5.QtGui import QIcon, QFont

#app = QApplication(sys.argv)
#w = QWidget()
#w.resize(350,150)
#w.move(300,300)
#w.setWindowTitle('Simple')
#w.show()

#sys.exit(app.exec_())

# an application icon
#class Example(QWidget):
#    def __init__(self):
#        super().__init__()
#        self.initUI()
#    def initUI(self):
#        self.setGeometry(300,300,300,220)
#        self.setWindowTitle('Icon')
#        self.setWindowIcon(QIcon('web.png'))

#        self.show()

#app = QApplication(sys.argv)
#ex = Example()
#sys.exit(app.exec_())

# a push button
#class Example(QWidget):
#    def __init__(self):
#        super().__init__()
#        self.initUI()
#    def initUI(self):
#        QToolTip.setFont(QFont('SansSerif',10))
#        self.setToolTip('This is a <b>QWidget</b> widget')
#        btn = QPushButton('Button',self)
#        btn.setToolTip('This is a <b>QPushButton</b> widget')
#        btn.resize(btn.sizeHint())
#        btn.move(50,50)
#        self.setGeometry(300,300,300,200)
#        self.setWindowTitle('ToolTips')
#        self.show()
#app = QApplication(sys.argv)
#ex = Example()
#sys.exit(app.exec_())


# closing a window
#class Example(QWidget):
#    def __init__(self):
#        super().__init__()
#        self.initUI()
#    def initUI(self):
#        qbtn = QPushButton('Quit',self)
#        qbtn.clicked.connect(QApplication.instance().quit)
#        qbtn.resize(qbtn.sizeHint())
#        qbtn.move(50,50)
#        self.setGeometry(300,300,450,150)
#        self.setWindowTitle('Quit button')
#        self.show()
#app = QApplication(sys.argv)
#ex = Example()
#sys.exit(app.exec_())

# message box
#class Example(QWidget):
#    def __init__(self):
#        super().__init__()
#        self.initUI()
#    def initUI(self):
#        self.setGeometry(300,300,450,150)
#        self.setWindowTitle('Message box')
#        self.show()
#    def closeEvent(self,event):
#        reply = QMessageBox.question(self, 'Message',"Are you sure you want to quit?",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
#        if reply == QMessageBox.Yes:
#            even.accept()
#        else:
#            event.ignore()
#app = QApplication(sys.argv)
#ex = Example()
#sys.exit(app.exec_())

# centering window
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.resize(450,150)
        self.center()
        self.setWindowTitle('Center')
        self.show()
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
