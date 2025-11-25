# Working with Sets
from pyscript import display

weather_today = {
    "location" : "Manila",
    "temperature_c": 32,
    "humidity" : 78,
    "condition" : "sunny"
}

temp = weather_today["temperature_c"]
display(f'{weather_today}', target='cont')
display(f'Temperature (in °C): {temp}', target='cont')

weather_today["condition"] = "cloudy"
weather_today["heat_index"] = "38"
cond = weather_today["condition"]
index = weather_today["heat_index"]

display(f'{weather_today}', target='conta')
display(f'Condition: {cond}', target='conta')
display(f'Heat Index (in °C): {index}', target='conta')

display(f'* Heat index is a measure of how hot the weather feels to the human body when relative humidity is combined with the air temperature.', target = 'conta')