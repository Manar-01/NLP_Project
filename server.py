#TODO: establishing server
from flask import Flask, render_template, request
import nltk
import spacy
app = Flask(__name__)


# essential entity models downloads
nltk.downloader.download('maxent_ne_chunker')
nltk.downloader.download('words')
nltk.downloader.download('treebank')
nltk.downloader.download('maxent_treebank_pos_tagger')
nltk.downloader.download('punkt')
nltk.download('averaged_perceptron_tagger')
spacy.cli.download('en_core_web_sm')

import locationtagger


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ExData', methods=['POST', 'GET'])
def ExData():
    # TODO: connect input text with backend
    text = ""
    if request.method == 'POST':
        text = request.form.get("text")
    # TODO: extract information
    # initializing sample text
    sample_text = text

    # extracting entities.
    place_entity = locationtagger.find_locations(text=sample_text)

    # getting all country regions
    print("The countries regions in text : ")
    print(place_entity.country_regions)

    # getting all country cities
    print("The countries cities in text : ")
    print(place_entity.country_cities)

    # getting all other countries
    print("All other countries in text : ")
    print(place_entity.other_countries)

    # getting all region cities
    print("The region cities in text : ")
    print(place_entity.region_cities)

    # getting all other regions
    print("All other regions in text : ")
    print(place_entity.other_regions)

    # getting all other entities
    print("All other entities in text : ")
    print(place_entity.other)
    return render_template('ExData.html')


if __name__ == "__main__":
    app.run(debug=True)



