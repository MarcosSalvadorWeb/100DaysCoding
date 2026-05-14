import requests
from email.message import EmailMessage
import smtplib

MY_EMAIL = "salvadormarcosjrjr@gmail.com"
PASSWORD = "llhu tdsl yqge chgc"

import requests
import smtplib

from email.message import EmailMessage


def send_good_morning():

    response = requests.get(
        "https://dog.ceo/api/breeds/image/random"
    )

    dog_url = response.json()["message"]

    msg = EmailMessage()

    msg["Subject"] = "Bom Dia com Cachorrinhos"
    msg["From"] = MY_EMAIL
    msg["To"] = "brenda.nunes0212@gmail.com"

    msg.set_content(
        f"""
Bom dia, Flor do Dia ☀️

Aqui está seu cachorrinho de Bom Dia:

{dog_url}

Amo Você!
Junior.
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


send_good_morning()