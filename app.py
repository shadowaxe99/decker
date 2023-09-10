from flask import Flask, render_template, request
from PitchDeckGenerator import PitchDeckGenerator

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        brand = request.form.get('brand')
        generator = PitchDeckGenerator()
        generator.create_pitch_deck(brand)
        return render_template('success.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)