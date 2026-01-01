import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QMainWindow,  QPushButton, QStackedWidget, QScrollArea, QGridLayout
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QFont, QFontDatabase, QIcon

import clockApp, stopwatchApp, weatherApp  

def obtainfont(path):
    #dealing with custom fonts
    font_id = QFontDatabase.addApplicationFont(path)
    #note, fontfamilies method returns a full list, we only need the first element from it
    if font_id != -1:
        return QFontDatabase.applicationFontFamilies(font_id)[0]
    else:
        return "Arial"

#main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #adding buttons
        self.clock_btn = QPushButton("Clock", self)
        self.stopwatch_btn = QPushButton("Stopwatch", self)
        self.weather_btn = QPushButton("Weather", self)

        #adding menu-style tab switching
        self.pages = QStackedWidget()
        self.menuPage = self.menuPageCreate()
        self.clockPage = clockApp.clock()
        self.stopwatchPage = stopwatchApp.stopwatch()
        self.weatherPage = weatherApp.Weather()
        self.initGUI()

    def initGUI(self):
        #set style, positioning, titles and icon
        self.setStyleSheet("background-color: black;")
        self.setWindowTitle("Multipurpose App")
        self.setWindowIcon(QIcon("C:\\Users\\asus\\VSc Codefolder\\python progs\\multipurpose app\\icon.png"))

        #add tabs
        self.pages.addWidget(self.menuPage)
        self.pages.addWidget(self.clockPage)
        self.pages.addWidget(self.stopwatchPage)
        self.pages.addWidget(self.weatherPage)

        #set logic to switch tabs
        self.clock_btn.clicked.connect(lambda: self.pages.setCurrentIndex(1))
        self.stopwatch_btn.clicked.connect(lambda: self.pages.setCurrentIndex(2))
        self.weather_btn.clicked.connect(lambda: self.pages.setCurrentIndex(3))

        #set back going logic
        self.clockPage.goBack.connect(lambda: self.pages.setCurrentIndex(0))
        self.weatherPage.goBack.connect(lambda: self.pages.setCurrentIndex(0))
        self.stopwatchPage.goBack.connect(lambda: self.pages.setCurrentIndex(0))

        #set the stacked widget as the central widget
        self.setCentralWidget(self.pages)
        
    def menuPageCreate(self):
        font_family = obtainfont("C:\\Users\\asus\\VSc Codefolder\\python progs\\multipurpose app\\Cerebro.ttf")

        #make a widget to serve as a selector
        page = QWidget()
        

        #set page style
        page.setStyleSheet(f"QPushButton {{background-color: black; color: #ff6900; border: 1px solid #ff6900; font-family: {font_family}; font-size: 48px}} QPushButton:hover {{background-color: #1e1e1e}}")

        #make layout manager and add buttons to it
        grid = QGridLayout(page)
        grid.addWidget(self.clock_btn, 0, 0)
        grid.addWidget(self.stopwatch_btn, 0, 1)
        grid.addWidget(self.weather_btn, 1, 0)

        #grid.setRowStretch(2, 1)      # extra space goes down
        #grid.setColumnStretch(2, 1)   # extra space goes right


        return page
        


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
#ff6900 neon orange