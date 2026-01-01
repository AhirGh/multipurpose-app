import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QMainWindow,  QPushButton, QStackedWidget, QScrollArea, QGridLayout
from PyQt5.QtCore import Qt, QTimer, QTime, pyqtSignal
from PyQt5.QtGui import QFont, QFontDatabase, QIcon

def obtainfont(path):
    #dealing with custom fonts
    font_id = QFontDatabase.addApplicationFont(path)
    #note, fontfamilies method returns a full list, we only need the first element from it
    if font_id != -1:
        return QFontDatabase.applicationFontFamilies(font_id)[0]
    else:
        return "Arial"
    
#stopwatch portion
class stopwatch(QWidget):

    #note, a pyqtsignal MUST be declared as a class-wide variable, pyqt under the hood gives every instance specific signals. You make a signal, its created. you 'emit' the signal, i.e. signal broadcasted, and any slot functions assigned to the signal using 'connect' will now run
    goBack = pyqtSignal()

    def __init__(self):
        super().__init__()

        #for managing lap gui
        self.lapContents = QWidget()
        self.lapLayout = QVBoxLayout(self.lapContents)
        self.lapLabel = QLabel("Laplist:")

        #time and time label and buttons for actual stopwatch stuff
        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel("00:00:00:00", self)
        self.startButton = QPushButton("Start", self)
        self.stopButton = QPushButton("Stop", self)
        self.resetButton = QPushButton("Reset", self)
        self.lapButton = QPushButton("Lap", self)
        self.timer = QTimer(self)

        #maxlaps and lap tracking
        self.MAXLAPS = int(10)
        self.lapCount = 0

        #back button for navigation
        self.back_btn = QPushButton("Back")

        self.initGUI()

    def initGUI(self):
        
        font_family = obtainfont("C:\\Users\\asus\\VSc Codefolder\\python progs\\multipurpose app\\digital.ttf")

        #scroll area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        #lap contents set to scrollable
        scroll.setWidget(self.lapContents)

        #layout managing, stretch is to put empty space to bottom
        vbox = QVBoxLayout(self)
        hbox1 = QHBoxLayout()
        vbox.addWidget(self.back_btn)
        hbox1.addWidget(self.startButton)
        hbox1.addWidget(self.stopButton)
        hbox1.addWidget(self.lapButton)
        hbox1.addWidget(self.resetButton)
        vbox.addWidget(self.time_label)
        vbox.addLayout(hbox1)
        vbox.addWidget(scroll)
        self.lapLayout.addWidget(self.lapLabel)
        self.lapLayout.addStretch()

        #giving time_label an unique id
        self.time_label.setObjectName("timelabel")
        #styling note it's quite tricky, in f-str, escape '{' by using {{
        self.setStyleSheet(f"""
                           QPushButton {{background-color: black; color: #ff6900; font-family: {font_family}; font-size: 48px; border: 1px solid #ff6900; padding: 20px;}} 

                           QPushButton:hover {{background-color: #1e1e1e}} 
                           
                           QLabel {{ font-family: {font_family}; font-size: 48px; font-weight: 700; color: #ff6900; border: 1px solid #ff6900; background-color: black; }}
                           
                           #timelabel {{font-size: 144px; text-align: center; }}""")
        
        self.time_label.setAlignment(Qt.AlignCenter)

        #performing connections
        self.back_btn.clicked.connect(self.goBack.emit)
        self.startButton.clicked.connect(lambda: self.timer.start(10))
        self.stopButton.clicked.connect(lambda: self.timer.stop())
        self.resetButton.clicked.connect(self.reset)
        self.lapButton.clicked.connect(self.lap)
        self.timer.timeout.connect(self.update_time)

    def reset(self):
        self.time_label.setText("00:00:00:00")
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
    
    def  lap(self):

        #if stopwatch not started, don't bother lapping
        if self.time == QTime(0, 0, 0, 0):
            return
        
        #increment lapcount, make a label and a delete button 
        self.lapCount += 1
        newLap = QLabel(f"{self.lapCount}. {self.format_time(self.time)}")
        newDel = QPushButton("X")

        #and add them to layout, stretch = ratio division
        hbox = QHBoxLayout()
        hbox.addWidget(newLap, stretch= 4)
        hbox.addWidget(newDel, stretch= 1)

        #get index of last element in laplayout
        index = self.lapLayout.count()
        #delete oldest entry when number of laps = MAXLAPS
        if index - 1 > self.MAXLAPS:
            #get the oldest hbox
            for i in range(self.lapLayout.count()):
                item = self.lapLayout.itemAt(i)
                if item.layout() is not None:
                    oldest_hbox = item.layout()
                    self.delete_lap(oldest_hbox)
                    break

        #insert the stuff to the second last posn, stretch remains at last
        self.lapLayout.insertLayout(index - 1, hbox)

        #connect to the deletion function WITH the proper hbox
        newDel.clicked.connect(lambda _, h=hbox: self.delete_lap(h))

    def update_time(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))

    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        msec = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}:{msec:02}"
    
    def delete_lap(self, hbox):

        #remove all stuff from the hbox (label and delete button)
        for i in reversed(range(hbox.count())):
            item = hbox.itemAt(i).widget()

            #if item is indeed a widget, delete it
            if item:
                item.deleteLater()
        #removing that hbox which contains the signalling delete button
        for i in range(self.lapLayout.count()):
            item = self.lapLayout.itemAt(i)
            if item.layout() == hbox:
                self.lapLayout.takeAt(i)
                break

def main():
    app = QApplication(sys.argv)
    stopwatch_ob = stopwatch()
    stopwatch_ob.setWindowTitle("Stopwatch App")
    stopwatch_ob.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
