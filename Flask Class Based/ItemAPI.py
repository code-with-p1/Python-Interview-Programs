from flask import request, jsonify
from flask.views import MethodView

class JsonResponseMixin:
    def json_response(self, data, status=200):
        return jsonify(data), status

class ItemAPI(MethodView, JsonResponseMixin):
    def get(self, id):
        # Example GET request handler
        if id is None:
            # Return a list of items
            return self.json_response(items=["item1", "item2", "item3"])
        else:
            # Return a specific item
            return self.json_response(item={"id": id, "name": f"Item {id}"})

    def post(self):
        # Example POST request handler
        data = request.get_json()
        return self.json_response(message="Item created", item=data), 201

    def put(self, id):
        # Example PUT request handler
        data = request.get_json()
        return self.json_response(message="Item updated", item={"id": id, "data": data})

    def delete(self, id):
        # Example DELETE request handler
        return self.json_response(message="Item deleted", id=id)