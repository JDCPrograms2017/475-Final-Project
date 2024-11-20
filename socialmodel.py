from sklearn.neighbors import KNeighborsClassifier
from sklearn.multioutput import MultiOutputClassifier
import pandas as pd
import joblib
import json

multi_knn_model = joblib.load('./social-media-knn-model.pkl') # Load the KNN model

def make_predictions(user_responses):
    print(user_responses)
    user_df = pd.DataFrame([user_responses])

    user_df = fill_missing_vals(user_df) # Compiles a new dataframe with filled information.
    results = multi_knn_model.predict_proba(user_df) # Calculate probabilities of each class!

    return {
        "output" : "This is a test"
    }

def fill_missing_vals(frame):
    feature_information = open("./averages.txt", 'r')
    feature_information.readline() # Skip the first line.
    columns = feature_information.readline().split(',') # Separate the columns by their commas.
    
    binary_class_cols = columns[6:] # Female, Male, Non-Binary, and social media platform classes.
    demographic_cols = columns[:5] # Columns 1 - 5 are the demographic and usage data columns.
    avg_values = feature_information.readline().split(',')
    
    filled_user_data = {}
    index = 0
    for col in demographic_cols:
        if frame.loc[0, col] == 0:
            filled_user_data[col] = float(avg_values[index]) # Get the average value for that column.
        else:
            filled_user_data[col] = frame.loc[0, col]

        index += 1

    for col in binary_class_cols:
        if col in frame.columns: # If the particular column is specified in the input.
            filled_user_data[col] = 1
        else:
            filled_user_data[col] = 0

    resulting_df = pd.DataFrame(filled_user_data) # Compile the filled user data into a Pandas DF.

    return resulting_df