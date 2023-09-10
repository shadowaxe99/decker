from flask import Flask, render_template, request
from decker.PitchDeckGenerator import PitchDeckGenerator
from decker.WebSearcher import WebSearcher

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        brand = request.form.get('brand')
        generator = PitchDeckGenerator()
        searcher = WebSearcher()
        xcom_links = searcher.search('site:x.com ' + brand)
        crunchbase_links = searcher.search('site:crunchbase.com ' + brand)
        generator.create_pitch_deck(brand, xcom_links, crunchbase_links)
        return render_template('success.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)