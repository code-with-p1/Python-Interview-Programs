from flask import request, jsonify
from flask.views import MethodView

class ProductAPI(MethodView):
    def get(self, id):
        # Example GET request handler
        if id is None:
            # Return a list of products
            return jsonify(products=["product1", "product2", "product3"])
        else:
            # Return a specific product
            return jsonify(product={"id": id, "name": f"product {id}"})

    def post(self):
        # Example POST request handler
        data = request.get_json()
        return jsonify(message="product created", product=data), 201

    def put(self, id):
        # Example PUT request handler
        data = request.get_json()
        return jsonify(message="product updated", product={"id": id, "data": data})

    def delete(self, id):
        # Example DELETE request handler
        return jsonify(message="product deleted", id=id)