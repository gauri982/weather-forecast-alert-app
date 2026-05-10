import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from weather import get_coordinates, fetch_weather
from alerts import generate_alert

st.title("🌦️ Weather Forecast & Alert System")

city = st.text_input("Enter City Name")

if city:

    lat, lon = get_coordinates(city)
    data = fetch_weather(lat, lon)

    current = data["current_weather"]
    temp = current["temperature"]
    wind = current["windspeed"]

    st.subheader("🌍 Current Weather")
    st.write("Temperature:", temp, "°C")
    st.write("Wind Speed:", wind, "km/h")

    # Alerts
    alerts = generate_alert(temp, wind)

    st.subheader("⚠️ Alerts")
    if alerts:
        for a in alerts:
            st.warning(a)
    else:
        st.success("No alerts — Normal weather")

    # Forecast graph
    st.subheader("📊 Temperature Forecast (7 Days)")

    daily = data["daily"]

    df = pd.DataFrame({
        "Day": range(1, 8),
        "Max Temp": daily["temperature_2m_max"],
        "Min Temp": daily["temperature_2m_min"]
    })

    fig, ax = plt.subplots()
    ax.plot(df["Day"], df["Max Temp"], label="Max Temp")
    ax.plot(df["Day"], df["Min Temp"], label="Min Temp")
    ax.set_xlabel("Days")
    ax.set_ylabel("Temperature (°C)")
    ax.legend()

    st.pyplot(fig)