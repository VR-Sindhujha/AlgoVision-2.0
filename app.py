from werkzeug.security import (

    generate_password_hash,

    check_password_hash
)
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
from datetime import datetime, timedelta
import threading
import time

app = Flask(__name__)
app.secret_key = "algo_super_secure_key"
app.permanent_session_lifetime = timedelta(minutes=30)

# JWT CONFIG

app.config["JWT_SECRET_KEY"] = "algo_super_secret"

jwt = JWTManager(app)


# SOCKET CONFIG

socketio = SocketIO(app)
# =========================
# MY ORDERS
# =========================

@app.route("/my-orders")
def my_orders():

    if "user" not in session:

        return redirect("/login")

    connection = sqlite3.connect("algo.db")

    cursor = connection.cursor()

    cursor.execute("""

        SELECT * FROM orders

        ORDER BY id DESC

    """)

    orders = cursor.fetchall()

    connection.close()

    return render_template(

        "my_orders.html",

        orders=orders
    )


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

        "price": "1,499",

        "category": "Medical",

        "stock": 5
    },

    "watch": {

        "name": "Luxury Watch",

        "image": "watch.jpg",

        "description":

        "Premium luxury watch for VIP customers.",

        "delivery": "VIP Delivery",

        "priority": 90,

        "resource_cost": 4,

        "price": "24,999",

        "category": "Luxury",

        "stock": 5
    },

    "grocery": {

        "name": "Grocery Pack",

        "image": "grocery.jpg",

        "description":

        "Daily household grocery essentials.",

        "delivery": "Normal Delivery",

        "priority": 50,

        "resource_cost": 2,

        "price": "2,999",

        "category": "Grocery",

        "stock": 5
    },

    "electronics": {

        "name": "Electronics Kit",

        "image": "electronics.jpg",

        "description":

        "Fragile electronic delivery package.",

        "delivery": "Fragile Delivery",

        "priority": 70,

        "resource_cost": 3,

        "price": "15,999",

        "category": "Electronics",

        "stock": 5
    },

    "food": {

        "name": "Food Package",

        "image": "food.jpg",

        "description":

        "Fast food delivery service package.",

        "delivery": "Fast Delivery",

        "priority": 80,

        "resource_cost": 4,

        "price": "799",

        "category": "Food",

        "stock": 5
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

            delivery_speed TEXT,

            status TEXT,

            created_at TEXT

        )

    """)


    # USERS TABLE

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS users (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT,

            email TEXT UNIQUE,

            password TEXT,

            address TEXT

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
        hashed_password = generate_password_hash(password)
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

            hashed_password

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

            WHERE email=?

        """, (

            email,

        ))

        user = cursor.fetchone()

        connection.close()

        if user and check_password_hash(

            user[3],

            password
        ):

            session["user"] = user[1]
            session.permanent = True
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

    category = request.args.get("category")

    price_filter = request.args.get("price")

    filtered_products = {}


    for key, value in products.items():

        matches_category = True

        matches_price = True


        # CATEGORY FILTER

        if category:

            matches_category = (

                value["category"].lower()

                ==

                category.lower()
            )


        # PRICE FILTER

        product_price = int(

            value["price"].replace(",", "")
        )


        if price_filter == "low":

            matches_price = product_price < 2000


        elif price_filter == "medium":

            matches_price = (

                2000 <= product_price < 5000
            )


        elif price_filter == "high":

            matches_price = product_price >= 5000


        if matches_category and matches_price:

            filtered_products[key] = value


    return render_template(

        "home.html",

        products=filtered_products
    )
# =========================
# REVIEWS STORAGE
# =========================

reviews_db = []

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


    # PRODUCT REVIEWS

    product_reviews = []

    for review in reviews_db:

        if review["product"] == product_name:

            product_reviews.append(review)


    # TOTAL REVIEWS

    total_reviews = len(product_reviews)


    # AVERAGE RATING

    average_rating = 0


    if total_reviews > 0:

        total = 0

        for review in product_reviews:

            total += int(review["rating"])

        average_rating = round(

            total / total_reviews,

            1
        )


    return render_template(

        "product.html",

        product_name=selected_product["name"],

        image=selected_product["image"],

        description=selected_product["description"],

        delivery=selected_product["delivery"],

        price=selected_product["price"],

        route_name=product_name,

        reviews=reviews_db,

        average_rating=average_rating,

        total_reviews=total_reviews
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

    if selected_product["stock"] <= 0:

        return "Out of Stock ❌"

    if request.method == "POST":

        customer_name = request.form["customer_name"]

        destination = request.form["destination"]
        session["destination"] = destination
        session["product_name"] = selected_product["name"]

        session["customer_name"] = customer_name
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

                delivery_speed,

                status,

                created_at

            )

            VALUES (?, ?, ?, ?, ?, ?, ?)

        """, (

            customer_name,

            selected_product["name"],

            destination,

            priority,

            delivery_speed,

            "Ordered",

            datetime.now().strftime("%d-%m-%Y %H:%M")

        ))

        order_id = cursor.lastrowid

        connection.commit()

        selected_product["stock"] -= 1
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

            url_for("payment")
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

        "image": selected_product["image"],

        "quantity": 1
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

        quantity = item.get("quantity", 1)

        total += int(price) * quantity

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
# INCREASE QUANTITY
# =========================

@app.route("/increase-quantity/<int:item_id>")
def increase_quantity(item_id):

    cart = session.get("cart", [])

    for item in cart:

        if item["id"] == item_id:

            item["quantity"] = item.get("quantity", 1) + 1

    session["cart"] = cart

    return redirect("/cart")


# =========================
# DECREASE QUANTITY
# =========================

@app.route("/decrease-quantity/<int:item_id>")
def decrease_quantity(item_id):

    cart = session.get("cart", [])

    for item in cart:

        if item["id"] == item_id:

            quantity = item.get("quantity", 1)

            if quantity > 1:

                item["quantity"] = quantity - 1

    session["cart"] = cart

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


    connection = sqlite3.connect("algo.db")

    cursor = connection.cursor()


    # GET REAL ORDERS

    cursor.execute("""

        SELECT * FROM orders

        ORDER BY id DESC

    """)

    orders = cursor.fetchall()


    # ANALYTICS

    delivered_count = 0

    cancelled_count = 0


    for order in orders:

        if "Delivered" in order[6]:

            delivered_count += 1

        elif "Cancelled" in order[6]:

            cancelled_count += 1


    admin_data = {

        "users": 12450,

        "orders": len(orders),

        "revenue": "92.5L",

        "deliveries": delivered_count,

        "fraud": 18,

        "stock": "Stable ✅"
    }

    connection.close()


    return render_template(

        "admin.html",

        data=admin_data,

        orders=orders,

        delivered_count=delivered_count,

        cancelled_count=cancelled_count
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

@app.route("/update-stock/<product_name>/<action>")
def update_stock(product_name, action):

    selected_product = products.get(product_name)

    if selected_product:

        if action == "increase":

            selected_product["stock"] += 1

        elif action == "decrease":

            if selected_product["stock"] > 0:

                selected_product["stock"] -= 1

    return redirect("/inventory")


# =========================
# INVENTORY MANAGEMENT
# =========================

@app.route("/inventory")
def inventory():

    if "user" not in session:

        return redirect("/login")


    inventory_items = []

    for key, value in products.items():

        inventory_items.append({

            "name": value["name"],

            "stock": value["stock"],

            "image": value["image"]
        })


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

@app.route("/dsa-solution")
def dsa_solution():

    destination = session.get(
        "destination",
        "Chennai"
    )

    city = destination.lower()

    if "chennai" in city:

        hub = "Chennai Central Hub"

        warehouse_distance = 20
        customer_distance = 15

    elif "vellore" in city:

        hub = "Vellore Logistics Hub"

        warehouse_distance = 45
        customer_distance = 20

    elif "kerala" in city:

        hub = "Kochi Distribution Hub"

        warehouse_distance = 120
        customer_distance = 40

    else:

        hub = "Regional Distribution Hub"

        warehouse_distance = 50
        customer_distance = 25

    total_distance = (

        warehouse_distance

        +

        customer_distance
    )

    route = f"Warehouse → {hub} → {destination}"

    product_name = session.get(
        "product_name",
        "Unknown Product"
    )

    username = session.get(
        "customer_name",
        "Customer"
    )

    if total_distance <= 40:

        eta = "12 Minutes"

    elif total_distance <= 80:

        eta = "25 Minutes"

    elif total_distance <= 150:

        eta = "45 Minutes"

    else:

        eta = "90 Minutes"

    return render_template(

        "dsa_solution.html",

        destination=destination,

        hub=hub,

        route=route,

        product=product_name,

        customer=username,

        eta=eta,

        warehouse_distance=warehouse_distance,

        customer_distance=customer_distance,

        total_distance=total_distance
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

@app.route("/save-address", methods=["POST"])
def save_address():

    if "user" not in session:

        return redirect("/login")

    address = request.form["address"]

    username = session["user"]

    connection = sqlite3.connect("algo.db")

    cursor = connection.cursor()

    cursor.execute("""

        UPDATE users

        SET address=?

        WHERE username=?

    """, (

        address,

        username
    ))

    connection.commit()

    connection.close()

    return redirect("/profile")


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

    cursor.execute("""

        SELECT * FROM orders

        WHERE LOWER(customer_name)=?

        ORDER BY id DESC

    """, (

        username.lower(),

    ))

    orders = cursor.fetchall()


    # DELIVERY STATS

    delivered_orders = 0

    cancelled_orders = 0


    for order in orders:

        if "Delivered" in order[6]:

            delivered_orders += 1

        elif "Cancelled" in order[6]:

            cancelled_orders += 1


        # SAVED ADDRESS

        cursor.execute("""

            SELECT address

            FROM users

            WHERE LOWER(username)=?

        """, (

            username.lower(),

        ))

        address_data = cursor.fetchone()

        saved_address = ""


        if address_data and address_data[0]:

            saved_address = address_data[0]


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

        wishlist_count=wishlist_count,

        delivered_orders=delivered_orders,

        cancelled_orders=cancelled_orders,

        saved_address=saved_address,
    )

# =========================
# PAYMENT PAGE
# =========================

@app.route("/payment", methods=["GET", "POST"])
def payment():

    if "user" not in session:

        return redirect("/login")

    error = None


    if request.method == "POST":

        payment_method = request.form["payment_method"]

        card_number = request.form["card_number"]

        card_name = request.form["card_name"]

        cvv = request.form["cvv"]


        # EMPTY CHECK

        if (

            not payment_method

            or

            not card_name

            or

            not card_number

            or

            not cvv
        ):

            error = "Please fill all payment details ❌"


        # CARD NUMBER CHECK

        elif (

            len(card_number) != 16

            or

            not card_number.isdigit()
        ):

            error = "Card Number must contain exactly 16 digits ❌"


        # CVV CHECK

        elif (

            len(cvv) != 3

            or

            not cvv.isdigit()
        ):

            error = "CVV must contain exactly 3 digits ❌"


        else:

            transaction_id = (

                "TXN"

                +

                datetime.now().strftime("%H%M%S")
            )

            return render_template(

                "payment_success.html",

                transaction_id=transaction_id
            )

    return render_template(

        "payment.html",

        error=error
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
# UPDATE STATUS
# =========================

@app.route("/update-status/<int:order_id>/<new_status>")
def update_status(order_id, new_status):

    connection = sqlite3.connect("algo.db")

    cursor = connection.cursor()

    cursor.execute("""

        UPDATE orders

        SET status=?

        WHERE id=?

    """, (

        new_status,

        order_id
    ))

    connection.commit()

    connection.close()

    return redirect("/live-tracking")

# =========================
# AUTO DELIVERY STATUS
# =========================

def auto_update_status(order_id):

    statuses = [

        "Packed 📦",

        "Shipped 🚚",

        "Delivered ✅"
    ]

    for status in statuses:

        time.sleep(6)

        connection = sqlite3.connect("algo.db")

        cursor = connection.cursor()

        cursor.execute("""

            UPDATE orders

            SET status=?

            WHERE id=?

        """, (

            status,

            order_id
        ))

        connection.commit()

        connection.close()

# =========================
# TRACKING PAGE
# =========================
@app.route("/tracking")
def tracking():

    if "user" not in session:

        return redirect("/login")


    connection = sqlite3.connect("algo.db")

    cursor = connection.cursor()

    cursor.execute("""

        SELECT * FROM orders

        ORDER BY id DESC

    """)

    orders = cursor.fetchall()
    for order in orders:

        if order[6] == "Ordered":

            threading.Thread(

                target=auto_update_status,

                args=(order[0],)

            ).start()
    connection.close()


    return render_template(

        "tracking.html",

        orders=orders
    )

# =========================
# CANCEL ORDER
# =========================

@app.route("/cancel-order/<int:order_id>")
def cancel_order(order_id):

    connection = sqlite3.connect("algo.db")

    cursor = connection.cursor()

    cursor.execute("""

        UPDATE orders

        SET status = ?

        WHERE id = ?

    """, ("Cancelled ❌", order_id))

    connection.commit()

    connection.close()

    return redirect("/live-tracking")


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
from datetime import datetime

@app.route("/queue-demo")
def queue_demo():

    queue_data = queue_engine.get_queue()

    return render_template(

        "queue_demo.html",

        queue_data=queue_data
    )
@app.route(

    "/bst-demo",

    methods=["GET", "POST"]

)
def bst_demo():

    result = None

    if request.method == "POST":

        keyword = request.form["keyword"].lower()

        result = bst_engine.search(

            keyword
        )

    traversal = bst_engine.inorder_traversal()

    return render_template(

        "bst_demo.html",

        result=result,

        traversal=traversal
    )

@app.route("/heap-demo")
def heap_demo():

    heap_data = sorted(

        heap_engine.get_all_orders()

    )

    highest = heap_engine.get_highest_priority()

    return render_template(

        "heap_demo.html",

        heap_data=heap_data,

        highest=highest
    )

@app.route("/hashmap-demo")
def hashmap_demo():

    orders = hashmap_engine.get_all_orders()

    return render_template(

        "hashmap_demo.html",

        orders=orders
    )
@app.route("/graph-demo")
def graph_demo():

    destination = session.get(
        "destination",
        "Chennai"
    )

    city = destination.lower()

    if "chennai" in city:

        hub = "Chennai Central Hub"

        d1 = 30
        d2 = 15

    elif "vellore" in city:

        hub = "Vellore Logistics Hub"

        d1 = 45
        d2 = 20

    elif "kerala" in city:

        hub = "Kochi Distribution Hub"

        d1 = 70
        d2 = 35

    else:

        hub = "Regional Hub"

        d1 = 40
        d2 = 20

    return render_template(

        "graph_demo.html",

        destination=destination,

        hub=hub,

        d1=d1,

        d2=d2
    )
@app.route("/demo-graph")
def demo_graph():

    return """
    Warehouse
      |
    Chennai Hub
      |
    Customer
    """

@app.route("/dijkstra-demo")
def dijkstra_demo():

    destination = session.get(
        "destination",
        "CHENNAI"
    )

    city = destination.lower()

    graph = {

        "Warehouse": []
    }

    if "vellore" in city:

        hub = "Vellore Hub"

        graph["Warehouse"] = [

            (hub, 45)
        ]

        graph[hub] = [

            ("VELLORE", 20)
        ]

        graph["VELLORE"] = []

        end = "VELLORE"

    elif "kerala" in city:

        hub = "Kochi Hub"

        graph["Warehouse"] = [

            (hub, 70)
        ]

        graph[hub] = [

            ("KERALA", 35)
        ]

        graph["KERALA"] = []

        end = "KERALA"

    else:

        hub = "Chennai Hub"

        graph["Warehouse"] = [

            (hub, 30)
        ]

        graph[hub] = [

            ("CHENNAI", 15)
        ]

        graph["CHENNAI"] = []

        end = "CHENNAI"

    path, distance = dijkstra_engine.shortest_path(

        graph,

        "Warehouse",

        end
    )

    return render_template(

        "dijkstra_demo.html",

        path=path,

        distance=distance,

        destination=destination
    )
@app.route("/dp-demo")
def dp_demo():

    destination = session.get(
        "destination",
        "CHENNAI"
    )

    city = destination.lower()

    if "vellore" in city:

        distance = 65

        traffic = "Medium"

        priority = "High"

        eta = "25 Minutes"

    elif "kerala" in city:

        distance = 105

        traffic = "High"

        priority = "High"

        eta = "40 Minutes"

    else:

        distance = 45

        traffic = "Low"

        priority = "High"

        eta = "18 Minutes"

    return render_template(

        "dp_demo.html",

        destination=destination,

        distance=distance,

        traffic=traffic,

        priority=priority,

        eta=eta
    )
@app.route("/dsa-labs")
def dsa_labs():

    return render_template(
        "dsa_labs.html"
    )
# =========================
# ADD REVIEW
# =========================

@app.route("/add-review/<product_name>", methods=["POST"])
def add_review(product_name):

    if "user" not in session:

        return redirect("/login")

    username = session["user"]

    review_text = request.form["review"]

    rating = request.form["rating"]


    # CHECK EXISTING REVIEW

    for review in reviews_db:

        if (

            review["user"] == username

            and

            review["product"] == product_name
        ):

            return "You already reviewed this product ⚠️"


    # ADD REVIEW

    reviews_db.append({

        "user": username,

        "product": product_name,

        "review": review_text,

        "rating": rating
    })

    return redirect(f"/product/{product_name}")
if __name__ == "__main__":

    socketio.run(app, debug=True)