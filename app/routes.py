from flask import request, jsonify
from app import app
from app.gpt import ask_gpt

@app.route("/whatsapp", methods=["POST"])
def whatsapp_bot():
    incoming_msg = request.values.get('Body', '').lower()
    response_text = ask_gpt(incoming_msg)
    return jsonify({"response": response_text})
