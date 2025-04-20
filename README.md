# 🌍 Travel Reviews Sentiment App

This is a Flask web application that analyzes travel reviews, predicts sentiment, and visualizes user feedback with animations, charts, and a clean dark-mode enabled UI.

---

## ✨ Features

- 🌟 Star rating system
- 💬 Animated sentiment results based on review
- 📊 Dashboard with charts (rating trends, sentiment)
- 🌑 Light/Dark mode switch
- 🧠 Sentiment analysis using a trained ML model
- 📝 Stores reviews, ratings, feedback in SQLite database

---

## 📂 Project Structure

```
travel_reviews_project/
├── app.py
├── models.py
├── models/
│   ├── vectorizer.pkl
│   └── sentiment_model.pkl
├── travel_reviews_cleaned.csv
├── templates/
│   ├── index.html
│   ├── result.html
│   └── dashboard.html
├── static/
│   ├── styles.css
│   └── script.js
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run

1. **Install dependencies**:
    ```
    pip install -r requirements.txt
    ```

2. **Run the app**:
    ```
    python app.py
    ```

3. **Open in browser**:
    ```
    http://127.0.0.1:5000/
    ```

---

## 📊 Dashboard

Access the dashboard at:
```
http://127.0.0.1:5000/dashboard
```

---

## 📦 Dataset

A sample travel reviews dataset (`travel_reviews_cleaned.csv`) is included to train the model.

---

## 🛠 Built With

- Flask
- SQLAlchemy
- Scikit-learn
- Chart.js
- HTML/CSS/JS

---

## 🙌 Author

Made with ❤️ to enhance your travel experiences digitally!