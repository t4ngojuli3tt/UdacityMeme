import random
import os
import requests
from flask import Flask, render_template, abort, request


from QuoteEngine import QuoteModel, Ingestor
from MemeGenerator import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for file in quote_files:
        quotes += Ingestor.parse(file)

    images_path = "./_data/photos/dog/"

    imgs = [os.path.join(images_path, file)
            for file in os.listdir(images_path) if file.endswith('.jpg')]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """
    try:
        image_url = request.form['image_url']
        body = request.form['body']
        author = request.form['author']
    except:
        raise Exception('Bad request')

    quote = QuoteModel(body, author)

    r = requests.get(image_url, allow_redirects=True)
    img = f'./tmp/{random.randint(0, 100000000)}.jpg'
    open(img, 'wb').write(r.content)

    path = meme.make_meme(img, quote.body, quote.author)

    os.remove(img)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run(debug=True)
