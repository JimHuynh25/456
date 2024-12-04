from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import re  # For better pattern matching

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
    "argentina": "Buenos Aires",
    "south africa": "Pretoria",
    "egypt": "Cairo",
    "kenya": "Nairobi",
    "turkey": "Ankara",
    "sweden": "Stockholm",
    "norway": "Oslo",
    "finland": "Helsinki",
    "netherlands": "Amsterdam",
    "belgium": "Brussels",
    "switzerland": "Bern",
    "denmark": "Copenhagen",
    "poland": "Warsaw",
    "portugal": "Lisbon",
    "singapore": "Singapore",
    "new zealand": "Wellington",
    "afghanistan": "Kabul",
    "armenia": "Yerevan",
    "azerbaijan": "Baku",
    "bangladesh": "Dhaka",
    "bhutan": "Thimphu",
    "brunei": "Bandar Seri Begawan",
    "burma": "Naypyidaw",
    "cambodia": "Phnom Penh",
    "georgia": "Tbilisi",
    "india": "New Delhi",
    "indonesia": "Jakarta",
    "iran": "Tehran",
    "iraq": "Baghdad",
    "israel": "Jerusalem",
    "jordan": "Amman",
    "kazakhstan": "Astana",
    "kyrgyzstan": "Bishkek",
    "laos": "Vientiane",
    "lebanon": "Beirut",
    "malaysia": "Kuala Lumpur",
    "maldives": "Malé",
    "mongolia": "Ulaanbaatar",
    "nepal": "Kathmandu",
    "north korea": "Pyongyang",
    "oman": "Muscat",
    "pakistan": "Islamabad",
    "palestine": "Ramallah",
    "philippines": "Manila",
    "qatar": "Doha",
    "saudi arabia": "Riyadh",
    "singapore": "Singapore",
    "south korea": "Seoul",
    "sri lanka": "Sri Jayawardenepura Kotte",
    "syria": "Damascus",
    "tajikistan": "Dushanbe",
    "thailand": "Bangkok",
    "timor-leste": "Dili",
    "turkmenistan": "Ashgabat",
    "united arab emirates": "Abu Dhabi",
    "uzbekistan": "Tashkent",
    "vietnam": "Hanoi",
    "yemen": "Sana'a",
}

# Route to render the index.html file
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint to handle chat messages
@app.route('/api/chat', methods=['POST'])
def handle_chat():
    try:
        # Get the user's message
        data = request.get_json()
        message = data.get('message', '').lower()  # Normalize to lowercase
        
        if not message:
            return jsonify({"error": "No message provided"}), 400

        # Default response
        response = "I'm sorry, I didn't understand that."

        # General responses
        if "hello" in message:
            response = "Hello! How can I assist you today?"
        elif "bye" in message:
            response = "Goodbye! It was nice talking to you."
        elif "space" in message:
            response = (
                "Did you know that space is completely silent? "
                "There's no atmosphere, so sound cannot travel."
            )
        elif "dog" in message:
            response = "Dogs are amazing animals! They are loyal, friendly, and make great companions."
        elif "bank" in message:
            response = "Banks help you manage your finances. Need more information about banking?"

        # Match country name for capitals
        for country, capital in country_capitals.items():
            # Use regex to detect exact country name in the message
            if re.search(rf'\b{country}\b', message):
                response = f"The capital of {country.capitalize()} is {capital}."
                break

        return jsonify({"response": response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
