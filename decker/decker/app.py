from flask import Flask, render_template, request
from .PitchDeckGenerator import PitchDeckGenerator

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        brand = request.form['brand']
        xcom_links = request.form['xcom_links']
        crunchbase_links = request.form['crunchbase_links']
        pitch_deck_generator = PitchDeckGenerator(brand, xcom_links, crunchbase_links)
        pitch_deck_generator.generate()
        return 'Pitch deck generated successfully!'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)