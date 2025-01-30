# Weather Forecast Application  

## Overview  
The **Weather Forecast Application** is a command-line tool that fetches real-time weather data using the **OpenWeatherMap API**. Users can enter a **city name or zip code** to retrieve current weather conditions and an extended forecast.  

## Features  
✅ **Input Validation** – Ensures valid city names or zip codes.  
✅ **Current Weather Display** – Shows temperature, humidity, wind speed, and weather conditions.  
✅ **Extended Forecast** – Provides upcoming weather details.  
✅ **Error Handling** – Manages API errors, invalid inputs, and connectivity issues.  

## Technologies Used  
- **Python** – Core programming language  
- **requests** – API interaction  
- **JSON Parsing** – Data processing  

## Installation  
1. **Clone the Repository**  
   ```sh
   git clone https://github.com/yourusername/weather-forecast-app.git  
   cd weather-forecast-app  
   ```
2. **Install Dependencies**  
   ```sh
   pip install requests  
   ```
3. **Set Up API Key**  
   - Get an API key from [OpenWeatherMap](https://openweathermap.org/)  
   - Replace `API_KEY` in `c0930172_Project.py` with your key.  

## Usage  
Run the application using:  
```sh
python c0930172_Project.py  
```  
Enter a city name or zip code when prompted.  

## Example Output  
```
Enter city name or zip code: Toronto
Current Weather:
Temperature: 293K
Humidity: 60%
Weather: Clear Sky
Wind Speed: 5 m/s

Extended Forecast:
2024-07-19 12:00 - Cloudy, Temp: 295K, Humidity: 58%
...
```  

## Future Enhancements  
🔹 Add graphical user interface (GUI)  
🔹 Support multiple weather sources  
🔹 Implement weather alerts  

## License  
This project is intended for academic and learning purposes. All rights reserved.
---
