import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from xgboost import XGBClassifier

from src.data.loader import load_data
from src.data.preprocess import preprocess_data


def train():
    df = load_data("data/sample_data.csv")

    df = preprocess_data(df)

    X = df.drop("target", axis=1)
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = XGBClassifier(
        n_estimators=100,
        max_depth=5,
        learning_rate=0.1
    )

    model.fit(X_train, y_train)

    preds = model.predict_proba(X_test)[:, 1]
    auc = roc_auc_score(y_test, preds)

    print(f"AUC Score: {auc:.4f}")

    joblib.dump(model, "artifacts/model.pkl")


if __name__ == "__main__":
    train()