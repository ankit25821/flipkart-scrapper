import datetime

from flask import (
    Flask, redirect, render_template, request, url_for, send_file
)

from scrapper import (
    get_default_products, search_products,
    dataframe_to_object
)

from product import DefaultProduct, Product


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    default_data = []

    df = get_default_products()

    for _, row in df.iterrows():
        default_data.append(dataframe_to_object(DefaultProduct, row))

    return render_template("index.html", default_data=default_data)


@app.route("/search/", methods=["GET"])
def search():

    if not request.args.get("q"):
        return redirect(url_for('index'))

    query = request.args['q']

    searched_products = []

    df = search_products(query)

    for _, row in df.iterrows():
        searched_products.append(dataframe_to_object(Product, row))

    return render_template("search.html", products=searched_products)



if __name__ == "__main__":
    app.run(debug=True)
