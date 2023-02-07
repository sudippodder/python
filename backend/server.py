from flask import Flask, request, jsonify
from flask_cors import CORS
from sql_connection import get_sql_connection
import mysql.connector
import json




import product_dao
import order_dao
import unit_dao

app = Flask(__name__)
CORS(app)
connection = get_sql_connection()

@app.route('/getUnit', methods=['GET'])
def get_units():
    response = unit_dao.get_unit(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/getProducts", methods=['GET'])
def get_products():
    product = product_dao.get_all_product(connection)
    response = jsonify(product)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    product_id = product_dao.insert_new_product(connection, request_payload)
    response = jsonify({
        'product_id': product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    response = order_dao.get_all_orders(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertOrder', methods=['POST'])
def insert_order():
    
    request_payload = json.loads(request.form['data'])
    order_id = order_dao.insert_order(connection, request_payload)
    response = jsonify({
        'order_id': order_id
    })
    #print(response)
    #return response
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    return_id = product_dao.delete_product(connection, request.form['product_id'])
    response = jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__=="__main__":
    print("starting python flask")
    app.run(port=5000)