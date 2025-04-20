
from flask import Flask, render_template, request
import pickle
import string
from models import db, Review

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reviews.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))
model = pickle.load(open("models/sentiment_model.pkl", "rb"))

def transform_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    review = request.form["review"]
    rating = int(request.form["rating"])
    feedback = request.form.get("feedback", "")
    transformed = transform_text(review)
    vector_input = vectorizer.transform([transformed])
    prediction = model.predict(vector_input)[0]
    sentiment = (
        f"Yikes! Looks like your experience wasn't great — overcrowded and stressful."
        if prediction == 0 else
        "What a wonderful experience! Sounds like a trip to remember."
    )

    new_review = Review(review_text=review, rating=rating, feedback=feedback, sentiment="Positive" if prediction == 1 else "Negative")
    db.session.add(new_review)
    db.session.commit()

    return render_template("result.html", review=review, prediction=sentiment, rating=rating, feedback=feedback)

@app.route("/dashboard")
def dashboard():
    reviews = Review.query.order_by(Review.timestamp.desc()).all()
    sentiments = [r.sentiment for r in reviews]
    ratings = [r.rating for r in reviews]
    labels = [r.timestamp.strftime("%b %d") for r in reviews]
    return render_template("dashboard.html", sentiments=sentiments, ratings=ratings, labels=labels)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
