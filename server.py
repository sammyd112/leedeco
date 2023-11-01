from flask import (Flask, redirect, request, render_template, session, jsonify, flash)
import json

app = Flask(__name__)



@app.route('/')
def show_homepage():
    return render_template("homepage.html")

@app.route('/about')
def show_about():
    return render_template("about.html")

@app.route('/services')
def show_services():
    return render_template("services.html")

@app.route('/projects')
def show_projects():
    return render_template("projects.html")

@app.route('/contact')
def show_contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")