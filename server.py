from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/home/<tipo>.html")
def tipo(tipo):
    if tipo == "ventas":
        clase_1 = 'active'
        clase_2 = None
    else:
        clase_1 = None
        clase_2 = 'active'
    return render_template("/paginas finales/plantillaVA.html", tipo=tipo, clase1= clase_1, clase2 = clase_2)

@app.route("/home/<tipo>/<clase>.html")
def plantilla(tipo, clase):
    if tipo == "ventas":
        clase_1 = 'active'
        clase_2 = None
    else:
        clase_1 = None
        clase_2 = 'active'
    return render_template("paginas finales/PlantillaProp.html", tipo=tipo, clase1= clase_1, clase2 = clase_2, clase=clase)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
