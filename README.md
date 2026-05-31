# AlgoVision – Smart Logistics Powered by Data Structures and Algorithms

## Project Overview

AlgoVision is a Smart Logistics and Delivery Optimization Platform developed using Python, Flask, HTML, CSS, and JavaScript.

The project demonstrates the practical implementation of Data Structures and Algorithms in real-world logistics systems. It simulates how modern delivery platforms manage incoming orders, prioritize urgent deliveries, optimize routes, estimate delivery times, and efficiently retrieve product and order information.

The system integrates multiple DSA concepts into a single workflow, making it both an educational and industry-oriented project.

---

## Features

* Product Catalog Management
* Order Placement System
* Shopping Cart
* Wishlist Management
* User Profile Management
* Inventory Management
* Live Delivery Tracking
* Route Visualization
* Fraud Detection Module
* JWT Authentication
* Real-Time Updates using SocketIO
* Analytics Dashboard
* AI ETA Prediction
* DSA Laboratory Modules

---

## Data Structures and Algorithms Used

### Queue

Used for managing incoming customer orders using FIFO (First In First Out).

### HashMap

Provides instant product and order lookup with O(1) complexity.

### Array

Stores and manages product catalog information.

### Binary Search Tree (BST)

Used for efficient product searching with O(log n) search complexity.

### Heap

Used for delivery priority scheduling.

Higher priority deliveries are processed first. If priorities are equal, timestamp-based ordering is used.

### Graph

Represents the logistics network.

Warehouses, logistics hubs and destinations are modeled as nodes while roads are modeled as edges.

### Dijkstra Algorithm

Calculates the shortest delivery route between source and destination.

### Dynamic Programming

Optimizes ETA prediction and delivery resource utilization.

---

## Project Workflow

Customer Places Order

↓

Queue Stores Incoming Order

↓

HashMap Retrieves Product Information

↓

Array Stores Product Catalog

↓

BST Enables Product Search

↓

Heap Prioritizes Deliveries

↓

Graph Models Logistics Network

↓

Dijkstra Finds Shortest Route

↓

Dynamic Programming Optimizes ETA

↓

Delivery Completed

---

## Technologies Used

### Backend

* Python
* Flask

### Frontend

* HTML
* CSS
* JavaScript

### Database

* SQLite
* MySQL Connector

### Authentication

* JWT Authentication

### Real-Time Communication

* Flask SocketIO
* Eventlet

---

## Project Structure

app.py

queue_engine.py

hashmap_engine.py

bst_engine.py

heap_engine.py

graph_engine.py

dijkstra_engine.py

dp_engine.py

database.py

templates/

static/

algo.db

requirements.txt

README.md

---

## Installation

1. Clone the repository

2. Install dependencies

pip install -r requirements.txt

3. Run the application

python app.py

4. Open browser

http://127.0.0.1:5000

---

## Author

Developed as a LaunchED Capstone Project.

Project Title:
AlgoVision – Smart Logistics Powered by Data Structures and Algorithms