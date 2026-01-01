import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QStackedWidget
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QFontDatabase, QIcon

def obtainfont(path):
    #dealing with custom fonts
    font_id = QFontDatabase.addApplicationFont(path)
    #note, fontfamilies method returns a full list, we only need the first element from it
    if font_id != -1:
        return QFontDatabase.applicationFontFamilies(font_id)[0]
    else:
        return "Arial"
    
class Weather(QWidget):

    goBack = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.cityLabel = QLabel("Enter City name:", self)
        self.cityInput = QLineEdit(self)
        self.cityInput.setPlaceholderText("City name here")
        self.weatherBtn = QPushButton("Get Weather", self)
        self.dataLabel = QLabel("Temperature", self)
        self.symbLabel = QLabel("❓", self)
        self.descLabel = QLabel("Sunny", self)
        self.backBtn = QPushButton("Back", self)
        self.initGUI()


    def initGUI(self):

        #obtain required fonts
        font_family = obtainfont("C:\\Users\\asus\\VSc Codefolder\\python progs\\multipurpose app\\Aadhunik.ttf")
        font_family2 = obtainfont("C:\\Users\\asus\\VSc Codefolder\\python progs\\multipurpose app\\seguiemj.ttf")

        #layout managing
        vbox = QVBoxLayout(self)
        vbox.addWidget(self.backBtn)
        vbox.addWidget(self.cityLabel)
        vbox.addWidget(self.cityInput)
        vbox.addWidget(self.weatherBtn)
        vbox.addWidget(self.dataLabel)
        vbox.addWidget(self.symbLabel)
        vbox.addWidget(self.descLabel)

        #aligning them
        self.cityLabel.setAlignment(Qt.AlignCenter)
        self.cityInput.setAlignment(Qt.AlignCenter)
        self.dataLabel.setAlignment(Qt.AlignCenter)
        self.descLabel.setAlignment(Qt.AlignCenter)
        self.symbLabel.setAlignment(Qt.AlignCenter)

        #assigning them ids to style them in sheet
        self.cityLabel.setObjectName("cityLabel")
        self.cityInput.setObjectName("cityInput")
        self.dataLabel.setObjectName("dataLabel")
        self.descLabel.setObjectName("descLabel")
        self.symbLabel.setObjectName("symbLabel")
        self.weatherBtn.setObjectName("weatherBtn")
        self.backBtn.setObjectName("backBtn")

        #setting up a stylesheet
        self.setStyleSheet(f"""
        #weatherBtn, #backBtn {{
                           background-color: #001f77;
                           font-family: {font_family};
                           font-size: 48px;
                           padding: 5px;
                           border-radius: 5px;
                           border: 2px solid #00d80b;
                           font-weight: 700;
                           color: #00d80b;
                           }}
        #weatherBtn:hover, #backBtn:hover  {{
                            background-color: #002797;
                            color: #00ff0c;
                            border: 3px dotted #00ff0c; 
        }}
        #cityInput {{
                            background-color: #2c0423;
                            font-family: {font_family};
                            font-size: 48px;
                            font-style: normal;
                            color: #00d80b;
                            }}
        #cityInput:hover {{
                            background-color: #5f044a;
                            }}
        #cityLabel, #descLabel {{
                            background-color: #36005b;
                            color: #00d80b;
                            font-family: {font_family};
                            font-weight: 500;
                            font-size: 48px;
                            font-style: oblique;
                            border: 2px solid #00d80b
                            }}
        #dataLabel       {{
                            background-color: black;
                            color: #00d80b;
                            font-family: {font_family};
                            font-weight: 500;
                            font-size: 36px;
                            border: 2px solid #00d80b
                            }}
        #symbLabel       {{
                            background-color: black;
                            font-size: 96px;
                            font-family: {font_family2};
                            color: white}}
        #descLabel       {{
                            font-style: normal}}
        #backBtn         {{
                            background-color: black;}}
        #backBtn:hover   {{
                            background-color: #1e1e1e;}}""")
        
        self.backBtn.clicked.connect(self.goBack.emit)
        self.weatherBtn.clicked.connect(self.getWeather)

    def getWeather(self):

        #get the cityname
        cityName  = self.cityInput.text().capitalize()

        #in case user puts no cityname
        if not cityName:
            self.cityInput.setPlaceholderText("Required!")
            return

        #setting gui elements
        self.dataLabel.setText("Fetching Data, Please Wait...")
        self.symbLabel.setText("⏳")

        #apikey for making requests
        apiKey = "YOUR_API_KEY_HERE"

        #crafting url to make requests
        url = f"https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apiKey}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.displayWeather(data)
        except requests.exceptions.HTTPError as error:
            match response.status_code:
                case 400:
                    self.displayError("Error 400 Bad Request\n")
                case 401:
                    self.displayError("Error 401 Unauthorized\n")
                case 403:
                    self.displayError("Error 403 Access Denied\n")
                case 404:
                    self.displayError("Error 404 Not Found\n")
                case 500:
                    self.displayError("Error 500 Internal Server Error\n")
                case 502:
                    self.displayError("Error 502 Bad Gateway\n")
                case 503:
                    self.displayError("Error 503 Service Unavailable\n")
                case 504:
                    self.displayError("Error 504 Gateway Timeout\n")
                case _:
                    self.displayError(f"HTTP error occured {error}")

        except requests.exceptions.ConnectionError:
            self.displayError("Connection Error!\n")
        except requests.exceptions.Timeout:
            self.displayError("Request Timeout\n")
        except requests.TooManyRedirects:
            self.displayError("Too Many Redirects, Check URL")
        except requests.exceptions.RequestException as error:
            self.displayError(f"An Error Occured, {error}")

    def displayError(self, message):
        self.cityInput.setText("")
        self.cityInput.setPlaceholderText("Error Occured")
        #self.dataLabel.setStyleSheet("font-size: 48px")
        self.dataLabel.setText(message)
        self.symbLabel.setText("⚠")
        self.descLabel.setText("No Description...")

    def displayWeather(self, data):

        #parse json file
        tempCelcius = round(data["main"]["temp"] - 273.15)
        feelsLike = round(data["main"]["feels_like"] - 273.15)
        humidity = data["main"]["humidity"]
        visibility = data["visibility"]/1000
        cloudCover = data["clouds"]["all"]
        wind = data["wind"]["speed"]
        lat = data["coord"]["lat"]
        lon = data["coord"]["lon"]
        descSmall = data["weather"][0]["main"]

        #set weather and location data
        self.dataLabel.setText(f"""Latitude: {lat}\tLongitude:{lon}
Visibility: {visibility:02}km\tCloud Cover: {cloudCover}%
Humidity: {humidity}%\tWind: {wind}km/h
Actual: {tempCelcius}°C\tFeels Like: {feelsLike}°C""")
        
        #setup description
        self.descLabel.setText(f"""{descSmall.capitalize()}""")

        #get a proper emoji icon to show
        self.symbLabel.setText(Weather.getSymbol(data["weather"][0]["id"]))

    @staticmethod
    def getSymbol(weatherID):
        if 200 <= weatherID <= 232:
            return "⛈️"
        elif 300 <= weatherID <= 321:
            return "⛅"
        elif 500 <= weatherID <= 531:
            return "🌧️"
        elif 600 <= weatherID <= 622:
            return "🌨️"
        elif 701 <= weatherID <= 741:
            return "🌫️"
        elif weatherID == 762:
            return "🌋"
        elif weatherID == 771:
            return "🍃"
        elif weatherID == 781:
            return "🌪️"
        elif weatherID == 800:
            return "🌞"
        elif 801 <= weatherID <= 804:
            return "☁️"
        else:
            return "❔"

def main():
    app = QApplication(sys.argv)
    weather_ob = Weather()
    weather_ob.show()
    sys.exit(app.exec_())

if __name__ == "__main__":

    main()
