from flask import Flask, jsonify, request,abort 
import entrada_controller_poo
from entrada_db import create_tables
from exchange_rate import get_xr
from entrada_db import get_db

app = Flask(__name__)


@app.route('/api/entradadavis/precios', methods=["GET"])
def get_entradas():
    entradas = entrada_controller_poo.get_entradas()
    entradas_list=[]
    for entrada in entradas:
        elem = entrada.serialize()
        entradas_list.append(elem)
    return jsonify(entradas_list)

@app.route("/api/entradadavis/precios", methods=["POST"])
def insert_entrada():
    entrada_details = request.get_json()
    id= entrada_details["id"]
    estadio = entrada_details["estadio"]
    partido =entrada_details["partido"]
    precio = entrada_details["precio"]
    sector = entrada_details["sector"]
    result = entrada_controller_poo.insert_entrada(id,estadio,partido,precio,sector)
    return jsonify(result)






@app.route("/api/entradadavis/comprar/<id>/cantidad/<cantidad>", methods=["GET"])
def get_entrada_by_id_psa(id, cantidad):
    try:
        entrada = entrada_controller_poo.get_by_id(id)

        if entrada is None:
            return "El ID es obligatorio.", 404

        xr = get_xr()
        cantidad = int(cantidad) 

        price_peso = entrada['precio'] * cantidad
        price_dolar = price_peso / xr
        price_descuento = price_peso * 0.85

        response_text = f"Precio en pesos: {price_peso}, Precio en dólares: {price_dolar}, Precio con descuento AAT: {price_descuento}"
        return response_text
    except Exception as e:
        return f"Error: El ID no existe o el parámetro es inválido.", 400

create_tables()

if __name__ == '__main__':
    app.run()
