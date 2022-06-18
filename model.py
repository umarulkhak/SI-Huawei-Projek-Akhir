from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class EdomModel(db.Model):
    __tablename__ = "edom"

    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String())
    semester = db.Column(db.String())
    review = db.Column(db.String())
    sentiment = db.Column(db.String())
    probability = db.Column(db.String())

    def __init__(self, nama, semester, review, sentiment, probability):
        self.nama = nama
        self.semester = semester
        self.review = review
        self.sentiment = sentiment
        self.probability = probability

    def __repr__(self):
        return f"{self.nama}:{self.nama}"
