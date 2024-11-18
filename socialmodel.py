from sklearn.neighbors import KNeighborsClassifier
from sklearn.multioutput import MultiOutputClassifier
import pandas as pd
import joblib
import json

multi_knn_model = joblib.load('./social-media-knn-model.pkl') # Load the KNN model

def make_predictions(user_responses):
    print(user_responses)
    user_df = pd.DataFrame([user_responses])

    user_df = fill_missing_vals(user_df)
    

    return {
        "output" : "This is a test"
    }

def fill_missing_vals(frame):
    return