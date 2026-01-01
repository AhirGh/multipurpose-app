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
    
class clock(QWidget):

    #note, a pyqtsignal MUST be declared as a class-wide variable, pyqt under the hood gives every instance specific signals
    goBack = pyqtSignal()

    def __init__(self):
        super().__init__()

        #buttons for navigation
        self.back_btn = QPushButton("Return to Menu")

        #label to show time
        self.timeinfo = QLabel(self)

        #timer to update time
        self.timer = QTimer(self)

        self.initGUI()
    
    def initGUI(self):

        font_family = obtainfont("C:\\Users\\asus\\VSc Codefolder\\python progs\\multipurpose app\\digital.ttf")

        #styling and aligment
        self.setStyleSheet(f"""QWidget {{background-color: black;}} 
                           QLabel {{ font-family: {font_family}; font-size: 144px; color: #ff6900; border: 1px solid #ff6900}} 
                           QPushButton {{background-color: black; color: #ff6900; border: 1px solid #ff6900; font-family: {font_family};}} 
                           QPushButton:hover {{background-color: #1e1e1e}}""")
        self.timeinfo.setAlignment(Qt.AlignCenter)

        #perform connection
        self.back_btn.clicked.connect(self.goBack.emit)
        
        # layout managers
        hbox = QHBoxLayout()
        hbox.addWidget(self.back_btn)
        #nesting layout managers
        vbox = QVBoxLayout(self)
        vbox.addLayout(hbox)
        vbox.addWidget(self.timeinfo)

        #set font of label and buttons
        self.timeinfo.setFont(QFont(font_family, 150))
        self.back_btn.setFont(QFont(font_family, 48))

        #update once every 1000ms (1s)
        self.timer.timeout.connect(self.put_time)
        self.timer.start(1000)


        self.put_time()

    def put_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss A")
        self.timeinfo.setText(current_time)
        

def main():
    app = QApplication(sys.argv)
    clock_ob = clock()
    clock_ob.setWindowTitle("Clock App")
    clock_ob.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()