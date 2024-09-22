from flask import Flask

def create_app():
    app = Flask(__name__)

   
    from .routes import whatsapp_webhook
    app.register_blueprint(whatsapp_webhook)

    return app
