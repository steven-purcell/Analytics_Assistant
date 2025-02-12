import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingClassifier, AdaBoostClassifier
from sklearn.metrics import r2_score, f1_score, accuracy_score
from xgboost import XGBClassifier
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def preprocess_data(data):
    # Example preprocessing steps
    data = data.dropna()  # Drop missing values
    return data

def model_data(data, target_column):
    data = preprocess_data(data)
    X = data.drop(columns=[target_column])
    y = data[target_column]

    # Identify categorical columns
    categorical_columns = X.select_dtypes(include=['object', 'category']).columns.tolist()

    # Create a ColumnTransformer to apply OneHotEncoder to categorical columns
    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(), categorical_columns)
        ],
        remainder='passthrough'  # Leave the remaining columns unchanged
    )

    # Encode the non-target variables
    X_encoded = preprocessor.fit_transform(X)

    # Determine if the target variable is categorical or continuous
    if y.dtype == 'object' or y.nunique() < 20:
        # Encode categorical target variable if necessary
        if y.dtype == 'object' or y.dtype.name == 'category':
            label_encoder = LabelEncoder()
            y = label_encoder.fit_transform(y)

        models = {
            "Logistic Regression": LogisticRegression(max_iter=1000),
            "Gradient Boosting": GradientBoostingClassifier(),
            "AdaBoost": AdaBoostClassifier(),
            "XGBoost": XGBClassifier()
        }

        scoring = {
            "f1": lambda y_true, y_pred: f1_score(y_true, y_pred, average='weighted'),
            "accuracy": accuracy_score
        }
    else:
        models = {
            "Linear Regression": LinearRegression(),
            "Decision Tree": DecisionTreeRegressor(),
            "Random Forest": RandomForestRegressor()
        }

        scoring = {
            "r2": r2_score
        }

    X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

    results = {}
    for name, model in models.items():
        print(f"Testing {name} model...")
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        if 'label_encoder' in locals():
            y_test_decoded = label_encoder.inverse_transform(y_test)
            y_pred_decoded = label_encoder.inverse_transform(y_pred)
        else:
            y_test_decoded = y_test
            y_pred_decoded = y_pred

        model_results = {metric: func(y_test_decoded, y_pred_decoded) for metric, func in scoring.items()}
        results[name] = model_results

    # Select the highest performing model based on the primary metric (f1 for classification, r2 for regression)
    best_model_name = max(results, key=lambda k: results[k][list(scoring.keys())[0]])
    best_model = models[best_model_name]
    best_model.fit(X_train, y_train)
    feature_importance = best_model.feature_importances_ if hasattr(best_model, 'feature_importances_') else None

    return best_model_name, results[best_model_name], feature_importance