import os
from flask import Flask, render_template, request
from flask_mail import Message, Mail

mail = Mail()

def create_app():

    app = Flask(__name__)    
    app.secret_key = os.environ.get('SECRET_FLASK_KEY')
    
    app.config["MAIL_SERVER"] = "smtp.gmail.com"
    app.config["MAIL_PORT"] = os.environ.get("SEND_PORT")
    app.config["MAIL_USE_SSL"] = True
    app.config["MAIL_USERNAME"] = os.environ.get("SEND_USERNAME")
    app.config["MAIL_PASSWORD"] = os.environ.get("SEND_PASSWORD")
    
    mail.init_app(app)

    from . import models
    app.register_blueprint(models.bp)
    from .forms import ContactForm



    @app.route('/')
    @app.route('/home')
    def index():
        form = ContactForm(request.form)
        return render_template("index.html", form=form)


    return app