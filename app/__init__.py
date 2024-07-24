from flask import Flask
from config import Config
import pickle

# Define the path for the model
MODEL_PATH = 'ML-Diabetes-Prediction/app/data/rf_model.pkl'

def init_app():
    app = Flask(__name__)
    # import configuration
    app.config.from_object(Config)
    with app.app_context():
        # Import parts of our core Flask app
        from . import routes

        # Import Dash application
        from .plotlydash.dashboard import init_dashboard
        app = init_dashboard(app)

        return app

# Ensure the model is loaded correctly
rf_model = pickle.load(open('ML-Diabetes-Prediction/app/rf_model.pkl', 'rb'))
