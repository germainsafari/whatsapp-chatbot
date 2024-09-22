from flask import Blueprint, request, jsonify
from app.gpt import ask_gpt
from app.data_handler import handle_custom_data

whatsapp_webhook = Blueprint('whatsapp_webhook', __name__)

@whatsapp_webhook.route("/whatsapp", methods=["POST"])
def whatsapp():
    incoming_msg = request.values.get('Body', '').lower()


    custom_answer = handle_custom_data(incoming_msg)

    if custom_answer:
        response_text = custom_answer
    else:
       
        response_text = ask_gpt(incoming_msg)

    
    return jsonify({"message": response_text})
