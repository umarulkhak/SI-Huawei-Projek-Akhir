from errno import EDOM
from flask import Flask, render_template, flash, request, url_for, redirect, session
import numpy as np
import re
import os
import tensorflow as tf
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from model import db, EdomModel
import pickle


IMAGE_FOLDER = os.path.join('static', 'img_pool')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()


with open('tokenizer1.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)


def init():
    global model, graph
    graph = tf.Graph()


@app.route('/', methods=['GET', 'POST'])
def home():

    return render_template("home.html")


@app.route('/predict', methods=['GET', 'POST'])
def predik():

    return render_template("index.html")


@app.route('/data')
def data():
    edom = EdomModel.query.all()
    return render_template("data.html", edom=edom)


@app.route('/about')
def about():

    return render_template("about.html")


@app.route('/sentiment_prediction', methods=['POST', "GET"])
def sent_anly_prediction():
    if request.method == 'POST':
        text = request.form['review']

        sentiment_classes = ['Baik', 'Cukup', 'Kurang', 'Sangat Baik']
        max_len = 50
        # Transforms text to a sequence of integers using a tokenizer object
        xt = tokenizer.texts_to_sequences([text])
        # Pad sequences to the same length
        xt = pad_sequences(xt, padding='post', maxlen=max_len)

        with graph.as_default():
            # load the pre-trained Keras model
            model = load_model('best_model.h5')
            yt = model.predict(xt).argmax(axis=1)
            probability = model.predict(xt)[0][0]
            sentiment = sentiment_classes[yt[0]]

            if sentiment == 'Kurang':
                img_filename = os.path.join(
                    app.config['UPLOAD_FOLDER'], 'merah.png')
            elif sentiment == 'Cukup':
                img_filename = os.path.join(
                    app.config['UPLOAD_FOLDER'], 'kuning.png')
            elif sentiment == 'Baik':
                img_filename = os.path.join(
                    app.config['UPLOAD_FOLDER'], 'hijau.png')
            else:
                img_filename = os.path.join(
                    app.config['UPLOAD_FOLDER'], 'biru.png')

        nama = request.form['nama']
        semester = request.form['semester']
        review = request.form['review']
        edom = EdomModel(
            nama=nama,
            semester=semester,
            review=review,
            sentiment=sentiment,
            probability=probability
        )
        db.session.add(edom)
        db.session.commit()

    return render_template('index.html', text=text, sentiment=sentiment, probability=probability, image=img_filename)


@app.route('/<int:id>/delete', methods=['GET', 'POST'])
def delete(id):
    edom = EdomModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        if edom:
            db.session.delete(edom)
            db.session.commit()
            return redirect('/')
        abort(404)
     # return redirect('/')
    return render_template('delete.html')


init()
app.run(debug=True)
