from flask import Flask
from config.config import load_env_variables

app = Flask(__name__)

# Load environment variables
load_env_variables()

from app import routes  # Import the routes
