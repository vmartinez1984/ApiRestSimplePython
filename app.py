from crypt import methods

from requests import request
from products import products
from flask import Flask, jsonify, make_response, request

app = Flask(__name__)


@app.route('/ping')
def ping():
    return jsonify({'message': 'Pong'})


@app.route('/Api/Products', methods=['GET'])
def getProducts():
    return jsonify(products)

@app.route('/Api/Products/<product_name>')
def getProduct(product_name):
    productSelected = [product for product in products if product['name'] == product_name]
    if( len(productSelected) > 0):
        return productSelected[0]
    else:
        return make_response (jsonify({"message": "not found"}), 404)

@app.route('/Api/Products/', methods=['POST'])
def post():
    newProduct = {
        "name": request.json["name"],
        "price": request.json["price"],
        "quantity": request.json["quantity"]
    }
    products.append(newProduct)
    response = make_response(jsonify({"id": newProduct["name"]}), 201)
    response.headers["route"] = "/Api/Products/1" + newProduct["name"]

    return response

if __name__ == '__main__':
    app.run(debug=True, port=1984)
