from flask import Flask
from ItemAPI import ItemAPI
from ProductAPI import ProductAPI
from urls import set_url

app = Flask(__name__)

set_url(app=app, cls=ItemAPI, view_name='items_api', url_path="items")
set_url(app=app, cls=ProductAPI, view_name='products_api', url_path="products")

if __name__ == '__main__':
    app.run(debug=True)
