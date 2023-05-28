from flask import Flask

app = Flask(__name__)

app.config["ENV"] = "development"  # Set the 'ENV' key explicitly

if app.config["ENV"] == "production":
    app.config.from_object("config.DevelopmentConfig")
elif app.config["ENV"] == "testing":
    app.config.from_object("config.TestingConfig")
else:
    app.config.from_object("config.ProductionConfig")

from app import views
