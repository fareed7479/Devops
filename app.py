from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
import re

app = Flask(__name__)
app.secret_key = "secret_key"

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client.registration_db
collection = db.users

@app.route("/")
def index():
    return render_template("reg.html")

@app.route("/register", methods=["POST"])
def register():
    # Form data
    full_name = request.form.get("fullName")
    email = request.form.get("email")
    password = request.form.get("password")
    username = request.form.get("username")
    phone = request.form.get("phone")
    confirm_password = request.form.get("confirmPassword")
    gender = request.form.get("gender")

    # Validation
    if not full_name or not email or not password or not username or not phone or not gender:
        flash("All fields are required!", "error")
        return redirect(url_for("index"))

    if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
        flash("Invalid email format!", "error")
        return redirect(url_for("index"))

    if password != confirm_password:
        flash("Passwords do not match!", "error")
        return redirect(url_for("index"))

    if not re.match(r"^[0-9]{10}$", phone):
        flash("Invalid phone number! Must be 10 digits.", "error")
        return redirect(url_for("index"))

    # Check if username or email already exists
    if collection.find_one({"username": username}) or collection.find_one({"email": email}):
        flash("Username or email already exists!", "error")
        return redirect(url_for("index"))

    # Save to MongoDB
    user = {
        "full_name": full_name,
        "email": email,
        "password": password,
        "username": username,
        "phone": phone,
        "gender": gender,
    }
    collection.insert_one(user)

    flash("Registration successful!", "success")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
