from flask import Flask, render_template, request

app = Flask(__name__)

restaurants = [
    {
        "id": 1,
        "name": "Burger king",
        "cuisine": "Cuisine 1",
        "menu": [
            {"id": 1, "name": "burger", "price": 9.9},
            {"id": 2, "name": "fries", "price": 5.0},
            {"id": 3, "name": "coke", "price": 4.0},
        ]
    },
    {
        "id": 2,
        "name": "china rose",
        "cuisine": "Cuisine 2",
        "menu": [
            {"id": 4, "name": "Kung Pao Chicken", "price": 12.0},
            {"id": 5, "name": "hot pot", "price": 13.0},
            {"id": 6, "name": "fried rice", "price": 12.0},
        ]
    },
    {
        "id": 3,
        "name": "k-pop",
        "cuisine": "Cuisine 3",
        "menu": [
            {"id": 7, "name": "Pickle", "price": 8.0},
            {"id": 8, "name": "barbecue", "price": 21.0},
            {"id": 9, "name": "fried chicken", "price": 16.0},
        ]
    },
]

@app.route("/")
def restaurant_list():
    return render_template("restaurant_list.html", restaurants=restaurants)

@app.route("/restaurant/<int:restaurant_id>/")
def restaurant_menu(restaurant_id):
    restaurant = [r for r in restaurants if r["id"] == restaurant_id][0]
    return render_template("restaurant_menu.html", restaurant=restaurant)

@app.route("/restaurant/<int:restaurant_id>/order", methods=["GET", "POST"])
def restaurant_order(restaurant_id):
    restaurant = [r for r in restaurants if r["id"] == restaurant_id][0]
    if request.method == "POST":
        order = request.form.getlist("dish")
        return render_template("restaurant_order.html", restaurant=restaurant, order=order)
    return render_template("restaurant_order.html", restaurant=restaurant)

if __name__ == "__main__":
    app.run(debug=True)