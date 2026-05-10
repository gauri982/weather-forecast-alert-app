def generate_alert(temp, wind):

    alerts = []

    if temp > 40:
        alerts.append("🔥 Heat Wave Alert")
    if temp < 10:
        alerts.append("❄️ Cold Wave Alert")
    if wind > 50:
        alerts.append("🌪️ Storm Alert")

    return alerts