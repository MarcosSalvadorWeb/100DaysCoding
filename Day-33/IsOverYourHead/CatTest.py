import time
import schedule
import requests
from email.message import EmailMessage
import smtplib
from datetime import datetime, timezone

MY_EMAIL = "salvadormarcosjrjr@gmail.com"
PASSWORD = "llhu tdsl yqge chgc"

def send_good_morning():

    cat_url = "https://cataas.com/cat/says/Bom%20Dia"

    msg = EmailMessage()

    msg["Subject"] = "Bom Dia com Gatinhos 🐱"
    msg["From"] = MY_EMAIL
    msg["To"] = "destino@gmail.com"

    msg.set_content(
        f"""
Bom dia, Flor do Dia ☀️

Aqui está seu gatinho de Bom dia:

{cat_url}
"""
    )

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:

        connection.starttls()

        connection.login(
            MY_EMAIL,
            PASSWORD,
        )

        connection.send_message(msg)

    print("Email enviado com sucesso!")


schedule.every().day.at("06:00").do(send_good_morning)

while True:

    schedule.run_pending()

    time.sleep(1)