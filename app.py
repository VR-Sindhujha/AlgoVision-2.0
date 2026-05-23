from flask_jwt_extended import (

    JWTManager,

    create_access_token,

    jwt_required,

    get_jwt_identity
)
from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO, emit
import sqlite3
import mysql.connector
from datetime import datetime

app = Flask(__name__)

app.secret_key = "algo_secret_key"


# JWT CONFIG

app.config["JWT_SECRET_KEY"] = "algo_super_secret"

jwt = JWTManager(app)


# SOCKET CONFIG

socketio = SocketIO(app)

# =========================
# MYSQL CONNECTION
# =========================
print("MYSQL CHECK STARTED")
try:

    mysql_connection = mysql.connector.connect(

        host="localhost",

        user="root",

        password="",

        database="algo_production"
    )

    print(

        "MySQL Connected Successfully 🚀"
    )

except Exception as e:

    print(

        "MySQL Connection Failed ❌"
    )

    print(e)
from queue_engine import QueueEngine
from heap_engine import HeapEngine
from hashmap_engine import HashMapEngine
from bst_engine import BSTEngine
from graph_engine import GraphEngine
from dijkstra_engine import DijkstraEngine
from dp_engine import DynamicProgrammingEngine



# =========================
# ENGINES
# =========================

queue_engine = QueueEngine()

heap_engine = HeapEngine()

hashmap_engine = HashMapEngine()

bst_engine = BSTEngine()

graph_engine = GraphEngine()

dijkstra_engine = DijkstraEngine()

dp_engine = DynamicProgrammingEngine()


# =========================
# PRODUCTS DATABASE
# =========================

products = {

    "medicine": {

        "name": "Medicine Kit",

        "image": "medicine.jpg",

        "description":

        "Emergency medical delivery package.",

        "delivery": "Emergency Delivery",

        "priority": 100,

        "resource_cost": 5,

        "price": "1,499"
    },

    "watch": {

        "name": "Luxury Watch",

        "image": "watch.jpg",

        "description":

        "Premium luxury watch for VIP customers.",

        "delivery": "VIP Delivery",

        "priority": 90,

        "resource_cost": 4,

        "price": "24,999"
    },

    "grocery": {

        "name": "Grocery Pack",

        "image": "grocery.jpg",

        "description":

        "Daily household grocery essentials.",

        "delivery": "Normal Delivery",

        "priority": 50,

        "resource_cost": 2,

        "price": "2,999"
    },

    "electronics": {

        "name": "Electronics Kit",

        "image": "electronics.jpg",

        "description":

        "Fragile electronic delivery package.",

        "delivery": "Fragile Delivery",

        "priority": 70,

        "resource_cost": 3,

        "price": "15,999"
    },

    "food": {

        "name": "Food Package",

        "image": "food.jpg",

        "description":

        "Fast food delivery service package.",

        "delivery": "Fast Delivery",

        "priority": 80,

        "resource_cost": 4,

        "price": "799"
    }
}


# =========================
# BST INSERTION
# =========================

for key, product in products.items():

    bst_engine.insert(

        key,

        product
    )


# =========================
# GRAPH NETWORK
# =========================

graph_engine.add_edge(

    "Chennai Hub",

    "Traffic Center",

    10
)

graph_engine.add_edge(

    "Traffic Center",

    "Anna Nagar",

    5
)

graph_engine.add_edge(

    "Chennai Hub",

    "Velachery",

    20
)

graph_engine.add_edge(

    "Velachery",

    "Anna Nagar",

    15
)

graph_engine.add_edge(

    "Traffic Center",

    "T Nagar",

    7
)


# =========================
# DATABASE
# =========================

def create_database():

    connection = sqlite3.connect("algo.db")

    cursor = connection.cursor()

    # ORDERS TABLE

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS orders (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            customer_name TEXT,

            product_name TEXT,

            destination TEXT,

            priority TEXT,

            delivery_speed TEXT

        )

    """)


    # USERS TABLE

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS users (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT,

            email TEXT UNIQUE,

            password TEXT

        )

    """)

    connection.commit()

    connection.close()


create_database()
# =========================
# SOCKET EVENTS
# =========================

@socketio.on("connect")
def handle_connect():

    print("Client Connected")


@socketio.on("delivery_update")
def handle_delivery(data):

    emit(

        "live_update",

        {

            "message":

            f"🚚 Delivery Update: {data}"
        },

        broadcast=True
    )

# =========================
# REALTIME SOCKET PAGE
# =========================

@app.route("/realtime")
def realtime():

    if "user" not in session:

        return redirect("/login")

    return render_template(

        "realtime.html"
    )


# =========================
# JWT LOGIN
# =========================

@app.route("/jwt-login", methods=["GET", "POST"])
def jwt_login():

    token = None

    if request.method == "POST":

        username = request.form["username"]

        password = request.form["password"]


        # SIMPLE AUTH

        if username and password:

            token = create_access_token(

                identity=username
            )


    return render_template(

        "jwt_login.html",

        token=token
    )


# =========================
# SIGNUP
# =========================

@app.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":

        username = request.form["username"]

        email = request.form["email"]

        password = request.form["password"]

        connection = sqlite3.connect("algo.db")

        cursor = connection.cursor()

        cursor.execute("""

            INSERT INTO users (

                username,

                email,

                password

            )

            VALUES (?, ?, ?)

        """, (

            username,

            email,

            password

        ))

        connection.commit()

        connection.close()

        return redirect("/login")

    return render_template(

        "signup.html"
    )


# =========================
# LOGIN
# =========================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]

        password = request.form["password"]

        connection = sqlite3.connect("algo.db")

        cursor = connection.cursor()

        cursor.execute("""

            SELECT * FROM users

            WHERE email=? AND password=?

        """, (

            email,

            password

        ))

        user = cursor.fetchone()

        connection.close()

        if user:

            session["user"] = user[1]

            return redirect("/home")

    return render_template(

        "login.html"
    )


# =========================
# LOGOUT
# =========================

@app.route("/logout")
def logout():

    session.pop("user", None)

    return redirect("/login")


# =========================
# SPLASH SCREEN
# =========================

@app.route("/")
def splash():

    return render_template(

        "splash.html"
    )


# =========================
# HOME PAGE
# =========================

@app.route("/home")
def home():

    if "user" not in session:

        return redirect("/login")

    return render_template(

        "home.html"
    )


# =========================
# PRODUCT PAGE
# =========================

@app.route("/product/<product_name>")
def product(product_name):

    if "user" not in session:

        return redirect("/login")

    selected_product = products.get(product_name)

    if selected_product is None:

        return "Product Not Found"

    return render_template(

        "product.html",

        product_name=selected_product["name"],

        image=selected_product["image"],

        description=selected_product["description"],

        delivery=selected_product["delivery"],

        price=selected_product["price"],

        route_name=product_name
    )


# =========================
# ORDER PAGE
# =========================

@app.route(

    "/order/<product_name>",

    methods=["GET", "POST"]
)

def order(product_name):

    if "user" not in session:

        return redirect("/login")

    selected_product = products.get(product_name)

    if selected_product is None:

        return "Product Not Found"

    if request.method == "POST":

        customer_name = request.form["customer_name"]

        destination = request.form["destination"]

        priority = request.form["priority"]

        delivery_speed = request.form["delivery_speed"]

        timestamp = datetime.now().strftime(

            "%H:%M:%S"
        )

        # DATABASE INSERT

        connection = sqlite3.connect(

            "algo.db"
        )

        cursor = connection.cursor()

        cursor.execute("""

            INSERT INTO orders (

                customer_name,

                product_name,

                destination,

                priority,

                delivery_speed

            )

            VALUES (?, ?, ?, ?, ?)

        """, (

            customer_name,

            selected_product["name"],

            destination,

            priority,

            delivery_speed

        ))

        order_id = cursor.lastrowid

        connection.commit()

        connection.close()


        # QUEUE

        queue_engine.enqueue(

            selected_product["name"],

            timestamp
        )


        # HEAP

        heap_engine.add_order(

            selected_product["priority"],

            timestamp,

            selected_product["name"]
        )


        # HASHMAP

        hashmap_engine.add_order(

            order_id,

            {

                "customer": customer_name,

                "product": selected_product["name"],

                "destination": destination,

                "priority": priority,

                "timestamp": timestamp
            }
        )

        return redirect(

            url_for("tracking")
        )

    return render_template(

        "order.html",

        product=selected_product
    )


# =========================
# PROCESSING PAGE
# =========================

@app.route("/processing")
def processing():

    return render_template(

        "processing.html"
    )

# =========================
# ADD TO CART
# =========================

@app.route("/add-to-cart/<product_name>")
def add_to_cart(product_name):

    if "user" not in session:

        return redirect("/login")

    selected_product = products.get(product_name)

    if selected_product is None:

        return "Product Not Found"

    cart = session.get("cart", [])

    cart.append({

        "id": len(cart),

        "name": selected_product["name"],

        "price": selected_product["price"],

        "image": selected_product["image"]
    })

    session["cart"] = cart

    return redirect("/cart")


# =========================
# CART PAGE
# =========================

@app.route("/cart")
def cart():

    if "user" not in session:

        return redirect("/login")

    cart_items = session.get("cart", [])

    total = 0

    for item in cart_items:

        price = item["price"]

        price = str(price).replace(",", "")

        total += int(price)

    return render_template(

        "cart.html",

        cart_items=cart_items,

        total=total
    )


# =========================
# REMOVE FROM CART
# =========================

@app.route("/remove-from-cart/<int:item_id>")
def remove_from_cart(item_id):

    cart = session.get("cart", [])

    updated_cart = []

    for item in cart:

        if item["id"] != item_id:

            updated_cart.append(item)

    session["cart"] = updated_cart

    return redirect("/cart")

# =========================
# ADD TO WISHLIST
# =========================

@app.route("/add-to-wishlist/<product_name>")
def add_to_wishlist(product_name):

    if "user" not in session:

        return redirect("/login")

    selected_product = products.get(product_name)

    if selected_product is None:

        return "Product Not Found"

    wishlist = session.get("wishlist", [])

    wishlist.append({

        "id": len(wishlist),

        "name": selected_product["name"],

        "price": selected_product["price"],

        "image": selected_product["image"]
    })

    session["wishlist"] = wishlist

    return redirect("/wishlist")


# =========================
# WISHLIST PAGE
# =========================

@app.route("/wishlist")
def wishlist():

    if "user" not in session:

        return redirect("/login")

    wishlist_items = session.get("wishlist", [])

    return render_template(

        "wishlist.html",

        wishlist_items=wishlist_items
    )


# =========================
# REMOVE WISHLIST
# =========================

@app.route("/remove-from-wishlist/<int:item_id>")
def remove_from_wishlist(item_id):

    wishlist = session.get("wishlist", [])

    updated_wishlist = []

    for item in wishlist:

        if item["id"] != item_id:

            updated_wishlist.append(item)

    session["wishlist"] = updated_wishlist

    return redirect("/wishlist")

# =========================
# GOOGLE MAPS
# =========================

@app.route("/maps")
def maps():

    if "user" not in session:

        return redirect("/login")

    return render_template(

        "maps.html"
    )


# =========================
# ADMIN PANEL
# =========================

@app.route("/admin")
def admin():

    if "user" not in session:

        return redirect("/login")


    admin_data = {

        "users": 12450,

        "orders": 48920,

        "revenue": "92.5L",

        "deliveries": 540,

        "fraud": 18,

        "stock": "Stable ✅"
    }


    return render_template(

        "admin.html",

        data=admin_data
    )


# =========================
# FRAUD DETECTION
# =========================

@app.route("/fraud-detection", methods=["GET", "POST"])
def fraud_detection():

    if "user" not in session:

        return redirect("/login")

    result = None

    score = 0


    if request.method == "POST":

        amount = int(

            request.form["amount"]
        )

        location = request.form["location"]

        payment = request.form["payment"]


        # AI FRAUD LOGIC

        score = 10


        # HIGH AMOUNT

        if amount > 50000:

            score += 40


        # HIGH RISK LOCATION

        if location == "High Risk Zone":

            score += 30


        # CRYPTO PAYMENT

        if payment == "Crypto":

            score += 25


        # RESULT

        if score >= 70:

            result = "🚨 High Fraud Risk Detected"

        elif score >= 40:

            result = "⚠️ Medium Fraud Risk"

        else:

            result = "✅ Safe Transaction"


    return render_template(

        "fraud_detection.html",

        result=result,

        score=score
    )


# =========================
# ROUTE OPTIMIZER
# =========================

@app.route("/route-optimizer", methods=["GET", "POST"])
def route_optimizer():

    if "user" not in session:

        return redirect("/login")

    best_route = None

    cost = None


    if request.method == "POST":

        source = request.form["source"]

        destination = request.form["destination"]


        # DIJKSTRA-STYLE LOGIC

        graph = {

            ("Warehouse", "Customer Zone"):
            ("Warehouse → Hub A → Customer Zone", 120),

            ("Warehouse", "City Center"):
            ("Warehouse → Hub B → City Center", 90),

            ("Warehouse", "Rural Area"):
            ("Warehouse → Hub A → Hub B → Rural Area", 180),

            ("Hub A", "Customer Zone"):
            ("Hub A → Customer Zone", 60),

            ("Hub B", "City Center"):
            ("Hub B → City Center", 45),

            ("Hub B", "Rural Area"):
            ("Hub B → Rural Area", 100)
        }


        result = graph.get(

            (source, destination),

            ("No Route Found", 0)
        )


        best_route = result[0]

        cost = result[1]


    return render_template(

        "route_optimizer.html",

        best_route=best_route,

        cost=cost
    )


# =========================
# AI DELIVERY PREDICTION
# =========================

@app.route("/prediction", methods=["GET", "POST"])
def prediction():

    if "user" not in session:

        return redirect("/login")

    eta = None

    if request.method == "POST":

        distance = int(

            request.form["distance"]
        )

        traffic = request.form["traffic"]

        priority = request.form["priority"]


        # AI ETA LOGIC

        eta_value = distance * 2


        # TRAFFIC EFFECT

        if traffic == "Medium":

            eta_value += 10

        elif traffic == "High":

            eta_value += 20


        # PRIORITY EFFECT

        if priority == "Express":

            eta_value -= 5

        elif priority == "VIP":

            eta_value -= 10


        # FINAL ETA

        eta = f"{eta_value} Minutes"


    return render_template(

        "prediction.html",

        eta=eta
    )


# =========================
# INVENTORY MANAGEMENT
# =========================

@app.route("/inventory")
def inventory():

    if "user" not in session:

        return redirect("/login")


    inventory_items = [

        {
            "name": "Medicine Kit",
            "stock": 45,
            "image": "medicine.jpg"
        },

        {
            "name": "Luxury Watch",
            "stock": 12,
            "image": "watch.jpg"
        },

        {
            "name": "Electronics Kit",
            "stock": 4,
            "image": "electronics.jpg"
        },

        {
            "name": "Food Package",
            "stock": 32,
            "image": "food.jpg"
        }

    ]


    return render_template(

        "inventory.html",

        inventory=inventory_items
    )


# =========================
# AI CHATBOT
# =========================

@app.route("/chatbot")
def chatbot():

    if "user" not in session:

        return redirect("/login")

    return render_template(

        "chatbot.html"
    )


# =========================
# LIVE TRACKING
# =========================

@app.route("/live-tracking")
def live_tracking():

    if "user" not in session:

        return redirect("/login")

    return render_template(

        "live_tracking.html"
    )


# =========================
# ANALYTICS DASHBOARD
# =========================

@app.route("/analytics")
def analytics():

    if "user" not in session:

        return redirect("/login")


    analytics_data = {

        "orders": 12480,

        "revenue": "24.8L",

        "deliveries": 320,

        "success": "98%"
    }


    return render_template(

        "analytics.html",

        data=analytics_data
    )
# =========================
# AI RECOMMENDATIONS
# =========================

@app.route("/recommendations")
def recommendations():

    if "user" not in session:

        return redirect("/login")


    # SIMPLE AI RECOMMENDATION LOGIC

    recommendations = [

        {
            "name": "Medicine Kit",
            "price": "999",
            "image": "medicine.jpg",
            "delivery": "Emergency Delivery",
            "route": "medicine"
        },

        {
            "name": "Luxury Watch",
            "price": "4999",
            "image": "watch.jpg",
            "delivery": "VIP Delivery",
            "route": "watch"
        },

        {
            "name": "Electronics Kit",
            "price": "2999",
            "image": "electronics.jpg",
            "delivery": "Fragile Delivery",
            "route": "electronics"
        }

    ]


    return render_template(

        "recommendations.html",

        recommendations=recommendations
    )
# =========================
# PROFILE PAGE
# =========================

@app.route("/profile")
def profile():

    if "user" not in session:

        return redirect("/login")

    username = session["user"]

    connection = sqlite3.connect(

        "algo.db"
    )

    cursor = connection.cursor()

    cursor.execute(

        "SELECT * FROM orders"
    )

    orders = cursor.fetchall()

    connection.close()


    # CART COUNT

    cart_items = session.get(

        "cart",

        []
    )

    cart_count = len(cart_items)


    # WISHLIST COUNT

    wishlist_items = session.get(

        "wishlist",

        []
    )

    wishlist_count = len(wishlist_items)


    # TOTAL ORDERS

    total_orders = len(orders)


    return render_template(

        "profile.html",

        username=username,

        orders=orders,

        total_orders=total_orders,

        cart_count=cart_count,

        wishlist_count=wishlist_count
    )

# =========================
# PAYMENT PAGE
# =========================

@app.route("/payment", methods=["GET", "POST"])
def payment():

    if "user" not in session:

        return redirect("/login")

    if request.method == "POST":

        return redirect("/success")

    return render_template(

        "payment.html"
    )


# =========================
# SUCCESS PAGE
# =========================

@app.route("/success")
def success():

    if "user" not in session:

        return redirect("/login")

    return render_template(

        "success.html"
    )


# =========================
# TRACKING PAGE
# =========================

@app.route("/tracking")
def tracking():

    if "user" not in session:

        return redirect("/login")

    return render_template(

        "tracking.html"
    )


# =========================
# DASHBOARD
# =========================

@app.route(

    "/dashboard",

    methods=["GET", "POST"]
)

def dashboard():

    if "user" not in session:

        return redirect("/login")

    connection = sqlite3.connect(

        "algo.db"
    )

    cursor = connection.cursor()

    cursor.execute(

        "SELECT * FROM orders"
    )

    orders = cursor.fetchall()

    connection.close()


    # QUEUE

    queue_events = queue_engine.get_queue()


    # HEAP

    heap_data = heap_engine.get_all_orders()

    heap_priorities = []

    for item in heap_data:

        priority = -item[0]

        timestamp = item[1]

        product = item[2]

        heap_priorities.append(

            f"Priority {priority} → {product} ({timestamp})"
        )


    # ACTIVE DISPATCH

    active_dispatch = heap_engine.get_highest_priority()


    # HASHMAP SEARCH

    searched_order = None

    if request.method == "POST":

        order_id = int(

            request.form["order_id"]
        )

        searched_order = hashmap_engine.get_order(

            order_id
        )


    # BST

    bst_products = bst_engine.inorder_traversal()


    # GRAPH

    graph_data = graph_engine.get_graph()


    # DIJKSTRA

    shortest_path, shortest_distance = (

        dijkstra_engine.shortest_path(

            graph_engine.get_graph(),

            "Chennai Hub",

            "Anna Nagar"
        )
    )


    # WAREHOUSE

    selected_warehouse = "Chennai Hub"


    # DYNAMIC PROGRAMMING

    values = [100, 90, 50, 70, 80]

    weights = [5, 4, 2, 3, 4]

    capacity = 10

    resource_value = dp_engine.knapsack(

        values,

        weights,

        capacity
    )


    return render_template(

        "dashboard.html",

        orders=orders,

        queue_events=queue_events,

        heap_priorities=heap_priorities,

        active_dispatch=active_dispatch,

        searched_order=searched_order,

        bst_products=bst_products,

        graph_data=graph_data,

        best_route=shortest_path,

        shortest_distance=shortest_distance,

        selected_warehouse=selected_warehouse,

        resource_value=resource_value
    )


# =========================
# RUN APP
# =========================

if __name__ == "__main__":

    socketio.run(app, debug=True)