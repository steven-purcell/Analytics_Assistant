import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingClassifier, AdaBoostClassifier
from sklearn.metrics import r2_score, f1_score, accuracy_score, precision_score, recall_score, confusion_matrix
from xgboost import XGBClassifier

def preprocess_data(data):
    # Example preprocessing steps
    data = data.dropna()  # Drop missing values
    return data

def model_data(data, target_column):
    data = preprocess_data(data)
    X = data.drop(columns=[target_column])
    y = data[target_column]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    models = {
        # "Linear Regression": LinearRegression(),
        # "Decision Tree": DecisionTreeRegressor(),
        # "Random Forest": RandomForestRegressor(),
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "Gradient Boosting": GradientBoostingClassifier(),
        "AdaBoost": AdaBoostClassifier(),
        "XGBoost": XGBClassifier()
    }

    results = {}
    for name, model in models.items():
        print(f"Testing {name} model...")
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        f1 = f1_score(y_test, y_pred)
        accuracy = accuracy_score(y_test, y_pred)
        results[name] = f1, accuracy

    return results