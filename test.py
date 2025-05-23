import pickle

# Load trained model and vectorizer
model = pickle.load(open("phishing_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def predict_message(text):
    """Predict whether a message is phishing or safe."""
    text_vectorized = vectorizer.transform([text])  # Convert text to numerical format
    prediction = model.predict(text_vectorized)[0]  # Get prediction (0 = Safe, 1 = Phishing)
    
    return "⚠️ Phishing Message" if prediction == 1 else "✅ Safe Message"

# Get message input from user
while True:
    user_message = input("\nEnter a message to check (or type 'exit' to quit): ")
    if user_message.lower() == "exit":
        print("Exiting program. 🔴")
        break

    print(f"Prediction: {predict_message(user_message)}")
