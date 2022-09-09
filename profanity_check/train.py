import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.calibration import CalibratedClassifierCV
from sklearn.svm import LinearSVC
import joblib

from utils import pre_process_features

# Read in data
data = pd.read_csv('data/clean_data.csv')
texts = pre_process_features(data['text'].astype(str))
y = data['is_offensive']

# Vectorize the text
vectorizer = CountVectorizer(min_df=0.0001)
X = vectorizer.fit_transform(texts)

# Train the model
model = LinearSVC(class_weight="balanced", dual=False, tol=1e-2, max_iter=1e5)
cclf = CalibratedClassifierCV(base_estimator=model)
cclf.fit(X, y)

# Save the model
joblib.dump(vectorizer, 'data/vectorizer.joblib')
joblib.dump(cclf, 'data/model.joblib')