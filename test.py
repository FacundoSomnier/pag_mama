from flask import Flask, render_template, request, url_for
from sender import sender

app = Flask(__name__)


def activar_menu(tipo):
    global clase_1, clase_2, clase_3, clase_4, clase_5
    if tipo == "ventas":
        clase_1 = None
        clase_2 = 'active'
        clase_3 = None
        clase_4 = None
        clase_5 = None
    elif tipo == "alquileres":
        clase_1 = None
        clase_2 = None
        clase_3 = 'active'
        clase_4 = None
        clase_5 = None
    elif tipo == "zonas":
        clase_1 = None
        clase_2 = None
        clase_3 = None
        clase_4 = 'active'
        clase_5 = None
    elif tipo == "contacto":
        clase_1 = None
        clase_2 = None
        clase_3 = None
        clase_4 = None
        clase_5 = 'active'


@app.route("/")
def home():
    return render_template("index.html", clase1='active')


@app.route("/<tipo>")
def tipo(tipo):
    activar_menu(tipo)
    return render_template("plantillaV_A.html", tipo=tipo, clase1=clase_1, clase2=clase_2, clase3=clase_3, clase4=clase_4, clase5=clase_5)


@app.route("/<tipo>/<clase>")
def plantilla(tipo, clase):
    activar_menu(tipo)
    return render_template("plantillaProp.html", tipo=tipo, clase1=clase_1, clase2=clase_2, clase3=clase_3, clase4=clase_4, clase5=clase_5)


@app.route("/contacto", methods=["POST", "GET"])
def contacto():
    activar_menu("contacto")
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("comment")
        phone = request.form.get("phone")
        print(name, email, message, phone)
        sender.send(name=name, mail=email, body=message, phone=phone)

    return render_template("contact.html", tipo=tipo, clase1=clase_1, clase2=clase_2, clase3=clase_3, clase4=clase_4, clase5=clase_5)


@app.route("/zonas")
def zonas():
    activar_menu("zonas")
    return render_template("plantillaZonas.html", tipo=tipo, clase1=clase_1, clase2=clase_2, clase3=clase_3, clase4=clase_4, clase5=clase_5)


if __name__ == "__main__":
    app.run(debug=True)
