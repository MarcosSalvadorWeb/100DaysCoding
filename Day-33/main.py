import requests
from datetime import datetime

# API TEST ONE ---------------------------------------------------------------------------------------------
# response = requests.get("http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# latitude = response.json()["iss_position"]["latitude"]
# latitude = str(latitude)
# longitude = response.json()["iss_position"]["longitude"]
# longitude = str(longitude)

latitude = -23.540531
longitude = -46.838579
iss_position = {"lat": latitude, "lng": longitude, "formatted": 0}


# TIPOS DE RESPOSTA (STATUS-CODE) QUE VOCÊ PODE RECEBER DO SERVER API
# 1XX Hold on
# 2XX Here you go
# 3XX Go Away
# 4XX You screwed up
# 5XX I screwed up

str = "https://api.sunrise-sunset.org/json"
sun = requests.get(str,params=iss_position)

sunrise = sun.json()["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = sun.json()["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)
