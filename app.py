from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

# Lists of adjectives and nouns
adjectives = ["Happy", "Cool", "Brave", "Clever", "Mighty", "Fierce", "Jolly"]
nouns = ["Dragon", "Tiger", "Wizard", "Knight", "Phoenix", "Panda", "Wolf"]

# Function to generate username
def generate_username(add_number=False, add_special=False):
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adj + noun

    if add_number:
        username += str(random.randint(10, 99))  # Add random number

    if add_special:
        username += random.choice(string.punctuation)  # Add special character

    return username

# Route to serve the webpage
@app.route('/')
def index():
    return render_template('index.html')

# Route to generate username via API
@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    add_number = data.get('addNumber', False)
    add_special = data.get('addSpecial', False)

    username = generate_username(add_number, add_special)

    # Save to file
    with open("usernames.txt", "a") as file:
        file.write(username + "\n")

    return jsonify({"username": username})

if __name__ == '__main__':
    app.run(debug=True)
