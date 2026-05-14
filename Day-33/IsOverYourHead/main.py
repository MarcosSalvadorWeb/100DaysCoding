import requests
from datetime import datetime, timezone
import smtplib
import time
from email.message import EmailMessage

MY_LAT = -23.540531  # Your latitude
MY_LONG = -46.838579  # Your longitude

def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now(timezone.utc)
    if(time_now.hour >= sunset or time_now.hour <= sunrise):
        return True

def is_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

while True:
    time.sleep(60)
    if True:

        MY_EMAIL = "salvadormarcosjrjr@gmail.com"
        PASSWORD = "llhu tdsl yqge chgc"

        msg = EmailMessage()

        msg["Subject"] = "Olhe para o céu"
        msg["From"] = MY_EMAIL
        msg["To"] = "salvadormarcosjr@usp.br"

        msg.set_content(
            "A Estação Espacial Internacional (ISS) está acima da sua cabeça!"
        )

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:

            connection.starttls()

            connection.login(
                user=MY_EMAIL,
                password=PASSWORD
            )

            connection.send_message(msg)

        print("Email enviado!")


