from werkzeug.exceptions import NotFound
from flask import Blueprint, render_template, abort

products_app = Blueprint('products_app', __name__)

PRODUCTS = {
    1: 'Phone',
    2: 'Tablet',
    3: 'Laptop',
}


@products_app.route('/', endpoint='products')
def products_list():
    return render_template(
        'products/index.html',
        products=PRODUCTS.items(),
    )


@products_app.route('/<int:id>/', endpoint='product')
def product_info(id):
    try:
        product_name = PRODUCTS[id]
    except KeyError:
        raise NotFound(f'There is no product #{id}')
        # abort(404)
    return f'Product #{id}: {product_name}'
