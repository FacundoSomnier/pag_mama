import smtplib
import os

my_gmail = os.environ.get("GMAIL")
password_g = os.environ.get("GMAILPASS")

class sender:
    def send(name, mail, body, phone):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_gmail, password=password_g)
            connection.sendmail(
                from_addr=my_gmail,
                to_addrs=os.environ.get("TOMAIL"),
                msg=f"Subject:Consulta Inmobiliaria\n\nNombre: {name}\nEmail: {mail}\nTelefono: {phone}\nMensaje: \n{body}"
            )