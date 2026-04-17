import joblib
from sklearn.metrics import classification_report


def evaluate():
    model = joblib.load("artifacts/model.pkl")
    print("Model loaded successfully")

    # Extend with test dataset if needed


if __name__ == "__main__":
    evaluate()