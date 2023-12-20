from flask import (Flask, redirect, request, render_template, session, jsonify, flash)
import json
import os
from jinja2 import StrictUndefined
from email.message import EmailMessage
from email.mime.text import MIMEText
import ssl
import smtplib

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def show_homepage():
    return render_template("homepage.html")

@app.route('/services')
def show_services():
    return render_template("services.html")

@app.route('/projects')
def show_projects():
    return render_template("projects.html")

@app.route('/contact')
def show_contact():
    return render_template("contact.html")

@app.route("/contactus", methods = ['POST'])
def contact_us():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']
    print(name, email, phone, message)

    sender = 'sammydunlop112@gmail.com'
    passcode = os.environ['GMAIL_PASSCODE']
    rec_email = 'mpapile@leedecorating.us'

    subject = 'AUTOMATED MESSAGE: ESTIMATE REQUEST'
    body = f"NEW MESSAGE \n Contact Name: {name} \n Contact Email: {email} \n Contact Phone: {phone} \n\n {message}"

    em = EmailMessage()
    em['From'] = sender
    em['To'] = rec_email
    em['Subject'] = subject
    em.set_content(body)

    if phone.isupper() or phone.islower() or len(phone) != 10:
        flash('The number you have entered is not 10 digits. Also ensure number does not contain dashes', 'warning')
        print("phone nope")
    elif phone == "" or email == "" or name == "" or message == "":
        flash('Please complete all fields to sumbit your message', 'warning')
        print('completion nope')
    else:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, passcode)
        print("Success")
        server.sendmail(sender, rec_email, em.as_string())
        print("Email Sent")
        flash('Your message has been sent', 'success')
    return render_template("homepage.html")

if __name__ == "__main__":
    app.run()