from manufactory import app, connection
from flask import render_template, request
from manufactory.queries import *
import psycopg2.extras


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/fruit")
def fruit():
    with connection:
        with connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute(SELECT_FRUIT)
            fruit = cursor.fetchall()
    return render_template('fruit.html', food_kind=fruit)


@app.route("/vegetables")
def vegetables():
    with connection:
        with connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute(SELECT_VEGETABLES)
            vegetables = cursor.fetchall()
    return render_template('vegetables.html', food_kind=vegetables)


@app.route("/inspirations")
def inspirations():
    return render_template('inspirations.html')


@app.post("/add_product")
def add_product():
    data = request.get_json()
    name = data["name"]
    kcal = data["kcal"]
    ml = data["ml"]
    description = data["description"]
    image = data["image"]
    is_fruit = data["is_fruit"]
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_TABLE)
            cursor.execute(INSERT_PRODUCT, (name, kcal, ml, description, image, is_fruit))

    return {"message": f"Product was added"}, 201
