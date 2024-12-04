import csv
import random
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Read CSV file and store data
def load_plants():
    plants = []
    with open('plant_classification_with_images.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            plants.append(row)
    #print("Plants loaded:", plants)  # Debugging the plants data
    return plants

@app.route('/')
def index():
    plants = load_plants()
    return render_template('index.html', plants=plants)

@app.route('/random_plant')
def random_plant():
    plants = load_plants()
    plant = random.choice(plants)
    print("Plant loaded:", plant)  # Debugging the plants data
    return jsonify(plant)

if __name__ == '__main__':
    app.run(debug=True)
