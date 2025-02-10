class DataModel:
    def __init__(self, data):
        self.data = data
        self.models = {}
    
    def handle_missing_values(self, strategy='mean'):
        if strategy == 'mean':
            self.data.fillna(self.data.mean(), inplace=True)
        elif strategy == 'drop':
            self.data.dropna(inplace=True)
    
    def encode_categorical(self):
        self.data = pd.get_dummies(self.data, drop_first=True)
    
    def train_model(self, model_name, model, X, y):
        model.fit(X, y)
        self.models[model_name] = model
    
    def evaluate_model(self, model_name, X_test, y_test):
        model = self.models.get(model_name)
        if model:
            predictions = model.predict(X_test)
            return {
                'accuracy': accuracy_score(y_test, predictions),
                'confusion_matrix': confusion_matrix(y_test, predictions),
                'classification_report': classification_report(y_test, predictions)
            }
        else:
            raise ValueError("Model not found.")
    
    def preprocess_data(self):
        self.handle_missing_values()
        self.encode_categorical()
        return self.data