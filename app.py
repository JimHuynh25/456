from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Dictionary of countries and their capitals
country_capitals = {
    "canada": "Ottawa",
    "united states": "Washington, D.C.",
    "france": "Paris",
    "germany": "Berlin",
    "japan": "Tokyo",
    "india": "New Delhi",
    "china": "Beijing",
    "australia": "Canberra",
    "brazil": "Brasília",
    "italy": "Rome",
    "russia": "Moscow",
    "mexico": "Mexico City",
    "spain": "Madrid",
    "south korea": "Seoul",
    "united kingdom": "London",
}

# Route to render the index.html file
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint to handle chat messages
@app.route('/api/chat', methods=['POST'])
def handle_chat():
    try:
        data = request.get_json()
        message = data.get('message', '').lower()  # Convert message to lowercase for case-insensitive comparison
        
        if not message:
            return jsonify({"error": "No message provided"}), 400

        # Default response
        response = "I'm sorry, I didn't understand that."

        # Chatbot logic for general queries
        if "hello" in message:
            response = "Hello! How can I assist you today?"
        elif "space" in message:
            response = (
                "Did you know that space is completely silent? "
                "There's no atmosphere, so sound cannot travel."
            )
        elif "president" in message and "united states" in message:
            response = "The current President of the United States is Joe Biden."
        elif "weather" in message:
            response = "I'm not a weather bot, but you can try asking about your city's weather online!"
        elif "dog" in message:
            response = "Dogs are wonderful companions! Did you know that the Labrador Retriever is the most popular dog breed in the US?"
        elif "bank" in message:
            response = "Banks are financial institutions that help manage money. They offer services like savings accounts, loans, and investments."
        
        # Check for country and respond with the capital
        for country, capital in country_capitals.items():
            if country in message:
                response = f"The capital of {country.capitalize()} is {capital}."
                break

        return jsonify({"response": response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
