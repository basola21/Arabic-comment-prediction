import pickle

def predict(text):
    # Load the model from the file

    filename = 'finalized_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    # Use the loaded model to make predictions
    result = loaded_model.predict([text])
    return result[0]