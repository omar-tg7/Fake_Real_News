# Fake and Real News Detection

## Project Overview
This project uses Machine Learning and Natural Language Processing (NLP) to classify news articles as Fake or Real based on their text.

## Technologies Used
- Python
- Pandas and NumPy
- Scikit-learn
- TF-IDF Vectorization
- Logistic Regression
- Jupyter Notebook

## Dataset
The dataset contains fake and real news articles stored in two CSV files:
- `Fake.csv`
- `True.csv`

The data was cleaned and prepared before training the model.

## Model
- **Text Representation:** TF-IDF
- **Classification Algorithm:** Logistic Regression
- **Train-Test Split:** 80% training, 20% testing

## Results
- **Test Accuracy:** 98.83%

The model was evaluated using accuracy, precision, recall, F1-score, and a confusion matrix.

## Project Structure
```text
Fake_Real_News/
├── data/
│   ├── Fake.csv
│   └── True.csv
├── news_detection.ipynb
├── Fake news model.pkl
├── TFIDF vectorizer.pkl
├── requirements.txt
└── README.md
```

## How to Run
1. Install the required libraries:
   `pip install -r requirements.txt`
2. Open `news_detection.ipynb` in Jupyter Notebook or VS Code.
3. Run the notebook cells in order.

## Disclaimer
This model identifies patterns learned from its training dataset. Its predictions do not independently verify whether a news article is factually true.

## Live Demo

Try the application here:
https://fakerealnews-mknyss79nzfk8jkmzfgrg8.streamlit.app/

## Source Code

https://github.com/omar-tg7/Fake_Real_News
