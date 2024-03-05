from flask import Flask, render_template, request, url_for, redirect
import smtplib
import os

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
