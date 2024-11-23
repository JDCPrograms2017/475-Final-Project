from sklearn.neighbors import KNeighborsClassifier
from sklearn.multioutput import MultiOutputClassifier
import pandas as pd
import joblib
import json

pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.max_columns', None)  # Show all columns

multi_knn_model = joblib.load('./social-media-knn-model.pkl') # Load the KNN model

def make_predictions(user_responses):
    print(user_responses)
    output_classes = ['Happiness', 'Anger', 'Neutral', 'Anxiety', 'Boredom', 'Sadness']

    user_df = fill_missing_vals(user_responses) # Compiles a new dataframe with filled information.
    # results = multi_knn_model.predict_proba(user_df) # Calculate probabilities of each class!
    # print("Model features: ", multi_knn_model.feature_names_in_)
    # print("Resulting dataframe to predict on:\n", user_df)
    
    results = multi_knn_model.predict(user_df)
    print("Predicted classes: ", results)

    resulting_dict = {}
    index = 0
    for res in results.flatten():
        resulting_dict[output_classes[index]] = int(res)
        index += 1

    print(resulting_dict)

    return resulting_dict

def fill_missing_vals(user_dict):
    feature_information = open("./averages.txt", 'r')
    feature_information.readline() # Skip the first line.
    columns = [token.strip() for token in feature_information.readline().split(',')] # Separate the columns by their commas.
    
    gender_cols = columns[6:9] # Female, Male, Non-Binary, and social media platform classes.
    social_platform_cols = columns[9:]
    demographic_cols = columns[:6] # Columns 1 - 5 are the demographic and usage data columns.
    avg_values = feature_information.readline().split(',')
    
    filled_user_data = {}
    index = 0
    for col in demographic_cols:
        if user_dict[col] is None or user_dict[col] == 0:
            filled_user_data[col] = [float(avg_values[index])] # Get the average value for that column.
        else:
            filled_user_data[col] = [user_dict[col]]

        index += 1

    for col in gender_cols:
        if col in user_dict['gender']: # If the particular column is specified in the input.
            filled_user_data[col] = [1]
        else:
            filled_user_data[col] = [0]

    for col in social_platform_cols:
        if col in user_dict['socialMedia']:
            filled_user_data[col] = [1]
        else:
            filled_user_data[col] = [0]

    resulting_df = pd.DataFrame(filled_user_data) # Compile the filled user data into a Pandas DF.

    return resulting_df