from flask import Flask, request, jsonify
import pickle
import requests

# Load trained model and vectorizer
try:
    model = pickle.load(open("phishing_model.pkl", "rb"))
    vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
except Exception as e:
    print(f"Error loading model/vectorizer: {e}")
    exit(1)

# Flask app
app = Flask(__name__)

VERIFY_TOKEN = "my_secret_key"  # Use this same token in Meta Developer Console

# WhatsApp API details (Replace with your values)
WHATSAPP_ACCESS_TOKEN = "EAAOA1pXwyK0BOyfSvH7RqtXQbZAnI3YMwOo0lJPZCsAQzXC3blIAhDYBZBU9FcZBaSZBZCbLfXgJymHHvhEo9DKqpcP1od5tgZAySEonfrN3iKvLJ1SmWA8meZCRw2JGFfzZAPZBcdKJEoUL2KsAlQZBZCuClsqxtg9HyvE1W3yZAcXiLW5WvZBPTsWBkCYQ5gBUWOKWSWcFLJMhXqnAehBEAX7rw3pECQYB4BsHWARAsZD"
PHONE_NUMBER_ID = "635754452960009"
WHATSAPP_API_URL = f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages"

# Verify webhook
@app.route("/webhook", methods=["GET"])
def verify_webhook():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return challenge, 200
    return "Forbidden", 403

# Handle incoming WhatsApp messages
@app.route("/webhook", methods=["POST"])
def receive_message():
    data = request.json
    try:
        if "entry" in data and data["entry"]:
            changes = data["entry"][0].get("changes", [])
            if changes:
                value = changes[0].get("value", {})
                messages = value.get("messages", [])
                if messages:
                    message = messages[0]
                    sender_number = message.get("from", "Unknown")
                    text = message.get("text", {}).get("body", "")
                    
                    if text:
                        print("text received")
                        # Predict phishing
                        text_vectorized = vectorizer.transform([text])
                        is_phishing = model.predict(text_vectorized)[0]

                        # Prepare response message
                        response_text = "⚠️ Warning! This message may be a phishing scam." if is_phishing else "✅ This message seems safe."

                        # Send response to user
                        send_whatsapp_message(sender_number, response_text)
                        return jsonify({"status": "Message processed"}), 200
    
        print("No valid message received.")
        return jsonify({"error": "No valid message"}), 400
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Failed to process message"}), 400

# Function to send WhatsApp messages
def send_whatsapp_message(to, message):
    headers = {
        "Authorization": f"Bearer {WHATSAPP_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": message}
    }
    response = requests.post(WHATSAPP_API_URL, headers=headers, json=payload)
    print(response.json())  # Debugging

# Run Flask server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
