# Multipurpose App

A PyQt5-based desktop application that combines three essential utilities in one sleek interface: a digital clock, a precision stopwatch, and a real-time weather information tool.

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.7+-green)
![PyQt5](https://img.shields.io/badge/PyQt5-5.15+-orange)

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#projectstructure)
- [Configuration](#configuration)
- [Dependencies](#dependencies)
- [API Setup](#apisetup)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [License](#license)

<a id="features"></a>
## Features 

### Digital Clock
- Real-time digital clock display with 12-hour format
- Large, easy-to-read LED-style display
- Updates every second with precise time including AM/PM indicator
- Custom digital font for authentic LED clock appearance

### Stopwatch
- High-precision timing (10ms accuracy)
- Start, Stop, Reset, and Lap functionality
- Lap recording system with up to 10 saved laps
- Individual lap deletion capability
- Scrollable lap list for easy viewing
- Time format: HH:MM:SS:MS (hours, minutes, seconds, milliseconds)

### Weather Information
- Real-time weather data from OpenWeatherMap API
- Displays comprehensive weather information:
  - Current temperature (in Celsius)
  - "Feels like" temperature
  - Humidity percentage
  - Wind speed
  - Visibility
  - Cloud cover percentage
  - Geographic coordinates (latitude/longitude)
- Weather condition emojis for visual representation
- Detailed error handling for network issues
- Search by city name

### UI/UX Features
- Modern dark theme with neon accent colors
- Intuitive navigation between modules
- Custom fonts for enhanced visual appeal
- Responsive layout design
- Hover effects on interactive elements
- Clean, minimalist interface

<a id="installation"></a>
## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone or Download the Repository

```bash
git clone <repository-url>
cd multipurpose-app
```

### Step 2: Install Required Dependencies

```bash
pip install PyQt5 requests
```

Or use the requirements file (if provided):

```bash
pip install -r requirements.txt
```

### Step 3: Download Required Fonts

The application uses custom fonts for enhanced visual appeal. You'll need the following font files:

- `digital.ttf` - For Clock and Stopwatch displays
- `Cerebro.ttf` - For main menu buttons
- `Aadhunik.ttf` - For Weather app text
- `seguiemj.ttf` - For emoji display in Weather app

Place these font files in the same directory as the Python files, or update the font paths in the code.

### Step 4: Set Up API Key

1. Sign up for a free account at [OpenWeatherMap](https://openweathermap.org/api)
2. Generate an API key from your account dashboard
3. Open `weatherApp.py` and replace the API key on line 79:

```python
apiKey = "YOUR_API_KEY_HERE"
```

### Step 5: Update File Paths

Update the font and icon file paths in each Python file to match your system:

**In `multipurpose.py`:**
```python
self.setWindowIcon(QIcon("path/to/your/icon.png"))
```

**Font paths in all files:**
```python
font_family = obtainfont("path/to/your/font.ttf")
```

<a id="usage"></a>
## Usage

### Running the Application

Execute the main application file:

```bash
python multipurpose.py
```

Alternatively, you can run individual modules independently:

```bash
python clockApp.py      # Run Clock only
python stopwatchApp.py  # Run Stopwatch only
python weatherApp.py    # Run Weather only
```

### Using the Clock

1. Launch the application
2. Click the **"Clock"** button from the main menu
3. View the current time in large digital format
4. Click **"Return to Menu"** to go back

### Using the Stopwatch

1. Click the **"Stopwatch"** button from the main menu
2. Click **"Start"** to begin timing
3. Click **"Lap"** to record lap times (up to 10 laps saved)
4. Click **"Stop"** to pause the stopwatch
5. Click **"Reset"** to clear the time
6. Delete individual laps by clicking the **"X"** button next to each lap
7. Click **"Back"** to return to the main menu

### Using the Weather App

1. Click the **"Weather"** button from the main menu
2. Enter a city name in the input field
3. Click **"Get Weather"** to fetch current weather data
4. View comprehensive weather information including:
   - Temperature and "feels like" temperature
   - Humidity and wind speed
   - Visibility and cloud cover
   - Weather condition with emoji
5. Search for different cities as needed
6. Click **"Back"** to return to the main menu

<a id="projectstructure"></a>
## Project Structure

```
multipurpose-app/
│
├── multipurpose.py      # Main application entry point
├── clockApp.py          # Digital clock module
├── stopwatchApp.py      # Stopwatch module
├── weatherApp.py        # Weather information module
│
├── digital.ttf          # LED-style font for clock/stopwatch
├── Cerebro.ttf          # Font for main menu
├── Aadhunik.ttf         # Font for weather app
├── seguiemj.ttf         # Emoji font
├── icon.png             # Application icon
│
└── README.md            # This file
```

### File Descriptions

#### `multipurpose.py`
The main application controller that:
- Creates the main window and menu interface
- Manages navigation between different modules using `QStackedWidget`
- Implements the grid-based menu layout
- Handles window styling and icon setup
- Coordinates signals between modules for navigation

**Key Classes:**
- `MainWindow(QMainWindow)`: Main application window with stacked widget navigation

#### `clockApp.py`
Digital clock implementation featuring:
- Real-time display using `QTimer` with 1-second intervals
- Custom LED-style digital font rendering
- 12-hour time format with AM/PM
- PyQt signal for navigation back to main menu

**Key Classes:**
- `clock(QWidget)`: Clock widget with timer-based updates

**Key Methods:**
- `put_time()`: Updates the time display every second
- `initGUI()`: Sets up the UI components and styling

#### `stopwatchApp.py`
High-precision stopwatch with lap tracking:
- 10-millisecond precision timing
- Dynamic lap list with scrolling
- Maximum 10 laps stored (oldest automatically removed)
- Individual lap deletion capability
- Time formatting: HH:MM:SS:MS

**Key Classes:**
- `stopwatch(QWidget)`: Stopwatch widget with lap tracking functionality

**Key Methods:**
- `update_time()`: Updates stopwatch display every 10ms
- `lap()`: Records current time as a lap
- `delete_lap(hbox)`: Removes a specific lap entry
- `format_time(time)`: Formats QTime to display string
- `reset()`: Resets stopwatch to zero

#### `weatherApp.py`
Weather information retrieval and display:
- OpenWeatherMap API integration
- Comprehensive error handling for HTTP and network errors
- Real-time weather data parsing
- Weather condition emoji mapping
- Temperature conversion from Kelvin to Celsius

**Key Classes:**
- `Weather(QWidget)`: Weather widget with API integration

**Key Methods:**
- `getWeather()`: Fetches weather data from API
- `displayWeather(data)`: Parses and displays weather information
- `displayError(message)`: Handles and displays error messages
- `getSymbol(weatherID)` (static): Maps weather condition IDs to emojis

### Common Utility Function

All modules share the `obtainfont(path)` function:
- Loads custom TrueType fonts at runtime
- Returns font family name for styling
- Fallback to Arial if font loading fails

<a id="configuration"></a>
## Configuration

### Color Scheme Customization

The application uses two distinct color schemes:

**Clock & Stopwatch (Neon Orange):**
- Background: `#000000` (black)
- Accent: `#ff6900` (neon orange)
- Hover: `#1e1e1e` (dark gray)

**Weather (Neon Green):**
- Background layers: `#001f77`, `#2c0423`, `#36005b`
- Accent: `#00d80b` (neon green)
- Hover: `#002797`, `#5f044a`

To customize colors, modify the `setStyleSheet()` calls in each module's `initGUI()` method.

### Font Customization

Replace font files or update paths in the `obtainfont()` calls:

```python
font_family = obtainfont("path/to/your/custom/font.ttf")
```

### Stopwatch Lap Limit

Modify the maximum number of laps in `stopwatchApp.py`:

```python
self.MAXLAPS = int(10)  # Change to desired number
```

### Timer Intervals

**Clock update interval** (default: 1000ms = 1 second):
```python
self.timer.start(1000)  # In clockApp.py
```

**Stopwatch precision** (default: 10ms):
```python
self.timer.start(10)  # In stopwatchApp.py
```

<a id="dependencties"></a>
## Dependencies

### Required Python Packages

```
PyQt5 >= 5.15
requests >= 2.25.0
```

### System Requirements

- **Operating System**: Windows, macOS, or Linux
- **Python Version**: 3.7 or higher
- **RAM**: 256 MB minimum
- **Screen Resolution**: 1024x768 or higher recommended

### External APIs

- **OpenWeatherMap API**: Free tier allows 60 calls/minute and 1,000,000 calls/month

<a id="apisetup"></a>
## API Setup

### Getting Your OpenWeatherMap API Key

1. Visit [OpenWeatherMap](https://openweathermap.org/)
2. Click "Sign Up" and create a free account
3. Verify your email address
4. Navigate to "API keys" in your account dashboard
5. Copy your default API key or generate a new one
6. Paste it into `weatherApp.py` at line 79

### API Key Security

**Important**: Never commit your API key to public repositories!

Best practices:
- Use environment variables for API keys
- Add API key files to `.gitignore`
- Consider using a configuration file not tracked by git

Example using environment variables:

```python
import os
apiKey = os.environ.get('OPENWEATHER_API_KEY', 'default_key')
```

Then set the environment variable:
```bash
# Windows
set OPENWEATHER_API_KEY=your_api_key_here

# Linux/Mac
export OPENWEATHER_API_KEY=your_api_key_here
```
<a id="customisation"></a>
## Customization

### Adding New Modules

To add a new feature module:

1. Create a new Python file (e.g., `timerApp.py`)
2. Create a widget class with a `goBack` signal:
```python
class Timer(QWidget):
    goBack = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        # Your implementation
```

3. Import it in `multipurpose.py`:
```python
import timerApp
```

4. Add it to the main window:
```python
self.timerPage = timerApp.Timer()
self.pages.addWidget(self.timerPage)
```

5. Create a button and connect it:
```python
self.timer_btn = QPushButton("Timer", self)
self.timer_btn.clicked.connect(lambda: self.pages.setCurrentIndex(4))
self.timerPage.goBack.connect(lambda: self.pages.setCurrentIndex(0))
```

### Modifying Weather Data Display

The weather display can be customized in the `displayWeather()` method. Current data available:

- `data["main"]["temp"]` - Temperature (Kelvin)
- `data["main"]["feels_like"]` - Feels like temperature
- `data["main"]["humidity"]` - Humidity percentage
- `data["main"]["pressure"]` - Atmospheric pressure
- `data["wind"]["speed"]` - Wind speed
- `data["clouds"]["all"]` - Cloud coverage
- `data["weather"][0]["description"]` - Weather description
- `data["weather"][0]["id"]` - Weather condition ID

### Weather Emoji Mapping

Customize weather emojis in the `getSymbol()` static method:

```python
@staticmethod
def getSymbol(weatherID):
    if 200 <= weatherID <= 232:
        return "⛈️"  # Thunderstorm
    # Add your custom mappings
```

Weather ID ranges:
- 200-232: Thunderstorm
- 300-321: Drizzle
- 500-531: Rain
- 600-622: Snow
- 700-781: Atmosphere (fog, mist, etc.)
- 800: Clear sky
- 801-804: Clouds

<a id="troubleshooting"></a>
## Troubleshooting

### Common Issues and Solutions

#### Application Won't Start

**Problem**: ImportError for PyQt5 or requests
```
ModuleNotFoundError: No module named 'PyQt5'
```

**Solution**: Install required packages
```bash
pip install PyQt5 requests
```

#### Font Not Loading

**Problem**: Default Arial font is used instead of custom fonts

**Solution**: 
- Verify font files exist in the specified path
- Check file paths are correct for your operating system
- Use absolute paths or update relative paths
- Ensure font files are not corrupted

#### Weather Data Not Fetching

**Problem**: "Error 401 Unauthorized" or no weather data displayed

**Solution**:
- Verify your API key is valid and activated
- New API keys can take up to 2 hours to activate
- Check your internet connection
- Ensure city name is spelled correctly

**Problem**: "Error 404 Not Found"

**Solution**:
- Check city name spelling
- Try using common city names (e.g., "London" instead of small towns)
- Some cities may not be in the OpenWeatherMap database

#### Icon Not Displaying

**Problem**: Window icon doesn't appear

**Solution**:
- Verify `icon.png` exists at the specified path
- Update the path in `multipurpose.py` to match your file location
- Ensure the icon is in a supported format (PNG, ICO)

#### Stopwatch Lap Deletion Issues

**Problem**: Laps not deleting properly

**Solution**:
- This is usually caused by layout reference issues
- Restart the application
- If persistent, check the `delete_lap()` method implementation

### Platform-Specific Issues

#### Windows
- Use raw strings or double backslashes for file paths:
  ```python
  r"C:\Users\username\fonts\font.ttf"
  # or
  "C:\\Users\\username\\fonts\\font.ttf"
  ```

#### macOS/Linux
- Use forward slashes for paths:
  ```python
  "/home/username/fonts/font.ttf"
  ```
- May need to install PyQt5 dependencies:
  ```bash
  # Ubuntu/Debian
  sudo apt-get install python3-pyqt5
  
  # macOS
  brew install pyqt5
  ```

### Debug Mode

To enable debug output, add print statements in key methods:

```python
def getWeather(self):
    cityName = self.cityInput.text().capitalize()
    print(f"Fetching weather for: {cityName}")  # Debug line
    # ... rest of method
```

<a id="license"></a>
## 📄 License

This project is provided as-is for educational and personal use.

## Contributing

Suggestions for improvements:
- Add timer/countdown functionality
- Implement world clock with multiple time zones
- Add weather forecast (5-day/hourly)
- Create alarm functionality
- Add theme customization options
- Implement data persistence (save laps, favorite cities, etc.)
- Add unit conversion tools
- Implement calendar view

## Future Enhancements

Potential features for future versions:
- Settings panel for customization
- Database integration for data persistence
- Multiple theme options
- System tray integration
- Keyboard shortcuts
- Export stopwatch lap times to CSV
- Weather alerts and notifications
- Historical weather data graphs

## Support

For issues, questions, or feature requests:
- Check the Troubleshooting section above
- Review PyQt5 documentation: https://www.riverbankcomputing.com/static/Docs/PyQt5/
- OpenWeatherMap API docs: https://openweathermap.org/api

## Acknowledgments

- **PyQt5**: For the powerful GUI framework
- **OpenWeatherMap**: For providing free weather API access
- **Font Creators**: For the custom fonts used in this project

---

**Note**: Remember to replace placeholder paths with your actual file paths before running the application. Keep your OpenWeatherMap API key secure and never share it publicly.
