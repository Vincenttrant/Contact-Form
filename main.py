from flask import Flask, render_template, request, redirect, flash, session
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from dotenv import load_dotenv
from config import MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD, MAIL_USE_TLS, MAIL_USE_SSL
from models import create_models

app = Flask(__name__)
load_dotenv()


# Datbase
app.config["SECRET_KEY"] = "123"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact_message.db'
db = SQLAlchemy(app)

Data_message = create_models(db)

# Mail
app.config['MAIL_SERVER'] = MAIL_SERVER
app.config['MAIL_PORT'] = MAIL_PORT
app.config['MAIL_USERNAME'] = MAIL_USERNAME
app.config['MAIL_PASSWORD'] = MAIL_PASSWORD
app.config['MAIL_USE_TLS'] = MAIL_USE_TLS
app.config['MAIL_USE_SSL'] = MAIL_USE_SSL
mail = Mail(app)


# Fixes databsae tables intially
@app.before_first_request
def create_tables():
    db.create_all()


# admin authentication
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("admin"):
            return f(*args, **kwargs)
        else:
            return redirect("/login")
    return decorated_function


@app.route("/", methods=["GET"])
def contact():
    return render_template("form.html")

@app.route("/", methods=["POST"])
def form():
    name = request.form.get("name")
    email = request.form.get("email")
    subject = request.form.get("subject")
    message = request.form.get("message")


    # Checks if all sections of form are filled out
    if not name or not email or not subject or not message:
        error_form = "Error filling out form"
        return render_template("form.html", error_form=error_form, name=name, email=email, subject=subject, message=message)


    # Sends data into database
    new_message = Data_message(name=name, email=email, subject=subject, message=message)
    db.session.add(new_message)
    db.session.commit()


    # Sends data to my email    
    msg = Message("Python Flask contact email", sender='noreply@demo.com', recipients=['youremail@gmail.com'])
    msg.subject = subject
    msg.body = (f'This is a message from, {name} - {email} using your contact form.\n\n{message}')
    
    mail.send(msg)
    
    return render_template("success.html", name=name, message=message)



# Reads messages from database
@app.route("/messages", methods=["GET"])
@admin_required
def display_messages():
    messages = Data_message.query.all()
    return render_template("messages.html", messages=messages)

@app.route("/delete_message/<int:message_id>", methods=["POST"])
def delete_message(message_id):
    message = Data_message.query.get_or_404(message_id)
    db.session.delete(message)
    db.session.commit() 
    return redirect('/messages')


@app.route("/login", methods=["GET", "POST"])
def login():
    error_login = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Checks correct username and password for admin authentication
        if username == "admin" and password == "password": 
            session["admin"] = True
            return redirect("/messages")

        error_login = "Unknown Username/Password"
    
    return render_template("login.html", error_login=error_login)

@app.route("/logout")
@admin_required
def logout():
    session.pop("admin", None)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)