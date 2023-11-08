import smtplib
import os

my_gmail = os.getenv("GMAIL")
password_g = os.getenv("GMAILPASS")

class sender:
    def send(name, mail, body, phone):
        print(os.getenv("GMAIL"), os.getenv("GMAILPASS"), os.getenv("TOMAIL"))
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_gmail, password=password_g)
            connection.sendmail(
                from_addr=my_gmail,
                to_addrs= os.getenv("TOMAIL"),
                msg=f"Subject:Consulta Inmobiliaria\n\nNombre: {name}\nEmail: {mail}\nTelefono: {phone}\nMensaje: \n{body}"
            )
