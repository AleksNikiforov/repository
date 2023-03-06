from flask import Blueprint, render_template, request, redirect, url_for, flash
from dataclasses import dataclass
from werkzeug.exceptions import BadRequest, NotFound
from models import db, Product


products_app = Blueprint(
    "products_app",
    __name__,
    url_prefix="/products",
)


@products_app.get("/", endpoint = 'list')
def get_products_list():
    products = Product.query.all()
    return render_template("products/list.html", products=products)


def get_product_or_raise(product_id: int) -> Product:
    product = Product.query.get(product_id)
    if product:
        return product
    raise NotFound(f"Product #{product_id} not found!")


@products_app.get("/<int:product_id>/", endpoint="details")
def get_product_details(product_id: int):
    # try:
    #     product = storage.products[product_id]
    # except KeyError:
    #     ...
    product = get_product_or_raise(product_id)
    return render_template("products/details.html", product=product)


@products_app.route("/create/", methods=["GET", "POST"], endpoint="create")
def create_product():
    if request.method == "GET":
        return render_template("products/create.html")

    product_name = request.form.get("product-name", "")
    product_name = product_name.strip()
    if not product_name:
        raise BadRequest("Field product-name is required!")

    product = Product(name=product_name)
    db.session.add(product)
    db.session.commit()
    flash(f"Product {product_name} was created")
    url = url_for("products_app.details", product_id=product.id)
    return redirect(url)


@products_app.route("/<int:product_id>/delete/", methods=["GET", "POST"], endpoint="delete")
def delete_product(product_id: int):
    product = get_product_or_raise(product_id)

    if request.method == "GET":
        return render_template("products/delete.html", product=product)

    product_name = product.name
    db.session.delete(product)
    db.session.commit()

    flash(f"Deleted product {product_name}!", category="warning")
    url = url_for("products_app.list")
    return redirect(url)