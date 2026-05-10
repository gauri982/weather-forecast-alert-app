# 🌦️ Weather Forecast & Alert System (No API Key Required)

## 📌 Project Overview

This is a **Python-based Weather Forecast & Alert Application** that provides real-time weather updates, 7-day forecasts, and intelligent weather alerts using a free public API.

The project uses:
:contentReference[oaicite:0]{index=0}

It includes a **Streamlit dashboard**, data visualization, and an alert system for extreme weather conditions like heat waves, storms, and cold waves.

---

## 🎯 Problem Statement

Weather conditions affect daily life, agriculture, travel, logistics, and outdoor planning. Sudden changes in weather can lead to risks such as:

- Heat waves 🌡️  
- Heavy storms 🌪️  
- Cold waves ❄️  
- Strong winds 🌬️  

This project helps users get **real-time weather insights and alerts**.

---

## 💡 Features

- 🌍 Real-time weather data fetching  
- 📊 7-day weather forecast  
- ⚠️ Smart alert system (Heat, Storm, Cold)  
- 📈 Data visualization using graphs  
- 🖥️ Streamlit interactive dashboard  
- 🚫 No API key required  
- 🧠 Rule-based weather analysis  

---

## 🏗️ Project Architecture


User Input (City Name)
↓
Coordinate Mapping
↓
Open-Meteo API Call
↓
JSON Weather Data
↓
Data Processing & Analysis
↓
Alert Generation Engine
↓
Streamlit Dashboard Output
↓
Graphs + Weather Report Display


---

## 🛠️ Tech Stack

- Python 🐍  
- Streamlit  
- Requests  
- Pandas  
- Matplotlib  
- Open-Meteo API  

---

## 📁 Project Structure


Weather-Forecast-Alert-Application/
│
├── app.py # Streamlit dashboard
├── weather.py # API handling
├── alerts.py # Alert logic
├── requirements.txt # Dependencies
├── README.md # Documentation


---
![Working Demo](outputs/workingdemo.mp4)

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/weather-forecast-alert-app.git
cd weather-forecast-alert-app
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run Application
streamlit run app.py
🌐 How It Works
User enters city name
System converts city → coordinates
Weather data fetched from Open-Meteo API
JSON response processed
Temperature, wind, and forecast analyzed
Alerts generated using rule-based logic
Output displayed in Streamlit dashboard
⚠️ Alert Conditions
🔥 Temperature > 40°C → Heat Wave Alert
❄️ Temperature < 10°C → Cold Wave Alert
🌪️ Wind Speed > 50 km/h → Storm Alert
🎬 Working Demo

This video demonstrates the complete working of the project:

📽️ Demo Video

If video does not play on GitHub, open file manually:

📁 outputs/workingdemo.mp4


Streamlit dashboard
Weather graph
Alert messages
Terminal output
📚 Learning Outcomes
API integration in Python
Real-time data handling
Streamlit dashboard creation
Data visualization
Modular coding structure
Weather alert system design
🚀 Future Enhancements
🌍 Map-based weather tracking
📧 Email/SMS alerts
🤖 AI-based prediction system
☁️ Cloud deployment (Render/Vercel)
📱 Mobile app version
👨‍💻 Author

gauri k Project – Python Developer Portfolio
